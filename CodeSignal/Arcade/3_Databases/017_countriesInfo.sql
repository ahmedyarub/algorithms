CREATE PROCEDURE solution()
BEGIN
    SELECT count(*) as number, avg(population) as average, sum(population) as total
    FROM countries;
END