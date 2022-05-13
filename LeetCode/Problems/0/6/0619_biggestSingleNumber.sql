SELECT MAX(n) as num
FROM (SELECT num as n
      FROM MyNumbers
      GROUP BY num
      HAVING count(*) = 1) as t;