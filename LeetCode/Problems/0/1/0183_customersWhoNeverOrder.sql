# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers
         LEFT JOIN Orders on Customers.id = Orders.customerId
Where Orders.id IS NULL;
