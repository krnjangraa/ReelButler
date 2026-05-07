import { Link } from "react-router-dom"

function TrendCard({ video }) {

    return (

        <Link
            to={`/video/${video.video_id}`}
            style={{
                textDecoration: "none",
                color: "white"
            }}
        >

            <div
                style={{
                    border: "1px solid white",
                    padding: "20px",
                    marginBottom: "20px",
                    borderRadius: "10px",
                    cursor: "pointer"
                }}
            >

                <h2>
                    {video.title}
                </h2>

                <p>
                    Channel:
                    {" "}
                    {video.channel_name}
                </p>

                <p>
                    Views:
                    {" "}
                    {video.views}
                </p>

                <p>
                    Velocity:
                    {" "}
                    {video.velocity}
                </p>

                <p>
                    Engagement:
                    {" "}
                    {video.engagement_ratio}%
                </p>

                <p>
                    Trend Score:
                    {" "}
                    {video.trend_score}
                </p>

            </div>

        </Link>
    )
}

export default TrendCard