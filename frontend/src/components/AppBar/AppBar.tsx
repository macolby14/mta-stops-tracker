import { TimeDisplay } from "./TimeDisplay";
import { SettingsIcon } from "./SettingsIcon";

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
