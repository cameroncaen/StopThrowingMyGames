# StopThrowingMyGames
LOL matchup checker for viewing stats about the current game and interpreting the data in order to improve player gameplay.

Usage: 
In order to install and run this inutitive matchup analyzer there are a few simple steps you need to follow

1.) Follow the React.js and Django/Python installation guides on their respective websites and install the latest versions

2.) Pull this repository into your local system storage 

3.) Install the role identification files using the folowing pip install command (NEED TO HAVE GIT INSTALLED)
pip install git+https://github.com/meraki-analytics/role-identification.git
Should there be any issues in the installation please refer to the creator meraki-analytics 's github page for assistance on installing packages from git.
(here is a link to the original creator of the role identification algorithm's github repo)
https://github.com/meraki-analytics/role-identification/tree/master
(These files and functions were not written by our team and are fully accredited to the github user linked above as their intellectual property)

4.) Login to your Riot Games account on the Riot Developer Portal (create an account if necessary): 
(link) https://developer.riotgames.com/

5.) On the Developer Portal homepage, click your username in the top right and then select Dashboard. On this page there will be a DEVELOPMENT API KEY section with a button to renerate a personal API key. Press this button, fill out the Captcha, and copy your key. 
IMPORTANT NOTICE: Your key will expire after 24 hours so make sure to refresh it before using after long breaks just in case. A confusing JSON doctype error will appear on the lookup page if this is the case

6.) Go into MatchupApp -> api -> user_info.py and open this file. Then, insert your API key in the riotKey variable inbetween the quotation marks

--------- AT THIS POINT ALL SETUP IS COMPLETED, THE ONLY MATINANCE REQUIRED IS A DAILY LIMIT OF THE API KEY DURATION ------

7.) To actually run the code on your local system, open two terminal windows both in the projects root directory. One terminal will be handling the frontend while the other will host the backend server. 

terminal 1: cd into MatchupApp/ and run the following command.

python ./manage.py runserver <desired server number here (if left blank will default to 8000)> 

after running, open up the link next to "Starting development server at " in your browser

terminal 2: cd into MatchupApp/frontend and run the following command.

npm run dev

(this will allow for changes to the frontend webpage to be constantly updated should you make changes to the frontend code)

8.) Finally, on the website that link from terminal 1 brough you to click the search button to be directed to the lookup page where you can lookup the desired summoner via their riot username and riot tag. After entering the player info into the indicated fields, in about 30 seconds the page will refresh and take you to the matchup page where the statistics and insigts for all players and roles this match will be displayed giving you all the data you need to get the edge on your oppenent

Note: the player looked up must have a valid riot username and tagline and be in an ongoing game or respective error messages will appear.