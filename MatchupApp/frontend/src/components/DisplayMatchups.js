import React from "react";
import { useNavigate } from 'react-router-dom';

export const DisplayMatchups = () => {
    const navigate =  useNavigate();
    
    const navigateSumSearch = () => {
        navigate('/find')
    }
    return (
        <div>
            <header className="App-header">
                <h2>Stop Throwing My Gamess </h2>
                <a className="subtitle">Don't get 'd.</a>
            </header>
            <article className="App-body">
            <button 
                className="search-button" 
                onClick={navigateSumSearch}
            >Player Matchup Analysis </button>
            </article>
        </div>
    )
}

export default DisplayMatchups