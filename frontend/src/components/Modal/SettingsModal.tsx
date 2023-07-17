import { useContext, useEffect, useState } from "react";
import { ModalContext } from "./ModalContext";

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

export function SettingsModal() {
    const { showModal, setShowModal } = useContext(ModalContext);
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
        <dialog
            style={{
                position: "absolute",
                width: "90%",
                height: "90%",
                top: "50%",
                left: "50%",
                transform: "translate(-50%, -50%)",
            }}
            open={showModal}
        >
            <div
                style={{
                    position: "relative",
                    width: "100%",
                    height: "100%",
                    zIndex: 0,
                }}
            >
                <div>
                    <h1>Settings</h1>
                    {stations.map((station, i) => (
                        <div key={i}>{station.name}</div>
                    ))}
                </div>
                <div
                    style={{
                        position: "absolute",
                        zIndex: 1,
                        top: "10px",
                        right: "10px",
                    }}
                    onClick={() => {
                        setShowModal(false);
                    }}
                >
                    Exit
                </div>
            </div>
        </dialog>
    );
}
