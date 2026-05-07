from rank_bm25 import BM25Okapi

from database import SessionLocal

import models


# DATABASE
db = SessionLocal()


# LOAD VIDEOS
videos = db.query(
    models.YouTubeVideo
).all()


# BM25 DOCUMENTS
documents = []

video_map = []


for video in videos:

    text = f"""

    {video.niche}

    {video.title}

    {video.channel_name}

    """

    tokens = text.lower().split()

    documents.append(tokens)

    video_map.append(video)


# BM25 MODEL
if len(documents) > 0:

    bm25 = BM25Okapi(documents)

else:

    bm25 = None


def hybrid_search(query):

    if bm25 is None:

        return []


    # TOKENIZE QUERY
    query_tokens = query.lower().split()


    # BM25 SCORES
    bm25_scores_raw = bm25.get_scores(
        query_tokens
    )


    results = []


    for i in range(len(bm25_scores_raw)):

        video = video_map[i]

        score = bm25_scores_raw[i]


        results.append({

            "video_id": video.video_id,

            "title": video.title,

            "channel_name": video.channel_name,

            "niche": video.niche,

            "score": float(score)
        })


    # SORT RESULTS
    results.sort(

        key=lambda x: x["score"],

        reverse=True
    )


    return results[:5]
# import json
# import faiss
# import numpy as np

# from sentence_transformers import SentenceTransformer

# from rank_bm25 import BM25Okapi

# from database import SessionLocal

# import models


# # LOAD MODEL
# model = SentenceTransformer(
#     "all-MiniLM-L6-v2"
# )


# # LOAD FAISS INDEX
# index = faiss.read_index(
#     "youtube_index.faiss"
# )


# # LOAD VIDEO IDS
# with open(
#     "video_ids.json",
#     "r"
# ) as file:

#     video_ids = json.load(file)


# # DATABASE
# db = SessionLocal()


# # LOAD VIDEOS
# videos = db.query(
#     models.YouTubeVideo
# ).all()


# # BM25 DOCUMENTS
# documents = []

# video_map = []


# for video in videos:

#     text = f"""

#     {video.niche}

#     {video.title}

#     """

#     tokens = text.lower().split()

#     documents.append(tokens)

#     video_map.append(video)


# # BM25 MODEL
# if len(documents) > 0:

#     bm25 = BM25Okapi(documents)

# else:

#     bm25 = None


# def hybrid_search(query):
        
#     if bm25 is None:

#         return []

#     # -------------------
#     # SEMANTIC SEARCH
#     # -------------------

#     query_embedding = model.encode(
#         query
#     )

#     query_embedding = np.array(
#         [query_embedding],
#         dtype="float32"
#     )

#     distances, indices = index.search(
#         query_embedding,
#         10
#     )

#     semantic_scores = {}

#     for rank, idx in enumerate(indices[0]):

#         video_id = video_ids[idx]

#         # LOWER DISTANCE = BETTER
#         semantic_score = 1 / (
#             1 + distances[0][rank]
#         )

#         semantic_scores[video_id] = semantic_score


#     # -------------------
#     # BM25 SEARCH
#     # -------------------

#     query_tokens = query.lower().split()

#     bm25_scores_raw = bm25.get_scores(
#         query_tokens
#     )

#     bm25_scores = {}

#     for i in range(len(bm25_scores_raw)):

#         video = video_map[i]

#         bm25_scores[
#             video.video_id
#         ] = bm25_scores_raw[i]


#     # -------------------
#     # HYBRID COMBINATION
#     # -------------------

#     combined_results = []


#     for video in videos:

#         semantic_score = semantic_scores.get(
#             video.video_id,
#             0
#         )

#         bm25_score = bm25_scores.get(
#             video.video_id,
#             0
#         )

#         final_score = (

#             semantic_score * 0.7

#             +

#             bm25_score * 0.3
#         )

#         combined_results.append({

#             "video_id": video.video_id,

#             "title": video.title,

#             "channel_name": video.channel_name,

#             "niche": video.niche,

#             "semantic_score": float(
#                 semantic_score
#             ),

#             "bm25_score": float(
#                 bm25_score
#             ),

#             "final_score": float(
#                 final_score
#             )
#         })


#     # SORT BEST RESULTS
#     combined_results.sort(

#         key=lambda x: x["final_score"],

#         reverse=True
#     )


#     return combined_results[:5]

