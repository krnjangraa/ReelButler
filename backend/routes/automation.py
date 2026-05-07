from fastapi import APIRouter

import youtube_discovery
import youtube_tracker
import cleanup


router = APIRouter()


@router.get("/run-discovery")
def run_discovery():

    youtube_discovery.run_discovery()

    return {
        "message": "Discovery completed"
    }


@router.get("/run-tracker")
def run_tracker():

    youtube_tracker.run_tracker()

    return {
        "message": "Tracking completed"
    }


@router.get("/run-cleanup")
def run_cleanup():

    cleanup.cleanup_old_data()

    return {
        "message": "Cleanup completed"
    }