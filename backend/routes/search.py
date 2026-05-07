from fastapi import APIRouter

from search.semantic_search import semantic_search


router = APIRouter()


@router.get("/search")
def search(query: str):

    results = semantic_search(query)

    return results