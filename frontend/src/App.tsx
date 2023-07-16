import "./App.css";
import "./reset.css";
import { AppBar } from "./components/AppBar/AppBar";
import { NextStopsDisplay } from "./components/NextStopsDisplay/NextStopsDisplay";

function App() {
    return (
        <div className="App">
            <div
                style={{
                    width: "100%",
                    height: "100%",
                    display: "flex",
                    flexDirection: "column",
                }}
            >
                <AppBar />
                <NextStopsDisplay />
            </div>
        </div>
    );
}

export default App;
