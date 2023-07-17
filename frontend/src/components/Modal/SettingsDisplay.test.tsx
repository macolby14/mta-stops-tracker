import { stationDataToDisplayRows } from "./SettingsDisplay.js";

const exampleRawStation = {
    name: "Example Station",
    lines: "A",
    gtfsId: "id1",
    northLabel: "North Name",
    southLabel: "South Name",
};

const exampleRawStationMultipleLines = {
    name: "Example Station",
    lines: "A B",
    gtfsId: "id1",
    northLabel: "North Name",
    southLabel: "South Name",
};

const exampleStationDisplay1 = {
    name: "Example Station",
    line: "A",
    id: "id1",
    northLabel: "North Name",
    southLabel: "South Name",
};

const exampleStationDisplay2 = {
    name: "Example Station",
    line: "B",
    id: "id1",
    northLabel: "North Name",
    southLabel: "South Name",
};

test("Produces one single row when converting station with one line", () => {
    expect(stationDataToDisplayRows(exampleRawStation)).toEqual([
        exampleStationDisplay1,
    ]);
});

test("Produces multiple rows when converting station with multiple lines", () => {
    expect(stationDataToDisplayRows(exampleRawStationMultipleLines)).toEqual([
        exampleStationDisplay1,
        exampleStationDisplay2,
    ]);
});
