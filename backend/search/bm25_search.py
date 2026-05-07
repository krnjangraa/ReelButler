from rank_bm25 import BM25Okapi

from database import SessionLocal

import models


db = SessionLocal()


videos = db.query(
    models.YouTubeVideo
).all()


documents = []

video_map = []


for video in videos:

    text = f"""

    {video.niche}

    {video.title}

    """

    tokens = text.lower().split()

    documents.append(tokens)

    video_map.append(video)


bm25 = BM25Okapi(documents)


def bm25_search(query):

    query_tokens = query.lower().split()

    scores = bm25.get_scores(
        query_tokens
    )

    scored_results = []


    for i in range(len(scores)):

        scored_results.append({

            "score": scores[i],

            "video": video_map[i]
        })


    scored_results.sort(

        key=lambda x: x["score"],

        reverse=True
    )


    results = []


    for item in scored_results[:5]:

        video = item["video"]

        results.append({

            "video_id": video.video_id,

            "title": video.title,

            "channel_name": video.channel_name,

            "niche": video.niche,

            "bm25_score": float(
                item["score"]
            )
        })


    return results

