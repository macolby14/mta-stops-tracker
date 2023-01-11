import "./App.css";

function App() {
    return (
        <div className="App">
            <body>
                Width:{" "}
                {Math.max(
                    document.documentElement.clientWidth || 0,
                    window.innerWidth || 0
                )}
                Height:
                {Math.max(
                    document.documentElement.clientHeight || 0,
                    window.innerHeight || 0
                )}
            </body>
        </div>
    );
}

export default App;
