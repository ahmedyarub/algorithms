SELECT query_name,
       ROUND(SUM(rating / position) / count(*), 2)          as quality,
       ROUND(SUM(if(rating < 3, 1, 0)) / count(*) * 100, 2) as poor_query_percentage
FROM Queries
GROUP BY query_name;