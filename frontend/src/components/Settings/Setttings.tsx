import { useState } from "react";
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

export function Dialog({ showDialog, setShowDialog }: DialogProps) {
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
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing
                        elit. Ducimus excepturi nihil unde modi ut quo, ea error
                        impedit possimus magnam? Veniam repudiandae eveniet
                        ullam quidem nobis iste laudantium perferendis. Nulla.
                    </p>
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
