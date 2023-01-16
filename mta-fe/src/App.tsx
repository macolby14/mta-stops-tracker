import React, { useEffect, useState } from "react";
import "./App.css";
import "./reset.css";

type NextStopsAPIType = {
    line: string;
    station: string;
    nextTimes: number[];
};

function App() {
    const [nextStops, setNextStops] = useState<number[]>([]);
    const [error, setError] = useState<string | null>(null);

    async function fetchNextStopTimes() {
        const res = (await fetch("/api/stops")
            .then((res) => {
                if (!res.ok) {
                    console.error("Error fetching /api/stops");
                    throw new Error(
                        `Fetch Failed. Status:${res.status}, Message: ${res.statusText}`
                    );
                }
                return res.json();
            })
            .catch((err) => {
                console.error(err.message);
                setError(err.message);
            })) as NextStopsAPIType;
        return res.nextTimes;
    }

    useEffect(() => {
        async function fetchData() {
            const nextStopTimes = await fetchNextStopTimes();
            setNextStops(nextStopTimes);
        }
        fetchData();
    }, []);

    const errorDisplay = <div>Error {error}</div>;

    const body = (
        <div className="NextTimesContainer VerticalFlexContainer">
            {nextStops.map((stopTime, ind) => {
                return (
                    <div
                        key={ind}
                        className="NextTimesContainerChild NextTimesItem"
                    >
                        <div className="NextTimesItemContent NextTimesItemContainer">
                            <div className="NextTimesItemCircle">
                                <div>C</div>
                            </div>
                        </div>
                        <div className="NextTimesItemContent NextTimesItemTime">
                            {stopTime} min
                        </div>
                    </div>
                );
            })}
        </div>
    );

    return <div className="App">{error ? errorDisplay : body}</div>;
}

export default App;
