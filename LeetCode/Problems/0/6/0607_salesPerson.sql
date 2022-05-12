SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (SELECT DISTINCT o.sales_id
                       FROM Orders as o
                                LEFT JOIN Company as c
                                          ON o.com_id = c.com_id
                       WHERE c.name = 'RED');