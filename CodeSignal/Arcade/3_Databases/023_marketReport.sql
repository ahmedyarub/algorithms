CREATE PROCEDURE solution()
BEGIN
    select country, competitors
    FROM (SELECT country, count(*) as competitors, 1 as r
          FROM foreignCompetitors
          GROUP BY country
          UNION
          SELECT 'Total:', count(*) as competitors, 2 as r
          FROM foreignCompetitors) as t
    ORDER BY r, country;
END