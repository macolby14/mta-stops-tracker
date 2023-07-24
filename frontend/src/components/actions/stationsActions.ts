import { StationSelected } from "../../reducers/stationsReducer";

export const loadStationsSelected = (stations: StationSelected[]) => {
    return {
        type: "LOAD_STATIONS_SELECTED",
        payload: {
            stations,
        },
    } as const;
};
export const setStationsSelected = ({
    id,
    direction,
    selected,
}: Omit<StationSelected, "line">) => {
    return {
        type: "SET_STATION_SELECTED",
        payload: {
            id,
            direction,
            selected,
        },
    } as const;
};

export type StationAction =
    | ReturnType<typeof loadStationsSelected>
    | ReturnType<typeof setStationsSelected>;
