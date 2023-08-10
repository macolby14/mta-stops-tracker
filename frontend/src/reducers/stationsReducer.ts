import { StationAction } from "../components/actions/stationsActions";

export interface StationSelected {
    id: string; // i.e. A44
    direction: "north" | "south";
    line: string; // i.e. A, C, G etc.
}

const initionalState = {
    stationsSelected: [] as StationSelected[],
};

export default function stationsReducer(
    state = initionalState,
    action: StationAction
) {
    switch (action.type) {
        case "SET_STATION_SELECTED":
            if (action.payload.selected === true) {
                return {
                    ...state,
                    stationsSelected: [
                        ...state.stationsSelected,
                        action.payload,
                    ],
                };
            } else {
                const newStationsSelected = state.stationsSelected.filter(
                    (station: StationSelected) => {
                        if (
                            station.id === action.payload.id &&
                            station.direction === action.payload.direction &&
                            station.line === action.payload.line
                        ) {
                            return false;
                        }
                        return true;
                    }
                );
                return { ...state, stationsSelected: newStationsSelected };
            }
        default:
            return state;
    }
}
