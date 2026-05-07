from agents.base_agent import BaseAgent


class HashtagAgent(

    BaseAgent
):


    def generate_hashtags(
        self,
        query
    ):

        context = self.retrieve_context(
            query
        )


        prompt = f"""

        You are an expert short-form social media growth strategist.

        Generate highly optimized hashtags.

        User Topic:
        {query}

        Viral Trend Examples:
        {context}

        Generate:

        1. Viral hashtags
        2. Niche hashtags
        3. Broad discovery hashtags
        4. Community hashtags
        5. SEO-friendly hashtags

        Also explain why these hashtags work.
        """


        return self.generate_response(
            prompt
        )


# agent = HashtagAgent()


# result = agent.generate_hashtags(

#     "fitness motivation for beginners"
# )

# print(result)