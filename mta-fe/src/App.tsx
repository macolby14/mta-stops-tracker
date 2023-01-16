import React, { useEffect, useState } from "react";
import "./App.css";
import "./reset.css";

async function fetchNextStopTimes() {
    const res = await fetch("/api/stops").then((res) => res.json());
    console.log(res);
    return [4, 10, 15, 20, 30, 40, 50, 60];
}

function App() {
    const [nextStops, setNextStops] = useState<number[]>([]);

    useEffect(() => {
        async function fetchData() {
            const nextStopTimes = await fetchNextStopTimes();
            setNextStops(nextStopTimes);
        }
        fetchData();
    }, []);

    return (
        <div className="App">
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
        </div>
    );
}

export default App;
