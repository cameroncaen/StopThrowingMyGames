import React, { Component } from "react";
import { render } from "react-dom";
import Hub from './Hub';

export const App = () => {
    return (
        <div>
            <Hub />
        </div>
    )

    
}

export default App;

const appDiv = document.getElementById("app");
render(<App />, appDiv);