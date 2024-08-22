"use client";

import React, {createContext, useContext, useState} from 'react';

// Create a Context
const SomeContext = createContext();

// Create a provider component
export function SomeProvider({children}) {
    const [state, setState] = useState('Initial State');

    return (
        <SomeContext.Provider value={{state, setState}}>
            {children}
        </SomeContext.Provider>
    );
}

// Custom hook to use the context
export function useSomeContext() {
    return useContext(SomeContext);
}
