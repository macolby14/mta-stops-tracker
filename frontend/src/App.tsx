import "./App.css";
import "./reset.css";
import { AppBar } from "./components/AppBar/AppBar";
import { NextStopsDisplay } from "./components/NextStopsDisplay/NextStopsDisplay";
import { SettingsModal } from "./components/Modal/SettingsModal";
import { ModalProvider } from "./components/Modal/ModalContext";

function App() {
    return (
        <div className="App">
            <ModalProvider>
                <div
                    style={{
                        width: "100%",
                        height: "100%",
                        display: "flex",
                        flexDirection: "column",
                        position: "relative",
                    }}
                >
                    <AppBar />
                    <NextStopsDisplay />
                    <SettingsModal />
                </div>
            </ModalProvider>
        </div>
    );
}

export default App;
