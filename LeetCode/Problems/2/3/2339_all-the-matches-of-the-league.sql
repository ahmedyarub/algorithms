select t1.team_name as home_team, t2.team_name as away_team
from teams t1
         cross join teams t2
where t1.team_name != t2.team_name