import { useContext } from "react";
import { ModalContext } from "./ModalContext";
import { SettingsDisplay } from "./SettingsDisplay";

export function SettingsModal() {
    const { showModal, setShowModal } = useContext(ModalContext);

    return (
        <dialog
            style={{
                position: "absolute",
                width: "90%",
                height: "90%",
                top: "50%",
                left: "50%",
                transform: "translate(-50%, -50%)",
                overflow: "auto",
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
                <SettingsDisplay />
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
