const API_URL = import.meta.env.VITE_API_URL


export async function fetchTrending(
    niche
) {

    const response = await fetch(

        `${API_URL}/trending/${niche}`
    )

    const data = await response.json()

    return data
}


export async function fetchVideoDetails(
    videoId
) {

    const response = await fetch(

        `${API_URL}/video/${videoId}`
    )

    const data = await response.json()

    return data
}


export async function searchVideos(
    query
) {

    const response = await fetch(

        `${API_URL}/search?query=${query}`
    )

    const data = await response.json()

    return data
}


export async function runWorkflow(
    topic
) {

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

    return data
}