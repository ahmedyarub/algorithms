CREATE PROCEDURE solution()
BEGIN
	SELECT DISTINCT name
    FROM projectLog
    ORDER BY name;
END