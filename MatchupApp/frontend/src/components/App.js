import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";

export const App = () => {
    return (
        <h1>BLLLAARRRSSHHH</h1>
    )
}

export default App

const appDiv = document.getElementById("app")
render(<App />, appDiv);