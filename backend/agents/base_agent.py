import os

from dotenv import load_dotenv

from google import genai

from search.hybrid_search import hybrid_search


load_dotenv()


class BaseAgent:


    def __init__(self):

        self.client = genai.Client(

            api_key=os.getenv(
                "GEMINI_API_KEY"
            )
        )


    # -------------------------
    # RETRIEVE RELEVANT TRENDS
    # -------------------------

    def retrieve_context(
        self,
        query
    ):

        search_results = hybrid_search(
            query
        )

        context = ""


        for result in search_results:

            context += f"""

            Title:
            {result['title']}

            Niche:
            {result['niche']}

            Channel:
            {result['channel_name']}

            """


        return context


    # -------------------------
    # GENERATE LLM RESPONSE
    # -------------------------

    def generate_response(
        self,
        prompt
    ):

        try:

            response = self.client.models.generate_content(

                model="gemini-3.1-flash-lite-preview",

                contents=prompt
            )

            return response.text


        except Exception as e:

            return str(e)