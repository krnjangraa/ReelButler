import os
import requests

from datetime import datetime, timezone

from dotenv import load_dotenv

from database import SessionLocal

import models


load_dotenv()


API_KEY = os.getenv("YOUTUBE_API_KEY")


SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

VIDEOS_URL = "https://www.googleapis.com/youtube/v3/videos"


NICHES = [

    "fitness shorts",

    "football edits",

    "motivation shorts",

    "AI tools",

    "anime edits"
]


db = SessionLocal()


def discover_videos(keyword):

    # SEARCH VIDEOS
    search_params = {

        "part": "snippet",

        "q": keyword,

        "type": "video",

        "maxResults": 10,

        "key": API_KEY
    }

    response = requests.get(
        SEARCH_URL,
        params=search_params
    )

    data = response.json()

    video_ids = []

    for item in data["items"]:

        video_id = item["id"]["videoId"]

        video_ids.append(video_id)

    # FETCH VIDEO DETAILS
    video_params = {

        "part": "snippet,statistics",

        "id": ",".join(video_ids),

        "key": API_KEY
    }

    response = requests.get(
        VIDEOS_URL,
        params=video_params
    )

    video_data = response.json()

    for item in video_data["items"]:

        video_id = item["id"]

        title = item["snippet"]["title"]

        channel_name = item["snippet"]["channelTitle"]

        published_at = item["snippet"]["publishedAt"]

        views = int(
            item["statistics"].get("viewCount", 0)
        )

        likes = int(
            item["statistics"].get("likeCount", 0)
        )

        comments = int(
            item["statistics"].get("commentCount", 0)
        )

        # FILTER SMALL VIDEOS
        if views < 50000:
            continue

        # CHECK DUPLICATE
        existing = db.query(
            models.YouTubeVideo
        ).filter(
            models.YouTubeVideo.video_id == video_id
        ).first()

        if existing:
            continue

        # STORE STATIC VIDEO INFO
        new_video = models.YouTubeVideo(

            video_id=video_id,

            title=title,

            channel_name=channel_name,

            niche=keyword,

            published_at=published_at
        )

        db.add(new_video)

        # STORE FIRST METRIC SNAPSHOT
        metric = models.YouTubeMetric(

            video_id=video_id,

            views=views,

            likes=likes,

            comments=comments,

            fetched_at=datetime.now(timezone.utc)
        )

        db.add(metric)

        db.commit()

        print("Stored:", title)


def run_discovery():

    print("Running discovery pipeline...")

    for niche in NICHES:

        discover_videos(niche)

