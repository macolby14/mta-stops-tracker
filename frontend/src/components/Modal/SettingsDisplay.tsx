import { useEffect, useState } from "react";

interface RawStation {
    name: string;
    lines: string;
    id: string;
    northLabel: string;
    southLabel: string;
}

interface Station {
    name: string;
    line: string;
    id: string;
    southLabel: string;
    northLabel: string;
}

export function SettingsDisplay() {
    const [stations, setStations] = useState<Station[]>([]);

    useEffect(() => {
        async function fetchStationData() {
            const rawStations: RawStation[] = await fetch("/api/stations").then(
                (resp) => resp.json()
            );
            const stations = rawStations
                .map((station) => {
                    const stationsPerLine: Station[] = [];
                    for (const line of station.lines.split(" ")) {
                        stationsPerLine.push({
                            ...station,
                            line,
                        });
                    }
                    return stationsPerLine;
                })
                .flat();
            setStations(stations);
        }
        fetchStationData();
    }, []);

    return (
        <div>
            <h1>Settings</h1>
            {stations.map((station, i) => (
                <div key={i}>{station.name}</div>
            ))}
        </div>
    );
}
