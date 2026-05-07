from agents.base_agent import BaseAgent


class TrendAnalyzerAgent(

    BaseAgent
):


    def analyze_trend(
        self,
        query
    ):

        # RETRIEVE CONTEXT
        context = self.retrieve_context(
            query
        )


        # BUILD PROMPT
        prompt = f"""

        You are an expert social media trend analyst.

        Analyze the following viral trends.

        User Query:
        {query}

        Viral Trend Examples:
        {context}

        Explain:

        1. Common patterns
        2. Why these trends work
        3. Audience psychology
        4. Content opportunities
        5. Recommendations for creators

        Keep answer detailed and structured.
        """


        # GENERATE RESPONSE
        return self.generate_response(
            prompt
        )


# agent = TrendAnalyzerAgent()


