SELECT unique_id, name
FROM Employees AS e
         LEFT JOIN EmployeeUNI as eu
                   ON e.id = eu.id;