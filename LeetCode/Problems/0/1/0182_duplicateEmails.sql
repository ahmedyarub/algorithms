SELECT email
FROM Person
GROUP BY email
HAVING count(id) > 1;