SELECT employee_id,
       CASE
           WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
           ELSE 0
           END
           AS bonus
FROM Employees
ORDER BY employee_id;