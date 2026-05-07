from agents.trend_analyzer import (
    TrendAnalyzerAgent
)

from agents.script_generator import (
    ScriptGeneratorAgent
)

from agents.psychology_agent import (
    PsychologyAgent
)

from agents.hashtag_agent import (
    HashtagAgent
)


class OrchestratorAgent:


    def __init__(self):

        self.trend_agent = (
            TrendAnalyzerAgent()
        )

        self.script_agent = (
            ScriptGeneratorAgent()
        )

        self.psychology_agent = (
            PsychologyAgent()
        )

        self.hashtag_agent = (
            HashtagAgent()
        )


    def run_workflow(
        self,
        query
    ):

        trend_analysis = (

            self.trend_agent.analyze_trend(
                query
            )
        )


        psychology_analysis = (

            self.psychology_agent
            .analyze_psychology(
                query
            )
        )


        script_generation = (

            self.script_agent.generate_script(
                query
            )
        )


        hashtags = (

            self.hashtag_agent
            .generate_hashtags(
                query
            )
        )


        final_output = f"""

# TREND ANALYSIS

{trend_analysis}



# PSYCHOLOGY ANALYSIS

{psychology_analysis}



# SCRIPT GENERATION

{script_generation}



# HASHTAGS

{hashtags}

"""


        return final_output


# agent = OrchestratorAgent()


# result = agent.run_workflow(

#     "fitness motivation for beginners"
# )

# print(result)