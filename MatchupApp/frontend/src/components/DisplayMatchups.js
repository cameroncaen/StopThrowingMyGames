import React, {useState} from "react";
import { useNavigate, useParams } from 'react-router-dom';

export const DisplayMatchups = () => {
    const matchCode = useParams();
    const [hostUser, setHostUser] = useState('');
    const [hostTag, setHostTag] = useState('');
    const [hostLvl, setHostLvl] = useState('');
    const [hostRole, setHostRole] = useState('');

    const [oppUser, setOppUser] = useState('');
    const [oppTag, setOppTag] = useState('');
    const [oppLvl, setoppLvl] = useState('');
    const [oppRole, setOppRole] = useState('');
    
    //console.log(matchCode.sessionCode);
    const getMatchInfo = () => {
        fetch("/api/get-stats" + "?code=" + matchCode.sessionCode)
        .then((response) => response.json())
        .then((data) => {
            setHostUser(data.username)
            setHostTag(data.tag)
            setHostLvl(data.user_sumLevel)
            setHostRole(data.user_role)

            setOppUser(data.opp_username)
            setOppTag(data.opp_tag)
            setoppLvl(data.opp_sumLevel)
            setOppRole(data.opp_role)
        }
       )
    }

    getMatchInfo()

    return (
        <div>
            <header className="App-header">
                <h2>Stop Throwing My Games </h2>
                <a className="subtitle">Don't get 'd.</a>
            </header>
            <article className="App-body">
            <button 
                className="search-button" 
                
            >Player Matchup Analysis </button>
            <h1>user: {matchCode.sessionCode}</h1>
            <h1>user: {hostUser}          Opp: {oppUser}</h1>
            <h1>tag: {hostTag}          OppTag: {oppTag}</h1>
            <h1>user level: {hostLvl}          Opp Level: {oppLvl}</h1>
            <h1>user role: {hostRole}          Opp Role: {oppRole}</h1>
            </article>
            
        </div>
    )
}

export default DisplayMatchups