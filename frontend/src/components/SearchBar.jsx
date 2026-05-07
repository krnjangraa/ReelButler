import { useState } from "react"


function SearchBar({ onSearch }) {

    const [query, setQuery] = useState("")


    function handleSearch() {

        onSearch(query)
    }

    return (

        <div>

            <input

                type="text"

                placeholder="Search trends..."

                value={query}

                onChange={(e) =>
                    setQuery(e.target.value)
                }
            />

            <button
                onClick={handleSearch}
            >
                Search
            </button>

        </div>
    )
}

export default SearchBar