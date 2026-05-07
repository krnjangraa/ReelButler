import json

from sentence_transformers import SentenceTransformer

from database import SessionLocal

import models


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


db = SessionLocal()


videos = db.query(
    models.YouTubeVideo
).all()


for video in videos:

    text = f"""

    {video.niche}

    {video.title}

    """

    embedding = model.encode(
        text
    ).tolist()

    video.embedding = json.dumps(
        embedding
    )

    print(
        "Embedded:",
        video.title
    )


db.commit()

db.close()