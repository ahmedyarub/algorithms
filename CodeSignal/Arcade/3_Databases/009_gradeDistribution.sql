CREATE PROCEDURE solution()
BEGIN
	SELECT Name, ID
    FROM Grades
    WHERE Final > (Midterm1 * 0.25 + Midterm2 * 0.25 + Final * 0.5) AND Final > (Midterm1 * 0.5 + Midterm2 * 0.5)
    ORDER BY LEFT(Name, 3), ID;
END