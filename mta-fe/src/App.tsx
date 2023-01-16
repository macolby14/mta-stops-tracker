import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function fetchNextStopTimes() {
    return [4, 10, 15];
}

function App() {
    const [nextStops, setNextStops] = useState<number[]>([]);

    useEffect(() => {
        setNextStops(fetchNextStopTimes());
    }, []);

    return (
        <div className="App">
            <body>
                {nextStops.map((stopTime) => {
                    return <div>C {stopTime}</div>;
                })}
            </body>
        </div>
    );
}

export default App;
