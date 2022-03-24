CREATE PROCEDURE solution()
BEGIN
    SELECT DISTINCT t.subscriber
    FROM (SELECT subscriber, newspaper
          FROM full_year
          UNION ALL
          SELECT subscriber, newspaper
          FROM half_year) as t
    WHERE t.newspaper LIKE '%Daily%'
    ORDER BY t.subscriber;
END