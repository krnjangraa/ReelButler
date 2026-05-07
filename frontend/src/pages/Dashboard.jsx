import { useEffect } from "react"

import { useState } from "react"

import TrendCard from "../components/TrendCard"

import SearchBar from "../components/SearchBar"

import {

    fetchTrending,

    searchVideos

} from "../services/api"


function Dashboard() {

    const [videos, setVideos] = useState([])

    const [niche, setNiche] = useState(
        "fitness shorts"
    )


    useEffect(() => {

        async function loadData() {

            const data = await fetchTrending(
                niche
            )

            setVideos(data)
        }

        loadData()

    }, [niche])


    async function handleSearch(query) {

        if (query.trim() === "") {

            const data = await fetchTrending(
                niche
            )

            setVideos(data)

            return
        }

        const data = await searchVideos(
            query
        )

        setVideos(data)
    }


    return (

        <div
            style={{
                padding: "20px"
            }}
        >

            <h1>
                Trending Dashboard
            </h1>


            <SearchBar
                onSearch={handleSearch}
            />


            <br />


            <select

                value={niche}

                onChange={(e) =>
                    setNiche(e.target.value)
                }
            >

                <option value="fitness shorts">
                    Fitness
                </option>

                <option value="football edits">
                    Football
                </option>

                <option value="AI tools">
                    AI
                </option>

                <option value="motivation shorts">
                    Motivation
                </option>

            </select>


            <br />
            <br />


            {
                videos.map((video) => (

                    <TrendCard

                        key={video.video_id}

                        video={video}
                    />
                ))
            }

        </div>
    )
}

export default Dashboard