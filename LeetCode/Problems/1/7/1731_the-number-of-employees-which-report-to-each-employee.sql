SELECT b.employee_id     AS employee_id,
       b.name            AS name,
       COUNT(*)          AS reports_count,
       ROUND(AVG(a.age)) AS average_age
FROM Employees a
         JOIN Employees b ON a.reports_to = b.employee_id
GROUP BY 1
ORDER BY 1;