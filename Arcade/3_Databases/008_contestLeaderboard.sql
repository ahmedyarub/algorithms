CREATE PROCEDURE solution()
BEGIN
	SELECT name
    FROM leaderboard
    ORDER BY score DESC
    LIMIT 3,5;
END