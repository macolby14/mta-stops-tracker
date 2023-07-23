import { ChangeEvent, useEffect, useState } from "react";
import { styled } from "styled-components";

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
            id: station.gtfsId, // i.e. A44
            line, // i.e. A, C, G etc.
        };
        delete (stationDisplayRow as Partial<RawStation>).gtfsId; // remove extra property to avoid misuse and confusion
        delete (stationDisplayRow as Partial<RawStation>).lines; // remove extra properties to avoid misuse and confusion
        stationsPerLine.push(stationDisplayRow);
    }
    return stationsPerLine;
}

const ListItem = styled.div`
    flex-grow: 1;
    text-align: center;
`;

const ItemWrapper = styled.div`
    width: 100%;
    display: grid;
    grid-template-columns: 3fr 3fr 2fr 2fr;
    gap: 10px;
    justify-items: center;
    align-items: center;
`;

interface ToggleProps {
    label: string;
    name: string;
    value: string;
    onChange: (ev: ChangeEvent) => void;
    checked: boolean;
}

export function Toggle({ label, name, value, checked, onChange }: ToggleProps) {
    return (
        <>
            <label htmlFor={`${name}-${value}`}>{label}</label>
            <input
                id={`${name}-${value}`}
                name={name}
                value={value}
                type="checkbox"
                checked={checked}
                onChange={onChange}
            />
        </>
    );
}

interface StationSelected {
    id: string; // i.e. A44
    direction: "north" | "south";
    line: string; // i.e. A, C, G etc.
    selected: boolean;
}

/**
 * Displays the settings modal. Shows a list of stations with checkboxes for based on /api/stations endpoint.
 * Stores in state the line (i.e. C, A, G, etc.), the stop id (i.e. A44), and the direction (i.e. N or S)
 */
export function SettingsDisplay() {
    const [stations, setStations] = useState<StationDisplayRow[]>([]);
    const [stationsSelected, setStationsSelected] = useState<StationSelected[]>(
        []
    );

    console.log(stationsSelected.filter((station) => station.selected));

    function handleSelectStation(
        ev: ChangeEvent,
        id: string,
        direction: "north" | "south"
    ) {
        const target = ev.target as HTMLInputElement;
        const checked = target.checked;
        setStationsSelected((prevValues) =>
            prevValues.map((sta) => {
                if (sta.id === id && sta.direction === direction) {
                    return { ...sta, selected: checked };
                }
                return sta;
            })
        );
    }

    useEffect(() => {
        async function fetchStationData() {
            const rawStations: RawStation[] = await fetch("/api/stations").then(
                (resp) => resp.json()
            );
            const stationsDisplayRows = rawStations
                .map((rawStation) => stationDataToDisplayRows(rawStation))
                .flat();
            setStations(stationsDisplayRows);

            const stationsSelectedFromStationRows = stationsDisplayRows
                .map((stationRow) => {
                    return [
                        {
                            id: stationRow.id,
                            direction: "north",
                            line: stationRow.line,
                            selected: false,
                        } as StationSelected,
                        {
                            id: stationRow.id,
                            direction: "south",
                            line: stationRow.line,
                            selected: false,
                        } as StationSelected,
                    ];
                })
                .flat();

            setStationsSelected(stationsSelectedFromStationRows);
        }
        fetchStationData();
    }, []);

    return (
        <div>
            <h1>Settings</h1>
            <div
                style={{ display: "flex", flexDirection: "column", gap: "8px" }}
            >
                {stations.map(
                    ({ name, id, line, northLabel, southLabel }, i) => (
                        <ItemWrapper key={i}>
                            <ListItem>{name}</ListItem>
                            <ListItem>{line}</ListItem>
                            <ListItem>
                                <Toggle
                                    name={id}
                                    value="north"
                                    label={northLabel}
                                    checked={
                                        stationsSelected.find(
                                            (station) =>
                                                station.id === id &&
                                                station.direction === "north"
                                        )?.selected || false
                                    }
                                    onChange={(ev) =>
                                        handleSelectStation(ev, id, "north")
                                    }
                                />
                            </ListItem>
                            <ListItem>
                                <Toggle
                                    name={id}
                                    value="south"
                                    label={southLabel}
                                    checked={
                                        stationsSelected.find(
                                            (station) =>
                                                station.id === id &&
                                                station.direction === "south"
                                        )?.selected || false
                                    }
                                    onChange={(ev) =>
                                        handleSelectStation(ev, id, "south")
                                    }
                                />
                            </ListItem>
                        </ItemWrapper>
                    )
                )}
            </div>
        </div>
    );
}
