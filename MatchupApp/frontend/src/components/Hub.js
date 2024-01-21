import React, {Component} from "react";
import HomePage from './HomePage';
import SumNameSearch from './SumNameSearch';
import DisplayMatchup from './DisplayMatchups';
import {
    BrowserRouter as Router,
    Routes,
    Route
} from 'react-router-dom';

export const Hub = () => {
    return (
        <Router>
            <Routes>
                <Route exact path="/" element = {<HomePage />}></Route>
                <Route path="/find" element = {<SumNameSearch />}></Route>
                <Route path="/matchup/:sessionCode" element = {<DisplayMatchup />}></Route>
            </Routes>
        </Router>
    )
}

export default Hub