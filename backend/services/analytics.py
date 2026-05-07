from database import SessionLocal

import models


def get_trending_videos(niche):

    db = SessionLocal()

    videos = db.query(
        models.YouTubeVideo
    ).filter(
        models.YouTubeVideo.niche == niche
    ).all()

    results = []

    for video in videos:

        metrics = db.query(
            models.YouTubeMetric
        ).filter(
            models.YouTubeMetric.video_id == video.video_id
        ).order_by(
            models.YouTubeMetric.fetched_at.desc()
        ).limit(2).all()

        # NEED 2 SNAPSHOTS
        if len(metrics) < 2:
            continue

        latest = metrics[0]

        older = metrics[1]

        velocity = latest.views - older.views

        engagement_ratio = 0

        if latest.views > 0:

            engagement_ratio = (
                latest.likes / latest.views
            ) * 100

        trend_score = (
            velocity * 0.7
        ) + (
            engagement_ratio * 0.3
        )

        results.append({

            "video_id": video.video_id,

            "title": video.title,

            "channel_name": video.channel_name,

            "views": latest.views,

            "likes": latest.likes,

            "comments": latest.comments,

            "velocity": velocity,

            "engagement_ratio": round(
                engagement_ratio,
                2
            ),

            "trend_score": round(
                trend_score,
                2
            )
        })

    db.close()

    results.sort(
        key=lambda x: x["trend_score"],
        reverse=True
    )

    return results[:20]