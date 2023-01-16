import React, { useEffect, useState } from "react";
import "./App.css";
import "./reset.css";

function fetchNextStopTimes() {
    return [4, 10, 15, 20, 30, 40, 50, 60];
}

function App() {
    const [nextStops, setNextStops] = useState<number[]>([]);

    useEffect(() => {
        setNextStops(fetchNextStopTimes());
    }, []);

    return (
        <body className="App">
            <div className="NextTimesContainer VerticalFlexContainer">
                {nextStops.map((stopTime) => {
                    return (
                        <div className="NextTimesContainerChild NextTimesItem">
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
        </body>
    );
}

export default App;
