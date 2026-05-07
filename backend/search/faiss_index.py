import json
import faiss
import numpy as np

from database import SessionLocal

import models


db = SessionLocal()


videos = db.query(
    models.YouTubeVideo
).all()


embeddings = []

video_ids = []


for video in videos:

    if not video.embedding:
        continue

    embedding = json.loads(
        video.embedding
    )

    embeddings.append(embedding)

    video_ids.append(video.video_id)


embedding_matrix = np.array(
    embeddings,
    dtype="float32"
)


dimension = embedding_matrix.shape[1]


index = faiss.IndexFlatL2(
    dimension
)


index.add(embedding_matrix)


faiss.write_index(
    index,
    "youtube_index.faiss"
)


with open(
    "video_ids.json",
    "w"
) as file:

    json.dump(
        video_ids,
        file
    )


print("FAISS index created")