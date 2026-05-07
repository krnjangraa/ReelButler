import { useState } from "react"

import AgentOutput from "../components/AgentOutput"

import {
    runWorkflow
} from "../services/api"


function CreatorStudio() {

    const [topic, setTopic] = useState("")

    const [loading, setLoading] = useState(false)

    const [output, setOutput] = useState("")


    async function handleWorkflow() {

        setLoading(true)

        setOutput("")

        try {

            const data = await runWorkflow(
                topic
            )

            setOutput(
                data.response
            )

        } catch (error) {

            console.error(error)
        }

        setLoading(false)
    }


    return (

        <div
            style={{
                padding: "20px"
            }}
        >

            <h1>
                AI Creator Studio
            </h1>


            <input

                type="text"

                placeholder="Enter topic..."

                value={topic}

                onChange={(e) =>
                    setTopic(e.target.value)
                }

                style={{
                    width: "400px",
                    padding: "10px"
                }}
            />


            <button

                onClick={handleWorkflow}

                style={{
                    marginLeft: "10px",
                    padding: "10px"
                }}
            >

                Run AI Workflow

            </button>


            {
                loading && (

                    <p>
                        Generating...
                    </p>
                )
            }


            {
                output && (

                    <AgentOutput
                        output={output}
                    />
                )
            }

        </div>
    )
}

export default CreatorStudio