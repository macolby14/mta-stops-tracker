import { useEffect, useState } from "react";
import { styled } from "styled-components";

type NextStop = {
    line: string;
    station: string;
    time: number;
    direction: string;
};

const NextTimesContainer = styled.div`
    display: flex;
    flex-direction: column;
    overflow-y: scroll;
`;

const NextTimesRow = styled.div`
    flex: 0 0 40%;
    border: 1px solid black;
    display: flex;
    flex-direction: row;
    position: relative;
`;

const NextTimesItem = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 6rem;
    padding: 8px;
    flex-grow: 1;
`;

const ACLineCircle = styled.div`
    background-color: blue;
    color: white;
    border-radius: 100%;
    height: 100%;
    aspect-ratio: 1;
    display: flex;
    align-items: center;
    justify-content: center;
`;

export function NextStopsDisplay() {
    const [nextStops, setNextStops] = useState<NextStop[]>([]);
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
            })) as NextStop[];
        return res;
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
        <NextTimesContainer>
            {nextStops.map((stop, ind) => {
                return (
                    <NextTimesRow key={ind}>
                        <NextTimesItem>
                            <ACLineCircle>{stop.line}</ACLineCircle>
                        </NextTimesItem>
                        <NextTimesItem>{stop.time} min</NextTimesItem>
                    </NextTimesRow>
                );
            })}
        </NextTimesContainer>
    );

    return <>{error ? errorDisplay : body}</>;
}
