export async function fetchTrending(niche) {

    const response = await fetch(

        `/trending/${niche}`
    )

    const data = await response.json()

    return data
}

export async function fetchVideoDetails(
    videoId
) {

    const response = await fetch(
        `/video/${videoId}`
    )

    const data = await response.json()

    return data
}

export async function searchVideos(
    query
) {

    const response = await fetch(

        `/search?query=${query}`
    )

    const data = await response.json()

    return data
}