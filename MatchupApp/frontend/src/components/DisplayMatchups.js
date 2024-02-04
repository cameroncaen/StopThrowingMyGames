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
    const [hostWardsPlaced, setHostWardsPlaced] = useState('');
    const [hostWardsKilled, setHostWardsKilled] = useState('');
    const [hostVWBought, setHostVWBought] = useState('');
    const [hostKP, setHostKP] = useState('');
    const [hostGPM, setHostGPM] = useState('');
    const [hostDPM, setHostDPM] = useState('');

    //User's lane opponent state fields
    const [oppUser, setOppUser] = useState('');
    const [oppTag, setOppTag] = useState('');
    const [oppLvl, setoppLvl] = useState('');
    const [oppRole, setOppRole] = useState('');
    const [oppKills, setOppKills] = useState('');
    const [oppDeaths, setOppDeaths] = useState('');
    const [oppAssists, setOppAssists] = useState('');
    const [oppWardsPlaced, setOppWardsPlaced] = useState('');
    const [oppWardsKilled, setOppWardsKilled] = useState('');
    const [oppVWBought, setOppVWBought] = useState('');
    const [oppKP, setOppKP] = useState('');
    const [oppGPM, setOppGPM] = useState('');
    const [oppDPM, setOppDPM] = useState('');

    // Ally1's state fields
    const [ally1User, setAlly1User] = useState('');
    const [ally1Tag, setAlly1Tag] = useState('');
    const [ally1Lvl, setAlly1Lvl] = useState('');
    const [ally1Role, setAlly1Role] = useState('');
    const [ally1Kills, setAlly1Kills] = useState('');
    const [ally1Deaths, setAlly1Deaths] = useState('');
    const [ally1Assists, setAlly1Assists] = useState('');
    const [ally1WardsPlaced, setAlly1WardsPlaced] = useState('');
    const [ally1WardsKilled, setAlly1WardsKilled] = useState('');
    const [ally1VWBought, setAlly1VWBought] = useState('');
    const [ally1KP, setAlly1KP] = useState('');
    const [ally1GPM, setAlly1GPM] = useState('');
    const [ally1DPM, setAlly1DPM] = useState('');

    // Enemy1 state fields
    const [enemy1User, setEnemy1User] = useState('');
    const [enemy1Tag, setEnemy1Tag] = useState('');
    const [enemy1Lvl, setEnemy1Lvl] = useState('');
    const [enemy1Role, setEnemy1Role] = useState('');
    const [enemy1Kills, setEnemy1Kills] = useState('');
    const [enemy1Deaths, setEnemy1Deaths] = useState('');
    const [enemy1Assists, setEnemy1Assists] = useState('');
    const [enemy1WardsPlaced, setEnemy1WardsPlaced] = useState('');
    const [enemy1WardsKilled, setEnemy1WardsKilled] = useState('');
    const [enemy1VWBought, setEnemy1VWBought] = useState('');
    const [enemy1KP, setEnemy1KP] = useState('');
    const [enemy1GPM, setEnemy1GPM] = useState('');
    const [enemy1DPM, setEnemy1DPM] = useState('');

    // Ally2 state fields
    const [ally2User, setAlly2User] = useState('');
    const [ally2Tag, setAlly2Tag] = useState('');
    const [ally2Lvl, setAlly2Lvl] = useState('');
    const [ally2Role, setAlly2Role] = useState('');
    const [ally2Kills, setAlly2Kills] = useState('');
    const [ally2Deaths, setAlly2Deaths] = useState('');
    const [ally2Assists, setAlly2Assists] = useState('');
    const [ally2WardsPlaced, setAlly2WardsPlaced] = useState('');
    const [ally2WardsKilled, setAlly2WardsKilled] = useState('');
    const [ally2VWBought, setAlly2VWBought] = useState('');
    const [ally2KP, setAlly2KP] = useState('');
    const [ally2GPM, setAlly2GPM] = useState('');
    const [ally2DPM, setAlly2DPM] = useState('');

    // Enemy2 state fields
    const [enemy2User, setEnemy2User] = useState('');
    const [enemy2Tag, setEnemy2Tag] = useState('');
    const [enemy2Lvl, setEnemy2Lvl] = useState('');
    const [enemy2Role, setEnemy2Role] = useState('');
    const [enemy2Kills, setEnemy2Kills] = useState('');
    const [enemy2Deaths, setEnemy2Deaths] = useState('');
    const [enemy2Assists, setEnemy2Assists] = useState('');
    const [enemy2WardsPlaced, setEnemy2WardsPlaced] = useState('');
    const [enemy2WardsKilled, setEnemy2WardsKilled] = useState('');
    const [enemy2VWBought, setEnemy2VWBought] = useState('');
    const [enemy2KP, setEnemy2KP] = useState('');
    const [enemy2GPM, setEnemy2GPM] = useState('');
    const [enemy2DPM, setEnemy2DPM] = useState('');
    
    // Ally3 state fields
    const [ally3User, setAlly3User] = useState('');
    const [ally3Tag, setAlly3Tag] = useState('');
    const [ally3Lvl, setAlly3Lvl] = useState('');
    const [ally3Role, setAlly3Role] = useState('');
    const [ally3Kills, setAlly3Kills] = useState('');
    const [ally3Deaths, setAlly3Deaths] = useState('');
    const [ally3Assists, setAlly3Assists] = useState('');
    const [ally3WardsPlaced, setAlly3WardsPlaced] = useState('');
    const [ally3WardsKilled, setAlly3WardsKilled] = useState('');
    const [ally3VWBought, setAlly3VWBought] = useState('');
    const [ally3KP, setAlly3KP] = useState('');
    const [ally3GPM, setAlly3GPM] = useState('');
    const [ally3DPM, setAlly3DPM] = useState('');

    // Enemy3 state fields
    const [enemy3User, setEnemy3User] = useState('');
    const [enemy3Tag, setEnemy3Tag] = useState('');
    const [enemy3Lvl, setEnemy3Lvl] = useState('');
    const [enemy3Role, setEnemy3Role] = useState('');
    const [enemy3Kills, setEnemy3Kills] = useState('');
    const [enemy3Deaths, setEnemy3Deaths] = useState('');
    const [enemy3Assists, setEnemy3Assists] = useState('');
    const [enemy3WardsPlaced, setEnemy3WardsPlaced] = useState('');
    const [enemy3WardsKilled, setEnemy3WardsKilled] = useState('');
    const [enemy3VWBought, setEnemy3VWBought] = useState('');
    const [enemy3KP, setEnemy3KP] = useState('');
    const [enemy3GPM, setEnemy3GPM] = useState('');
    const [enemy3DPM, setEnemy3DPM] = useState('');

    // Ally4 state fields
    const [ally4User, setAlly4User] = useState('');
    const [ally4Tag, setAlly4Tag] = useState('');
    const [ally4Lvl, setAlly4Lvl] = useState('');
    const [ally4Role, setAlly4Role] = useState('');
    const [ally4Kills, setAlly4Kills] = useState('');
    const [ally4Deaths, setAlly4Deaths] = useState('');
    const [ally4Assists, setAlly4Assists] = useState('');
    const [ally4WardsPlaced, setAlly4WardsPlaced] = useState('');
    const [ally4WardsKilled, setAlly4WardsKilled] = useState('');
    const [ally4VWBought, setAlly4VWBought] = useState('');
    const [ally4KP, setAlly4KP] = useState('');
    const [ally4GPM, setAlly4GPM] = useState('');
    const [ally4DPM, setAlly4DPM] = useState('');
    
    // Enemy4 state fields
    const [enemy4User, setEnemy4User] = useState('');
    const [enemy4Tag, setEnemy4Tag] = useState('');
    const [enemy4Lvl, setEnemy4Lvl] = useState('');
    const [enemy4Role, setEnemy4Role] = useState('');
    const [enemy4Kills, setEnemy4Kills] = useState('');
    const [enemy4Deaths, setEnemy4Deaths] = useState('');
    const [enemy4Assists, setEnemy4Assists] = useState('');
    const [enemy4WardsPlaced, setEnemy4WardsPlaced] = useState('');
    const [enemy4WardsKilled, setEnemy4WardsKilled] = useState('');
    const [enemy4VWBought, setEnemy4VWBought] = useState('');
    const [enemy4KP, setEnemy4KP] = useState('');
    const [enemy4GPM, setEnemy4GPM] = useState('');
    const [enemy4DPM, setEnemy4DPM] = useState('');


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
            setHostWardsPlaced(data.user_wardsPlaced)
            setHostWardsKilled(data.user_wardsKilled)
            setHostVWBought(data.user_VWBought)
            setHostKP(data.user_KP)
            setHostGPM(data.user_GPM)
            setHostDPM(data.user_DPM)

            setOppUser(data.opp_username)
            setOppTag(data.opp_tag)
            setoppLvl(data.opp_sumLevel)
            setOppRole(data.opp_role)
            setOppKills(data.opp_kills)
            setOppDeaths(data.opp_deaths)
            setOppAssists(data.opp_assists)
            setOppWardsPlaced(data.opp_wardsPlaced)
            setOppWardsKilled(data.opp_wardsKilled)
            setOppVWBought(data.opp_VWBought)
            setOppKP(data.opp_KP)
            setOppGPM(data.opp_GPM)
            setOppDPM(data.opp_DPM)

            setAlly1User(data.ally1_username)
            setAlly1Tag(data.ally1_tag)
            setAlly1Lvl(data.ally1_sumLevel)
            setAlly1Role(data.ally1_role)
            setAlly1Kills(data.ally1_kills)
            setAlly1Deaths(data.ally1_deaths)
            setAlly1Assists(data.ally1_assists)
            setAlly1WardsPlaced(data.ally1_wardsPlaced)
            setAlly1WardsKilled(data.ally1_wardsKilled)
            setAlly1VWBought(data.ally1_VWBought)
            setAlly1KP(data.ally1_KP)
            setAlly1GPM(data.ally1_GPM)
            setAlly1DPM(data.ally1_DPM)
            
            console.log(data.enemy1_username)
            setEnemy1User(data.enemy1_username)
            setEnemy1Tag(data.enemy1_tag)
            setEnemy1Lvl(data.enemy1_sumLevel)
            setEnemy1Role(data.enemy1_role)
            setEnemy1Kills(data.enemy1_kills)
            setEnemy1Deaths(data.enemy1_deaths)
            setEnemy1Assists(data.enemy1_assists)
            setEnemy1WardsPlaced(data.enemy1_wardsPlaced)
            setEnemy1WardsKilled(data.enemy1_wardsKilled)
            setEnemy1VWBought(data.enemy1_VWBought)
            setEnemy1KP(data.enemy1_KP)
            setEnemy1GPM(data.enemy1_GPM)
            setEnemy1DPM(data.enemy1_DPM)

            setAlly2User(data.ally2_username)
            setAlly2Tag(data.ally2_tag)
            setAlly2Lvl(data.ally2_sumLevel)
            setAlly2Role(data.ally2_role)
            setAlly2Kills(data.ally2_kills)
            setAlly2Deaths(data.ally2_deaths)
            setAlly2Assists(data.ally2_assists)
            setAlly2WardsPlaced(data.ally2_wardsPlaced)
            setAlly2WardsKilled(data.ally2_wardsKilled)
            setAlly2VWBought(data.ally2_VWBought)
            setAlly2KP(data.ally2_KP)
            setAlly2GPM(data.ally2_GPM)
            setAlly2DPM(data.ally2_DPM)

            setEnemy2User(data.enemy2_username)
            setEnemy2Tag(data.enemy2_tag)
            setEnemy2Lvl(data.enemy2_sumLevel)
            setEnemy2Role(data.enemy2_role)
            setEnemy2Kills(data.enemy2_kills)
            setEnemy2Deaths(data.enemy2_deaths)
            setEnemy2Assists(data.enemy2_assists)
            setEnemy2WardsPlaced(data.enemy2_wardsPlaced)
            setEnemy2WardsKilled(data.enemy2_wardsKilled)
            setEnemy2VWBought(data.enemy2_VWBought)
            setEnemy2KP(data.enemy2_KP)
            setEnemy2GPM(data.enemy2_GPM)
            setEnemy2DPM(data.enemy2_DPM)

            setAlly3User(data.ally3_username)
            setAlly3Tag(data.ally3_tag)
            setAlly3Lvl(data.ally3_sumLevel)
            setAlly3Role(data.ally3_role)
            setAlly3Kills(data.ally3_kills)
            setAlly3Deaths(data.ally3_deaths)
            setAlly3Assists(data.ally3_assists)
            setAlly3WardsPlaced(data.ally3_wardsPlaced)
            setAlly3WardsKilled(data.ally3_wardsKilled)
            setAlly3VWBought(data.ally3_VWBought)
            setAlly3KP(data.ally3_KP)
            setAlly3GPM(data.ally3_GPM)
            setAlly3DPM(data.ally3_DPM)

            setEnemy3User(data.enemy3_username)
            setEnemy3Tag(data.enemy3_tag)
            setEnemy3Lvl(data.enemy3_sumLevel)
            setEnemy3Role(data.enemy3_role)
            setEnemy3Kills(data.enemy3_kills)
            setEnemy3Deaths(data.enemy3_deaths)
            setEnemy3Assists(data.enemy3_assists)
            setEnemy3WardsPlaced(data.enemy3_wardsPlaced)
            setEnemy3WardsKilled(data.enemy3_wardsKilled)
            setEnemy3VWBought(data.enemy3_VWBought)
            setEnemy3KP(data.enemy3_KP)
            setEnemy3GPM(data.enemy3_GPM)
            setEnemy3DPM(data.enemy3_DPM)

            setAlly4User(data.ally4_username)
            setAlly4Tag(data.ally4_tag)
            setAlly4Lvl(data.ally4_sumLevel)
            setAlly4Role(data.ally4_role)
            setAlly4Kills(data.ally4_kills)
            setAlly4Deaths(data.ally4_deaths)
            setAlly4Assists(data.ally4_assists)
            setAlly4WardsPlaced(data.ally4_wardsPlaced)
            setAlly4WardsKilled(data.ally4_wardsKilled)
            setAlly4VWBought(data.ally4_VWBought)
            setAlly4KP(data.ally4_KP)
            setAlly4GPM(data.ally4_GPM)
            setAlly4DPM(data.ally4_DPM)

            setEnemy4User(data.enemy4_username)
            setEnemy4Tag(data.enemy4_tag)
            setEnemy4Lvl(data.enemy4_sumLevel)
            setEnemy4Role(data.enemy4_role)
            setEnemy4Kills(data.enemy4_kills)
            setEnemy4Deaths(data.enemy4_deaths)
            setEnemy4Assists(data.enemy4_assists)
            setEnemy4WardsPlaced(data.enemy4_wardsPlaced)
            setEnemy4WardsKilled(data.enemy4_wardsKilled)
            setEnemy4VWBought(data.enemy4_VWBought)
            setEnemy4KP(data.enemy4_KP)
            setEnemy4GPM(data.enemy4_GPM)
            setEnemy4DPM(data.enemy4_DPM)
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
                        <h1>Wards Places/Wards Killed: {hostWardsPlaced}/{hostWardsKilled}</h1>
                        <h1>Control Wards Bought: {hostVWBought}</h1>
                        <h1>Kill Participation: {hostKP}</h1>
                        <h1>Gold Per Minute: {hostGPM}</h1>
                        <h1>Damage Per Minute: {hostDPM}</h1>
                    </div>
                    <div className="main-matchup-center">
                        <h1>{hostRole}</h1>
                    </div>
                    <div className="main-matchup-opp">
                        <h1>User: {oppUser}#{oppTag}</h1>
                        <h1>Lvl: {oppLvl}</h1>
                        <h1>KDA: {oppKills}/{oppDeaths}/{oppAssists}</h1>
                        <h1>{oppWardsPlaced}/{oppWardsKilled} :Wards Places/Wards Killed</h1>
                        <h1>{oppVWBought} :Control Wards Bought</h1>
                        <h1>{oppKP} :Kill Participation</h1>
                        <h1>{oppGPM} :Gold Per Minute</h1>
                        <h1>{oppDPM} :Damage Per Minute</h1>
                    </div>
                </div>

                <div className="sub-matchup-row">
                    <div className="sub-matchup-wrapper">
                        <div className="sub-matchup-user">
                            <h1>User: {ally1User}#{ally1Tag}</h1>
                            <h1>Lvl: {ally1Lvl}</h1>
                            <h1>KDA: {ally1Kills}/{ally1Deaths}/{ally1Assists}</h1>
                            <h1>Wards Places/Wards Killed: {ally1WardsPlaced}/{ally1WardsKilled}</h1>
                            <h1>Control Wards Bought: {ally1VWBought}</h1>
                            <h1>Kill Participation: {ally1KP}</h1>
                            <h1>Gold Per Minute: {ally1GPM}</h1>
                            <h1>Damage Per Minute: {ally1DPM}</h1>
                        </div>
                        <div className="sub-matchup-center">
                            <h1>{ally1Role}</h1>
                        </div>
                        <div className="sub-matchup-opp">
                            <h1>User: {enemy1User}#{enemy1Tag}</h1>
                            <h1>Lvl: {enemy1Lvl}</h1>
                            <h1>KDA: {enemy1Kills}/{enemy1Deaths}/{enemy1Assists}</h1>
                            <h1>{enemy1WardsPlaced}/{enemy1WardsKilled} :Wards Places/Wards Killed</h1>
                            <h1>{enemy1VWBought} :Control Wards Bought</h1>
                            <h1>{enemy1KP} :Kill Participation</h1>
                            <h1>{enemy1GPM} :Gold Per Minute</h1>
                            <h1>{enemy1DPM} :Damage Per Minute</h1>
                        </div>
                    </div>

                    <div className="sub-matchup-wrapper">
                        <div className="sub-matchup-user">
                            <h1>User: {ally2User}#{ally2Tag}</h1>
                            <h1>Lvl: {ally2Lvl}</h1>
                            <h1>KDA: {ally2Kills}/{ally2Deaths}/{ally2Assists}</h1>
                            <h1>Wards Places/Wards Killed: {ally2WardsPlaced}/{ally2WardsKilled}</h1>
                            <h1>Control Wards Bought: {ally2VWBought}</h1>
                            <h1>Kill Participation: {ally2KP}</h1>
                            <h1>Gold Per Minute: {ally2GPM}</h1>
                            <h1>Damage Per Minute: {ally2DPM}</h1>
                        </div>
                        <div className="sub-matchup-center">
                            <h1>{ally2Role}</h1>
                        </div>
                        <div className="sub-matchup-opp">
                            <h1>User: {enemy2User}#{enemy2Tag}</h1>
                            <h1>Lvl: {enemy2Lvl}</h1>
                            <h1>KDA: {enemy2Kills}/{enemy2Deaths}/{enemy2Assists}</h1>
                            <h1>{enemy2WardsPlaced}/{enemy2WardsKilled} :Wards Places/Wards Killed</h1>
                            <h1>{enemy2VWBought} :Control Wards Bought</h1>
                            <h1>{enemy2KP} :Kill Participation</h1>
                            <h1>{enemy2GPM} :Gold Per Minute</h1>
                            <h1>{enemy2DPM} :Damage Per Minute</h1>
                        </div>
                    </div>
                </div>

                <div className="sub-matchup-row">
                    <div className="sub-matchup-wrapper">
                        <div className="sub-matchup-user">
                            <h1>User: {ally3User}#{ally3Tag}</h1>
                            <h1>Lvl: {ally3Lvl}</h1>
                            <h1>KDA: {ally3Kills}/{ally3Deaths}/{ally3Assists}</h1>
                            <h1>Wards Places/Wards Killed: {ally3WardsPlaced}/{ally3WardsKilled}</h1>
                            <h1>Control Wards Bought: {ally3VWBought}</h1>
                            <h1>Kill Participation: {ally3KP}</h1>
                            <h1>Gold Per Minute: {ally3GPM}</h1>
                            <h1>Damage Per Minute: {ally3DPM}</h1>
                        </div>
                        <div className="sub-matchup-center">
                            <h1>{ally3Role}</h1>
                        </div>
                        <div className="sub-matchup-opp">
                            <h1>User: {enemy3User}#{enemy3Tag}</h1>
                            <h1>Lvl: {enemy3Lvl}</h1>
                            <h1>KDA: {enemy3Kills}/{enemy3Deaths}/{enemy3Assists}</h1>
                            <h1>{enemy3WardsPlaced}/{enemy3WardsKilled} :Wards Places/Wards Killed</h1>
                            <h1>{enemy3VWBought} :Control Wards Bought</h1>
                            <h1>{enemy3KP} :Kill Participation</h1>
                            <h1>{enemy3GPM} :Gold Per Minute</h1>
                            <h1>{enemy3DPM} :Damage Per Minute</h1>
                        </div>
                    </div>
                    
                    <div className="sub-matchup-wrapper">
                        <div className="sub-matchup-user">
                            <h1>User: {ally4User}#{ally4Tag}</h1>
                            <h1>Lvl: {ally4Lvl}</h1>
                            <h1>KDA: {ally4Kills}/{ally4Deaths}/{ally4Assists}</h1>
                            <h1>Wards Places/Wards Killed: {ally4WardsPlaced}/{ally4WardsKilled}</h1>
                            <h1>Control Wards Bought: {ally4VWBought}</h1>
                            <h1>Kill Participation: {ally4KP}</h1>
                            <h1>Gold Per Minute: {ally4GPM}</h1>
                            <h1>Damage Per Minute: {ally4DPM}</h1>
                        </div>
                        <div className="sub-matchup-center">
                            <h1>{ally4Role}</h1>
                        </div>
                        <div className="sub-matchup-opp">
                            <h1>User: {enemy4User}#{enemy4Tag}</h1>
                            <h1>Lvl: {enemy4Lvl}</h1>
                            <h1>KDA: {enemy4Kills}/{enemy4Deaths}/{enemy4Assists}</h1>
                            <h1>{enemy4WardsPlaced}/{enemy4WardsKilled} :Wards Places/Wards Killed</h1>
                            <h1>{enemy4VWBought} :Control Wards Bought</h1>
                            <h1>{enemy4KP} :Kill Participation</h1>
                            <h1>{enemy4GPM} :Gold Per Minute</h1>
                            <h1>{enemy4DPM} :Damage Per Minute</h1>
                        </div>
                    </div>
                </div>
            </article>            
        </div>
    )
}

export default DisplayMatchups