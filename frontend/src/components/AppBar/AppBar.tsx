import settingsImage from "../../images/settings.svg";
import { TimeDisplay } from "./TimeDisplay";
import { ModalContext, ModalProvider } from "../Modal/ModalContext";
import { useContext } from "react";

export function AppBar() {
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
            <SettingsIcon />
        </div>
    );
}

export function SettingsIcon() {
    const { setShowModal } = useContext(ModalContext);

    return (
        <div
            style={{
                width: "50px",
                height: "50px",
            }}
            onClick={() => {
                console.log("Clicked on settings");
                setShowModal(true);
            }}
        >
            <img src={settingsImage} alt="Settings" />
        </div>
    );
}
