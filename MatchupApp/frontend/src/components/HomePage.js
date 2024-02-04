import React from "react";
import { useNavigate } from 'react-router-dom';

import ping from '../../static/images/qping.png';
import search from '../../static/images/magnifyingglass.png';

export const HomePage = () => {
    const navigate =  useNavigate();
    
    const navigateSumSearch = () => {
        navigate('/find')
    }
    return (
        <div>
            <header className="App-header">
                <h2>Stop Throwing My Games </h2>
                <a className="subtitle">Don't get <img src={ping} alt="Question Mark Ping" width="50" height="50" />'d.</a>
            </header>
            <article className="App-body">
                <div class="search-wrapper">
                    <div class="search-container">
                        <button 
                            className="search-button" 
                            onClick={navigateSumSearch}
                        >
                            <img src={search} alt="Search" />
                        </button>
                    </div>
                </div>
                <p className="na-only">Works for NA summoners only.</p>
            </article>
        </div>
    )
}

export default HomePage