CREATE PROCEDURE solution()
BEGIN
	SELECT weekday(mischief_date) as weekday, mischief_date, author, title
    FROM mischief
    ORDER BY weekday(mischief_date),field(author,"Huey","Dewey","Louie"),mischief_date, title;
END