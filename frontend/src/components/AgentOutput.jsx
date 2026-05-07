function AgentOutput({ output }) {

    return (

        <div

            style={{
                marginTop: "30px",
                padding: "20px",
                border: "1px solid white",
                borderRadius: "10px",
                whiteSpace: "pre-wrap"
            }}
        >

            {output}

        </div>
    )
}

export default AgentOutput