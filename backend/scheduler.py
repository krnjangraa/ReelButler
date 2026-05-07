from apscheduler.schedulers.background import BackgroundScheduler
import youtube_discovery

import youtube_tracker

import cleanup


scheduler = BackgroundScheduler()


# DISCOVERY PIPELINE
scheduler.add_job(

    youtube_discovery.run_discovery,

    trigger="interval",

    hours=12
)


# TRACKING PIPELINE
scheduler.add_job(

    youtube_tracker.run_tracker,

    trigger="interval",

    hours=3
)


# CLEANUP PIPELINE
scheduler.add_job(

    cleanup.cleanup_old_data,

    trigger="interval",

    days=1
)


print("Scheduler started...")


scheduler.start()