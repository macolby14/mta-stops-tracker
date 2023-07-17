import { useContext } from "react";
import { ModalContext } from "../Modal/ModalContext";
import settingsImage from "../../images/settings.svg";

export function SettingsIcon() {
    const { setShowModal } = useContext(ModalContext);

    return (
        <div
            style={{
                width: "50px",
                height: "50px",
            }}
            onClick={() => {
                setShowModal(true);
            }}
        >
            <img src={settingsImage} alt="Settings" />
        </div>
    );
}
