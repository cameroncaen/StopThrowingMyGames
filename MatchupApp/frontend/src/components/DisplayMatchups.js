import React, {useState} from "react";
import { useNavigate, useParams } from 'react-router-dom';

export const DisplayMatchups = () => {
    const matchCode = useParams();
    const [hostUser, setHostUser] = useState('');
    const [hostTag, setHostTag] = useState('');
    
    //console.log(matchCode.sessionCode);
    const getMatchInfo = () => {
        fetch("/api/get-stats" + "?code=" + matchCode.sessionCode)
        .then((response) => response.json())
        .then((data) => {
            setHostUser(data.username)
            setHostTag(data.tag)
        }
       )
    }

    getMatchInfo()

    return (
        <div>
            <header className="App-header">
                <h2>Stop Throwing My Gamess </h2>
                <a className="subtitle">Don't get 'd.</a>
            </header>
            <article className="App-body">
            <button 
                className="search-button" 
                
            >Player Matchup Analysis </button>
            <p>user: {matchCode.sessionCode}</p>
            <p>user: {hostUser}</p>
            <p>tag: {hostTag}</p>
            </article>
            
        </div>
    )
}

export default DisplayMatchups