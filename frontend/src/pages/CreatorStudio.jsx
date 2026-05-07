import { useState } from "react"

import AgentOutput from "../components/AgentOutput"
const API_URL = import.meta.env.VITE_API_URL

function CreatorStudio() {

    const [topic, setTopic] = useState("")

    const [loading, setLoading] = useState(false)

    const [output, setOutput] = useState("")


    async function runWorkflow() {

    setLoading(true)

    setOutput("")


    const response = await fetch(

        `${API_URL}/run-workflow`,

        {

            method: "POST",

            headers: {

                "Content-Type":
                "application/json"
            },

            body: JSON.stringify({

                topic: topic
            })
        }
    )


    const data = await response.json()

    setOutput(data.response)

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

                onClick={runWorkflow}

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