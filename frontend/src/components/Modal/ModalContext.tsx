import React, { createContext, useState } from "react";

type ModalContextType = {
    showModal?: boolean;
    setShowModal: React.Dispatch<React.SetStateAction<boolean>>;
};

export const ModalContext = createContext<ModalContextType>({
    showModal: undefined,
    setShowModal: () => {}, //eslint-disable-line @typescript-eslint/no-empty-function
});

interface ModalProviderProps {
    children: React.ReactNode;
}

export function ModalProvider({ children }: ModalProviderProps) {
    const [showModal, setShowModal] = useState(false);

    return (
        <ModalContext.Provider value={{ showModal, setShowModal }}>
            {children}
        </ModalContext.Provider>
    );
}
