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
            <header className="matchup-header">
                <h2>{hostUser}'s Game</h2>
                <hr className="matchup-title-divider"></hr>
            </header>
            <article className="matchup-body">
                <h1 className="room-code">user: {matchCode.sessionCode}</h1>
                <div className="main-matchup-wrapper">
                    <div className="main-matchup-user">
                        <h1>user: {hostUser}</h1>
                        <h1>tag: {hostTag}</h1>
                        <h1>user level: {hostLvl}</h1>
                        <h1>user role: {hostRole}</h1>
                    </div>
                    <div className="main-matchup-user">
                        <h1>Opp: {oppUser}</h1>
                        <h1>OppTag: {oppTag}</h1>
                        <h1>Opp Level: {oppLvl}</h1>
                        <h1>Opp Role: {oppRole}</h1>
                    </div>
                </div>
            </article>
            
        </div>
    )
}

export default DisplayMatchups