DELETE
FROM Person
WHERE id NOT IN (SELECT mid FROM (SELECT MIN(id) as mid FROM Person GROUP BY email) AS p2);