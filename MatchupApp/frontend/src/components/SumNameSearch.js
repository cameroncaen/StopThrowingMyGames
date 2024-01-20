import React, { Component } from "react";

//import "@fontsource/league-spartan";
//import "@fontsource/be-vietnam-pro";
//import ping from '../../static/images/qping.png';
//import search from '../../static/images/magnifyingglass.png';

export const SumNameSearch = () => {
    return (
        <div>
            <header className="App-header">
                <h2>Stop Throwing My Games</h2>
                <a className="subtitle">Don't get 'd.</a>
            </header>

            <article className="App-body">
                <form>
                    <div class="search-wrapper">
                        <div class="search-container">
                            <input className="ID-search" name="summonerid" placeholder="Summoner Name" />
                            <label className="search-line" />
                            <label className="tag-label">#</label>
                            <input className="tag-search" name="summonertag" maxlength="5" />
                            <button className="search-button" type="submit">
                                
                            </button>
                        </div>
                    </div>
                </form>
                <p className="na-only">Works for NA summoners only.</p>
            </article>
        </div>
    )
}

export default SumNameSearch



// these two images will be in the frontend, however image loading not working yet
// <img src={ping} alt="Question Mark Ping" width="50" height="50" />
// <img src={search} alt="Search" width="30" height="30" />
// fonts also not working rn LOL