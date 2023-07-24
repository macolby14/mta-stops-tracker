import { combineReducers } from "redux";
import stationsReducer from "./stationsReducer";
import { configureStore } from "@reduxjs/toolkit";

const rootReducer = combineReducers({
    stations: stationsReducer,
});

export const store = configureStore({ reducer: rootReducer });

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
