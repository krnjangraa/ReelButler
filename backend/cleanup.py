from datetime import datetime, timedelta, timezone
from database import SessionLocal

import models


def cleanup_old_data():

    print("Running cleanup pipeline...")

    db = SessionLocal()

    cutoff_time = datetime.now(timezone.utc) - timedelta(days=14)

    old_metrics = db.query(
        models.YouTubeMetric
    ).filter(
        models.YouTubeMetric.fetched_at < str(cutoff_time)
    )

    deleted_count = old_metrics.count()

    old_metrics.delete()

    db.commit()

    print(f"Deleted {deleted_count} old rows")

    db.close()