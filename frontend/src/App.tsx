import "./App.css";
import "./reset.css";
import {Settings} from "./components/Settings/Setttings";
import { NextStopsDisplay } from "./components/NextStopsDisplay/NextStopsDisplay";

function App() {
    return <div className="App">
        <div style={{width: "100%", height: "100%", position: "relative"}}>
        <Settings />
        <NextStopsDisplay />
        </div>
    </div>;
}

export default App;
