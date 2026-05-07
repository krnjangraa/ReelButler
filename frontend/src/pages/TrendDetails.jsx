import {

    LineChart,

    Line,

    XAxis,

    YAxis,

    Tooltip,

    CartesianGrid

} from "recharts"

import { useParams } from "react-router-dom"

import { useEffect } from "react"

import { useState } from "react"

import {

    fetchVideoDetails

} from "../services/api"


function TrendDetails() {

    const { videoId } = useParams()

    const [data, setData] = useState([])

    useEffect(() => {

        async function loadData() {

            const result = await fetchVideoDetails(
                videoId
            )

            setData(result)
        }

        loadData()

    }, [])

    return (

        <div>

            <h1>
                Trend Analytics
            </h1>

            <LineChart
                width={900}
                height={400}
                data={data}
            >

                <CartesianGrid />

                <XAxis dataKey="fetched_at" />

                <YAxis />

                <Tooltip />

                <Line
                    type="monotone"
                    dataKey="views"
                />

            </LineChart>

        </div>
    )
}

export default TrendDetails