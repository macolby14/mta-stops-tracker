import { StationAction } from "../components/actions/stationsActions";

export interface StationSelected {
    id: string; // i.e. A44
    direction: "north" | "south";
    line: string; // i.e. A, C, G etc.
    selected: boolean;
}

const initionalState = {
    stationsSelected: [] as StationSelected[],
};

export default function stationsReducer(
    state = initionalState,
    action: StationAction
) {
    switch (action.type) {
        case "LOAD_STATIONS_SELECTED":
            const out = { ...state, stationsSelected: action.payload.stations };
            return out;
        case "SET_STATION_SELECTED":
            const prevStationsSelected = state.stationsSelected;
            const newStationsSelected = prevStationsSelected.map(
                (station: StationSelected) => {
                    if (
                        station.id === action.payload.id &&
                        station.direction === action.payload.direction &&
                        station.line === action.payload.line
                    ) {
                        return {
                            ...station,
                            selected: action.payload.selected,
                        };
                    }
                    return station;
                }
            );
            return { ...state, stationsSelected: newStationsSelected };
        default:
            return state;
    }
}
