from agents.base_agent import BaseAgent


class PsychologyAgent(

    BaseAgent
):


    def analyze_psychology(
        self,
        query
    ):

        context = self.retrieve_context(
            query
        )


        prompt = f"""

        You are an expert viral content psychology analyst.

        Analyze the following viral content trends.

        User Topic:
        {query}

        Viral Content:
        {context}

        Explain:

        1. Emotional triggers
        2. Curiosity gaps
        3. FOMO elements
        4. Attention retention methods
        5. Why viewers engage
        6. Audience behavior psychology

        Keep analysis detailed and actionable.
        """


        return self.generate_response(
            prompt
        )


# agent = PsychologyAgent()


# result = agent.analyze_psychology(

#     "fitness motivation for beginners"
# )

# print(result)