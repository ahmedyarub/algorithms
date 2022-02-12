CREATE PROCEDURE solution()
BEGIN
	SELECT id, scholarship / 12 as scholarship
    FROM scholarships;
END