# IPL-PowerplayScorePredictor--IITM Hackathon
Submission for IITM Cricket Powerplay Prediction Competition
 
We used RandomForestRegression to predict the powerplay scores.
We created a database for venue, team and players , and made an index for each of them using the following formula;

Venue : 
Runs scored in venue / Total matches played in venue --for each innings


Team: 
For each innings:
Team batting index : Totals Runs by team/ Matches played by team
Team bowling index : Total balls bowled by team / Total wickets taken by team

Player Index: 
For each innings:
Batsmen index : Totals Runs by batsmen/ Matches played by batsmen/ 
Bowler index : Average (Economy of Bowler(match)/ Total wickets taken by bowler (match)
