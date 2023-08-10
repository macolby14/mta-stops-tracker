import { StationSelected } from "../../reducers/stationsReducer";

type SetStationSelected = StationSelected & { selected: boolean };

export const setStationSelected = ({
    id,
    direction,
    selected,
    line,
}: SetStationSelected) => {
    return {
        type: "SET_STATION_SELECTED",
        payload: {
            id,
            direction,
            selected,
            line,
        },
    } as const;
};

export type StationAction = ReturnType<typeof setStationSelected>;
