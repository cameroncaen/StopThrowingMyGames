import React, {useState} from "react";
import { useNavigate, useParams } from 'react-router-dom';

export const DisplayMatchups = () => {
    const matchCode = useParams();

    // User state fields
    const [hostUser, setHostUser] = useState('');
    const [hostTag, setHostTag] = useState('');
    const [hostLvl, setHostLvl] = useState('');
    const [hostRole, setHostRole] = useState('');
    const [hostKills, setHostKills] = useState('');
    const [hostDeaths, setHostDeaths] = useState('');
    const [hostAssists, setHostAssists] = useState('');

    //User's lane opponent state fields
    const [oppUser, setOppUser] = useState('');
    const [oppTag, setOppTag] = useState('');
    const [oppLvl, setoppLvl] = useState('');
    const [oppRole, setOppRole] = useState('');
    const [oppKills, setOppKills] = useState('');
    const [oppDeaths, setOppDeaths] = useState('');
    const [oppAssists, setOppAssists] = useState('');

    // Ally1's state fields
    const [ally1User, setAlly1User] = useState('');
    const [ally1Tag, setAlly1Tag] = useState('');
    const [ally1Lvl, setAlly1Lvl] = useState('');
    const [ally1Role, setAlly1Role] = useState('');
    const [ally1Kills, setAlly1Kills] = useState('');
    const [ally1Deaths, setAlly1Deaths] = useState('');
    const [ally1Assists, setAlly1Assists] = useState('');

    // Enemy1 state fields
    const [enemy1User, setEnemy1User] = useState('');
    const [enemy1Tag, setEnemy1Tag] = useState('');
    const [enemy1Lvl, setEnemy1Lvl] = useState('');
    const [enemy1Role, setEnemy1Role] = useState('');
    const [enemy1Kills, setEnemy1Kills] = useState('');
    const [enemy1Deaths, setEnemy1Deaths] = useState('');
    const [enemy1Assists, setEnemy1Assists] = useState('');

    // Ally2 state fields
    const [ally2User, setAlly2User] = useState('');
    const [ally2Tag, setAlly2Tag] = useState('');
    const [ally2Lvl, setAlly2Lvl] = useState('');
    const [ally2Role, setAlly2Role] = useState('');
    const [ally2Kills, setAlly2Kills] = useState('');
    const [ally2Deaths, setAlly2Deaths] = useState('');
    const [ally2Assists, setAlly2Assists] = useState('');

    // Enemy2 state fields
    const [enemy2User, setEnemy2User] = useState('');
    const [enemy2Tag, setEnemy2Tag] = useState('');
    const [enemy2Lvl, setEnemy2Lvl] = useState('');
    const [enemy2Role, setEnemy2Role] = useState('');
    const [enemy2Kills, setEnemy2Kills] = useState('');
    const [enemy2Deaths, setEnemy2Deaths] = useState('');
    const [enemy2Assists, setEnemy2Assists] = useState('');
    
    // Ally3 state fields
    const [ally3User, setAlly3User] = useState('');
    const [ally3Tag, setAlly3Tag] = useState('');
    const [ally3Lvl, setAlly3Lvl] = useState('');
    const [ally3Role, setAlly3Role] = useState('');
    const [ally3Kills, setAlly3Kills] = useState('');
    const [ally3Deaths, setAlly3Deaths] = useState('');
    const [ally3Assists, setAlly3Assists] = useState('');

    // Enemy3 state fields
    const [enemy3User, setEnemy3User] = useState('');
    const [enemy3Tag, setEnemy3Tag] = useState('');
    const [enemy3Lvl, setEnemy3Lvl] = useState('');
    const [enemy3Role, setEnemy3Role] = useState('');
    const [enemy3Kills, setEnemy3Kills] = useState('');
    const [enemy3Deaths, setEnemy3Deaths] = useState('');
    const [enemy3Assists, setEnemy3Assists] = useState('');

    // Ally4 state fields
    const [ally4User, setAlly4User] = useState('');
    const [ally4Tag, setAlly4Tag] = useState('');
    const [ally4Lvl, setAlly4Lvl] = useState('');
    const [ally4Role, setAlly4Role] = useState('');
    const [ally4Kills, setAlly4Kills] = useState('');
    const [ally4Deaths, setAlly4Deaths] = useState('');
    const [ally4Assists, setAlly4Assists] = useState('');
    
    // Enemy4 state fields
    const [enemy4User, setEnemy4User] = useState('');
    const [enemy4Tag, setEnemy4Tag] = useState('');
    const [enemy4Lvl, setEnemy4Lvl] = useState('');
    const [enemy4Role, setEnemy4Role] = useState('');
    const [enemy4Kills, setEnemy4Kills] = useState('');
    const [enemy4Deaths, setEnemy4Deaths] = useState('');
    const [enemy4Assists, setEnemy4Assists] = useState('');


    //console.log(matchCode.sessionCode);
    const getMatchInfo = () => {
        fetch("/api/get-stats" + "?code=" + matchCode.sessionCode)
        .then((response) => response.json())
        .then((data) => {
            setHostUser(data.username)
            setHostTag(data.tag)
            setHostLvl(data.user_sumLevel)
            setHostRole(data.user_role)
            setHostKills(data.user_kills)
            setHostDeaths(data.user_deaths)
            setHostAssists(data.user_assists)

            setOppUser(data.opp_username)
            setOppTag(data.opp_tag)
            setoppLvl(data.opp_sumLevel)
            setOppRole(data.opp_role)
            setOppKills(data.opp_kills)
            setOppDeaths(data.opp_deaths)
            setOppAssists(data.opp_assists)

            setAlly1User(data.ally1_username)
            setAlly1Tag(data.ally1_tag)
            setAlly1Lvl(data.ally1_sumLevel)
            setAlly1Role(data.ally1_role)
            setAlly1Kills(data.ally1_kills)
            setAlly1Deaths(data.ally1_deaths)
            setAlly1Assists(data.ally1_assists)

            setEnemy1User(data.enemy1_username)
            setEnemy1Tag(data.enemy1_tag)
            setEnemy1Lvl(data.enemy1_sumLevel)
            setEnemy1Role(data.enemy1_role)
            setEnemy1Kills(data.enemy1_kills)
            setEnemy1Deaths(data.enemy1_deaths)
            setEnemy1Assists(data.enemy1_assists)

            setAlly2User(data.ally2_username)
            setAlly2Tag(data.ally2_tag)
            setAlly2Lvl(data.ally2_sumLevel)
            setAlly2Role(data.ally2_role)
            setAlly2Kills(data.ally2_kills)
            setAlly2Deaths(data.ally2_deaths)
            setAlly2Assists(data.ally2_assists)

            setEnemy2User(data.enemy2_username)
            setEnemy2Tag(data.enemy2_tag)
            setEnemy2Lvl(data.enemy2_sumLevel)
            setEnemy2Role(data.enemy2_role)
            setEnemy2Kills(data.enemy2_kills)
            setEnemy2Deaths(data.enemy2_deaths)
            setEnemy2Assists(data.enemy2_assists)

            setAlly3User(data.ally3_username)
            setAlly3Tag(data.ally3_tag)
            setAlly3Lvl(data.ally3_sumLevel)
            setAlly3Role(data.ally3_role)
            setAlly3Kills(data.ally3_kills)
            setAlly3Deaths(data.ally3_deaths)
            setAlly3Assists(data.ally3_assists)

            setEnemy3User(data.enemy3_username)
            setEnemy3Tag(data.enemy3_tag)
            setEnemy3Lvl(data.enemy3_sumLevel)
            setEnemy3Role(data.enemy3_role)
            setEnemy3Kills(data.enemy3_kills)
            setEnemy3Deaths(data.enemy3_deaths)
            setEnemy3Assists(data.enemy3_assists)

            setAlly4User(data.ally4_username)
            setAlly4Tag(data.ally4_tag)
            setAlly4Lvl(data.ally4_sumLevel)
            setAlly4Role(data.ally4_role)
            setAlly4Kills(data.ally4_kills)
            setAlly4Deaths(data.ally4_deaths)
            setAlly4Assists(data.ally4_assists)

            setEnemy4User(data.enemy4_username)
            setEnemy4Tag(data.enemy4_tag)
            setEnemy4Lvl(data.enemy4_sumLevel)
            setEnemy4Role(data.enemy4_role)
            setEnemy4Kills(data.enemy4_kills)
            setEnemy4Deaths(data.enemy4_deaths)
            setEnemy4Assists(data.enemy4_assists)
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
                <div className="main-matchup-wrapper">
                    <div className="main-matchup-user">
                        <h1>User: {hostUser}#{hostTag}</h1>
                        <h1>Lvl: {hostLvl}</h1>
                        <h1>KDA: {hostKills}/{hostDeaths}/{hostAssists}</h1>
                    </div>
                    <div className="main-matchup-center">
                        <h1>{hostRole}</h1>
                    </div>
                    <div className="main-matchup-opp">
                        <h1>User: {oppUser}#{oppTag}</h1>
                        <h1>Lvl: {oppLvl}</h1>
                        <h1>KDA: {oppKills}/{oppDeaths}/{oppAssists}</h1>
                    </div>
                </div>
            </article>
            <article className="matchup-body">
                <div className="main-matchup-wrapper">
                    <div className="main-matchup-user">
                        <h1>User: {ally1User}#{ally1Tag}</h1>
                        <h1>Lvl: {ally1Lvl}</h1>
                        <h1>KDA: {ally1Kills}/{ally1Deaths}/{ally1Assists}</h1>
                    </div>
                    <div className="main-matchup-center">
                        <h1>{ally1Role}</h1>
                    </div>
                    <div className="main-matchup-opp">
                        <h1>User: {enemy1User}#{enemy1Tag}</h1>
                        <h1>Lvl: {enemy1Lvl}</h1>
                        <h1>KDA: {enemy1Kills}/{enemy1Deaths}/{enemy1Assists}</h1>
                    </div>
                </div>
            </article>
            <article className="matchup-body">
                <div className="main-matchup-wrapper">
                    <div className="main-matchup-user">
                        <h1>User: {ally2User}#{ally2Tag}</h1>
                        <h1>Lvl: {ally2Lvl}</h1>
                        <h1>KDA: {ally2Kills}/{ally2Deaths}/{ally2Assists}</h1>
                    </div>
                    <div className="main-matchup-center">
                        <h1>{ally2Role}</h1>
                    </div>
                    <div className="main-matchup-opp">
                        <h1>User: {enemy2User}#{enemy2Tag}</h1>
                        <h1>Lvl: {enemy2Lvl}</h1>
                        <h1>KDA: {enemy2Kills}/{enemy2Deaths}/{enemy2Assists}</h1>
                    </div>
                </div>
            </article><article className="matchup-body">
                <div className="main-matchup-wrapper">
                    <div className="main-matchup-user">
                        <h1>User: {ally3User}#{ally3Tag}</h1>
                        <h1>Lvl: {ally3Lvl}</h1>
                        <h1>KDA: {ally3Kills}/{ally3Deaths}/{ally3Assists}</h1>
                    </div>
                    <div className="main-matchup-center">
                        <h1>{ally3Role}</h1>
                    </div>
                    <div className="main-matchup-opp">
                        <h1>User: {enemy3User}#{enemy3Tag}</h1>
                        <h1>Lvl: {enemy3Lvl}</h1>
                        <h1>KDA: {enemy3Kills}/{enemy3Deaths}/{enemy3Assists}</h1>
                    </div>
                </div>
            </article><article className="matchup-body">
                <div className="main-matchup-wrapper">
                    <div className="main-matchup-user">
                        <h1>User: {ally4User}#{ally4Tag}</h1>
                        <h1>Lvl: {ally4Lvl}</h1>
                        <h1>KDA: {ally4Kills}/{ally4Deaths}/{ally4Assists}</h1>
                    </div>
                    <div className="main-matchup-center">
                        <h1>{ally4Role}</h1>
                    </div>
                    <div className="main-matchup-opp">
                        <h1>User: {enemy4User}#{enemy4Tag}</h1>
                        <h1>Lvl: {enemy4Lvl}</h1>
                        <h1>KDA: {enemy4Kills}/{enemy4Deaths}/{enemy4Assists}</h1>
                    </div>
                </div>
            </article>
            
        </div>
    )
}

export default DisplayMatchups