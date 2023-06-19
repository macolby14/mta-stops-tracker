import React, { useEffect, useState } from "react";

import "./NextStopsDisplay.css";


type NextStopsAPIType = {
    line: string;
    station: string;
    nextTimes: number[];
};

export function NextStopsDisplay() {
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
                setError(null);
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
        /* Update every 20 seconds. 20 seconds is arbitrarily smaller than 1 min, time most care about */
        const fetchDataIntervalId = setInterval(fetchData, 20000);

        return () => {
            clearInterval(fetchDataIntervalId);
        };
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

    return <>{error ? errorDisplay : body}</>;
}

