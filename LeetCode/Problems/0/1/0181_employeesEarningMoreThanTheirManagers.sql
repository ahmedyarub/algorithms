SELECT e.name as Employee
FROM Employee as e
         INNER JOIN Employee as m ON e.managerId = m.id
WHERE e.salary > m.salary;