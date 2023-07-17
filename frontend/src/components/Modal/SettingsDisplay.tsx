import { useEffect, useState } from "react";

interface RawStation {
    name: string;
    lines: string;
    gtfsId: string;
    northLabel: string;
    southLabel: string;
}

interface StationDisplayRow {
    name: string;
    line: string;
    id: string;
    southLabel: string;
    northLabel: string;
}

/**
 * Produces station data formatted for display (station name, line name, south label, north label)
 * given the raw data from MTA API
 */
export function stationDataToDisplayRows(
    station: RawStation
): StationDisplayRow[] {
    const stationsPerLine: StationDisplayRow[] = [];
    for (const line of station.lines.split(" ")) {
        const stationDisplayRow = {
            ...station,
            id: station.gtfsId,
            line,
        };
        delete (stationDisplayRow as Partial<RawStation>).gtfsId; // remove extra property to avoid misuse and confusion
        delete (stationDisplayRow as Partial<RawStation>).lines; // remove extra properties to avoid misuse and confusion
        stationsPerLine.push(stationDisplayRow);
    }
    return stationsPerLine;
}

export function SettingsDisplay() {
    const [stations, setStations] = useState<StationDisplayRow[]>([]);

    useEffect(() => {
        async function fetchStationData() {
            const rawStations: RawStation[] = await fetch("/api/stations").then(
                (resp) => resp.json()
            );
            const stationsDisplayRows = rawStations
                .map((rawStation) => stationDataToDisplayRows(rawStation))
                .flat();
            setStations(stationsDisplayRows);
        }
        fetchStationData();
    }, []);

    return (
        <div>
            <h1>Settings</h1>
            {stations.map(({ name, id, line, northLabel, southLabel }) => (
                <div key={id}>
                    {name} {line} {northLabel} {southLabel}
                </div>
            ))}
        </div>
    );
}
