import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function fetchNextStopTimes() {
    return [4, 10, 15];
}

type VertifcalFlexContainerProps = {
    children?: React.ReactNode;
};

type FlexItemProps = {
    children?: React.ReactNode;
};

function FlexItem({ children }: FlexItemProps) {
    return <div>{children}</div>;
}

function App() {
    const [nextStops, setNextStops] = useState<number[]>([]);

    useEffect(() => {
        setNextStops(fetchNextStopTimes());
    }, []);

    return (
        <body className="App">
            <div className="VerticalFlexContainer">
                {nextStops.map((stopTime) => {
                    return (
                        <div style={{ flexGrow: 1, border: "1px solid black" }}>
                            C {stopTime}
                        </div>
                    );
                })}
            </div>
        </body>
    );
}

export default App;
