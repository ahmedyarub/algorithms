CREATE PROCEDURE solution()
BEGIN
	SELECT *
    FROM results
    ORDER BY wins;
END