import { useState } from "react";
import settingsImage from "../../images/settings.svg";
import { TimeDisplay } from "./TimeDisplay";

export function AppBar() {
    const [showDialog, setShowDialog] = useState(false);
    console.log(showDialog); //TODO - Remove. To remove not used error

    return (
        <div
            style={{
                width: "100%",
                height: "64px",
                border: "1px solid black",
                backgroundColor: "#d9d7d77d",
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                gap: "8px",
                padding: "4px 8px",
            }}
        >
            <TimeDisplay />
            <SettingsIcon setShowDialog={setShowDialog} />
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
