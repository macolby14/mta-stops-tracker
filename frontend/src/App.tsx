import "./App.css";
import "./reset.css";
import { AppBar } from "./components/AppBar/AppBar";
import { NextStopsDisplay } from "./components/NextStopsDisplay/NextStopsDisplay";
import { SettingsModal } from "./components/Modal/Modal";
import { ModalProvider } from "./components/Modal/ModalContext";
import { Provider } from "react-redux";
import { store } from "./reducers/store";

function App() {
    return (
        <Provider store={store}>
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
        </Provider>
    );
}

export default App;
