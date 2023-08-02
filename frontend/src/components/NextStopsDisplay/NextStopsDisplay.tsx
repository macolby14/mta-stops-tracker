import { useEffect, useState } from "react";
import { styled } from "styled-components";

enum LineColor {
    BLUE = "rgb(0,57,165)",
    ORANGE = "rgb(255,101,28)",
    LIGHT_GREEN = "rgb(108,189,69)",
    GREEN = "rgb(0,165,82)",
    GRAY = "rgb(137,137,137)",
    YELLOW = "rgb(253,204,11)",
    RED = "rgb(236,27,36)",
    PURPLE = "rgb(204,0,203)",
    BROWN = "rgb(153,102,51)",
}

const lineToColor = new Map<string, string>(
    Object.entries({
        A: LineColor.BLUE,
        C: LineColor.BLUE,
        E: LineColor.BLUE,
        B: LineColor.ORANGE,
        D: LineColor.ORANGE,
        F: LineColor.ORANGE,
        M: LineColor.ORANGE,
        G: LineColor.LIGHT_GREEN,
        N: LineColor.YELLOW,
        Q: LineColor.YELLOW,
        R: LineColor.YELLOW,
        W: LineColor.YELLOW,
        J: LineColor.BROWN,
        Z: LineColor.BROWN,
        L: LineColor.GRAY,
        "1": LineColor.RED,
        "2": LineColor.RED,
        "3": LineColor.RED,
        "4": LineColor.GREEN,
        "5": LineColor.GREEN,
        "6": LineColor.GREEN,
        "7": LineColor.PURPLE,
    })
);

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

const LineDirectionContainer = styled.div`
    height: 100%;
    aspect-ratio: "1";
    display: "flex";
    flex-direction: "column";
    align-items: center;
`;

const LineCircle = styled.div`
    background-color: ${(props) => props.color};
    color: white;
    border-radius: 100%;
    aspect-ratio: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    flex: "0 0 80%";
`;

const Direction = styled.div`
    flex: 0 0 20%;
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
                            <LineDirectionContainer>
                                <LineCircle
                                    color={lineToColor.get(stop.line)}
                                    style={{}}
                                >
                                    {stop.line}
                                </LineCircle>
                                <Direction
                                    style={{
                                        flex: "0 0 20%",
                                        fontSize: "2rem",
                                    }}
                                >
                                    {stop.direction}
                                </Direction>
                            </LineDirectionContainer>
                        </NextTimesItem>
                        <NextTimesItem>{stop.time} min</NextTimesItem>
                    </NextTimesRow>
                );
            })}
        </NextTimesContainer>
    );

    return <>{error ? errorDisplay : body}</>;
}
