import { useEffect, useState } from "react";
import settingsImage from "../../images/settings.svg";

export function Settings() {
    const [showDialog, setShowDialog] = useState(false);

    return (
        <div
            style={{
                width: "100%",
                height: "100%",
                position: "absolute",
                zIndex: 1,
            }}
        >
            <SettingsIcon setShowDialog={setShowDialog} />
            <Dialog showDialog={showDialog} setShowDialog={setShowDialog} />
        </div>
    );
}

interface SettingsIconProps {
    setShowDialog: (a: boolean) => void;
}

export function SettingsIcon({ setShowDialog }: SettingsIconProps) {
    return (
        <div
            style={{
                width: "50px",
                height: "50px",
                position: "absolute",
                right: "20px",
                top: "5px",
            }}
            onClick={() => {
                console.log("Clicked on settings");
                setShowDialog(true);
            }}
        >
            <img src={settingsImage} alt="Settings" />
        </div>
    );
}

interface DialogProps {
    showDialog: boolean;
    setShowDialog: (a: boolean) => void;
}

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

export function Dialog({ showDialog, setShowDialog }: DialogProps) {
    const [stations, setStations] = useState<Station[]>([]);

    useEffect(() => {
        async function fetchData() {
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
            console.log({ stations });
            setStations(stations);
        }
        fetchData();
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
            open={showDialog}
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
                    {stations.map((station) => (
                        <div>{station.name}</div>
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
                        setShowDialog(false);
                    }}
                >
                    Exit
                </div>
            </div>
        </dialog>
    );
}
