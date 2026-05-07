import os
import requests


from datetime import datetime, timezone

from dotenv import load_dotenv

from database import SessionLocal

import models


load_dotenv()


API_KEY = os.getenv("YOUTUBE_API_KEY")


VIDEOS_URL = "https://www.googleapis.com/youtube/v3/videos"


def run_tracker():

    print("Running tracking pipeline...")

    db = SessionLocal()

    videos = db.query(
        models.YouTubeVideo
    ).all()

    video_ids = []

    for video in videos:

        video_ids.append(video.video_id)

    if len(video_ids) == 0:

        print("No videos to track")

        return

    # BATCH OF 50 IDS
    for i in range(0, len(video_ids), 50):

        batch = video_ids[i:i+50]

        params = {

            "part": "statistics",

            "id": ",".join(batch),

            "key": API_KEY
        }

        response = requests.get(
            VIDEOS_URL,
            params=params
        )

        data = response.json()

        for item in data["items"]:

            video_id = item["id"]

            views = int(
                item["statistics"].get("viewCount", 0)
            )

            likes = int(
                item["statistics"].get("likeCount", 0)
            )

            comments = int(
                item["statistics"].get("commentCount", 0)
            )

            metric = models.YouTubeMetric(

                video_id=video_id,

                views=views,

                likes=likes,

                comments=comments,

                fetched_at=datetime.now(timezone.utc)
            )

            db.add(metric)

        db.commit()

        print("Tracked batch")

    db.close()

