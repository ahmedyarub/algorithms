SELECT e1.employee_id, (SELECT COUNT(*) FROM Employee as e2 WHERE e2.team_id = e1.team_id) AS team_size
FROM Employee AS e1;