import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

from database import SessionLocal

import models


# LOAD EMBEDDING MODEL
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# LOAD FAISS INDEX
index = faiss.read_index(
    "youtube_index.faiss"
)


# LOAD VIDEO IDS
with open(
    "video_ids.json",
    "r"
) as file:

    video_ids = json.load(file)


db = SessionLocal()


def semantic_search(query):

    # CONVERT QUERY TO EMBEDDING
    query_embedding = model.encode(
        query
    )

    query_embedding = np.array(
        [query_embedding],
        dtype="float32"
    )

    # SEARCH FAISS
    distances, indices = index.search(
        query_embedding,
        5
    )

    results = []

    for idx in indices[0]:

        video_id = video_ids[idx]

        video = db.query(
            models.YouTubeVideo
        ).filter(
            models.YouTubeVideo.video_id == video_id
        ).first()

        if not video:
            continue

        results.append({

            "video_id": video.video_id,

            "title": video.title,

            "channel_name": video.channel_name,

            "niche": video.niche
        })

    return results

