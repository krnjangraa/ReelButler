from fastapi import APIRouter

from search.hybrid_search import hybrid_search


router = APIRouter()


@router.get("/search")
def search(query: str):

    results = hybrid_search(query)

    return results
    