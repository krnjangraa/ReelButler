from fastapi import APIRouter

from services.analytics import get_trending_videos

from database import SessionLocal
import models

router = APIRouter()

@router.get("/trending/{niche}")
def trending(niche: str):

    return get_trending_videos(niche)


@router.get("/video/{video_id}")
def video_details(video_id: str):

    db = SessionLocal()

    metrics = db.query(
        models.YouTubeMetric
    ).filter(
        models.YouTubeMetric.video_id == video_id
    ).order_by(
        models.YouTubeMetric.fetched_at.asc()
    ).all()

    result = []

    for metric in metrics:

        result.append({

            "views": metric.views,

            "likes": metric.likes,

            "comments": metric.comments,

            "fetched_at": metric.fetched_at
        })

    db.close()

    return result