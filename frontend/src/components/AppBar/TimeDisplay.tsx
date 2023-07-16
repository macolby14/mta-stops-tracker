import { useEffect, useState } from "react";

export function TimeDisplay() {
    const [currentTime, setCurrentTime] = useState(new Date());

    /**
     * Update the time state every second
     */
    useEffect(() => {
        const timerID = setInterval(() => {
            setCurrentTime(new Date());
        }, 1000);

        // Cleanup the interval on unmount
        return () => clearInterval(timerID);
    }, []);

    const hours = currentTime.getHours().toString().padStart(2, "0");
    const minutes = currentTime.getMinutes().toString().padStart(2, "0");

    const formattedTime = `${hours}:${minutes}`;

    return <div style={{ fontSize: "48px" }}>{formattedTime}</div>;
}
