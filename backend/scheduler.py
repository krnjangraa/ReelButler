from apscheduler.schedulers.background import (
    BackgroundScheduler
)

import youtube_discovery
import youtube_tracker
import cleanup


scheduler = BackgroundScheduler()


scheduler.add_job(

    youtube_discovery.run_discovery,

    trigger="interval",

    hours=12
)


scheduler.add_job(

    youtube_tracker.run_tracker,

    trigger="interval",

    hours=3
)


scheduler.add_job(

    cleanup.cleanup_old_data,

    trigger="interval",

    days=1
)


def start_scheduler():

    scheduler.start()

    print("Scheduler started...")