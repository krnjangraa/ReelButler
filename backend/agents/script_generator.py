from agents.base_agent import BaseAgent


class ScriptGeneratorAgent(

    BaseAgent
):


    def generate_script(
        self,
        query
    ):

        # -------------------------
        # RETRIEVE VIRAL CONTEXT
        # -------------------------

        context = self.retrieve_context(
            query
        )


        # -------------------------
        # BUILD PROMPT
        # -------------------------

        prompt = f"""

        You are an expert viral short-form content strategist.

        Create a highly engaging short-form reel script.

        User Topic:
        {query}

        Similar Viral Content:
        {context}

        Generate:

        1. Hook
        2. Full Script
        3. CTA
        4. Hashtags
        5. Editing Suggestions
        6. Why This Script Can Perform Well

        Keep it optimized for:
        - TikTok
        - YouTube Shorts
        - Instagram Reels

        Make the hook extremely attention-grabbing.
        """


        # -------------------------
        # GENERATE RESPONSE
        # -------------------------

        return self.generate_response(
            prompt
        )


# agent = ScriptGeneratorAgent()


# result = agent.generate_script(

#     "fitness motivation for beginners"
# )

# print(result)