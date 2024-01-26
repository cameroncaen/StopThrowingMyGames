import React, { Component, useState } from "react";
import { useNavigate, Link } from 'react-router-dom';
import '../../static/css/index.css'

import ping from '../../static/images/qping.png';
import search from '../../static/images/magnifyingglass.png';

export const SumNameSearch = () => {
    const [riotId, setRiotId] = useState('');
    const [riotTag, setRiotTag] = useState('');

    const navigate = useNavigate();

    const requestOptions = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            //These keys must match the backend variables from views.py EXACTLY, the values of course can differ
            username: riotId,
            tag: riotTag,
        }),
    };

    //For invalid riot tags, must have a function to check them and update if the input is valid accordingly

    function findMatchup () {
        
        fetch('/api/gen-stats', requestOptions)
        .then((response) => response.json())
        .then((data) => navigate('/matchup/' + data.code))
        
        //navigate('/matchup/12345'), data)
        
       //setTemp(temp + 1)
       //navigate('/matchup')
    }

    return (
        <div>
            <header className="App-header">
                <h2>Stop Throwing My Gamess</h2>
                <a className="subtitle">Don't get <img src={ping} alt="Question Mark Ping" width="50" height="50" />'d.</a>
            </header>

            <article className="App-body">
                {/* the form tag causes a page refresh after search, hypothesis one of two ways */}
                {/* 1: youtube tutorial way without form to allow to fetching of page and returning of new one */}
                {/* 2: reseearch how the form tag operates and see if it can be called from there */}
                {/* way 2 NOTE: there is an error in the console when the form tag is included the way it is */}
                {/* No label associated with a form */}

                <div class="search-wrapper">
                    <div class="search-container">
                        <input 
                            className="ID-search" 
                            name="summonerid" 
                            placeholder="Summoner Name" 
                            onChange={(newRiotId) => setRiotId(newRiotId.target.value)}
                        />
                        <label className="search-line" />
                        <label className="tag-label">#</label>
                        <input 
                            className="tag-search" 
                            name="tagline" 
                            maxlength="5" 
                            onChange={(newRiotTag) => setRiotTag(newRiotTag.target.value)}
                        />
                        <button 
                            className="search-button" 
                            //type="submit"
                            onClick={findMatchup}
                        >
                            <img src={search} alt="Search" width='30' height='30' />
                        </button>
                    </div>
                </div>
                <p className="na-only">Works for NA summoners only.</p>
            </article>
        </div>
    )
}

export default SumNameSearch
