SELECT customer_id, name
FROM Customers
         JOIN Orders USING (customer_id)
         JOIN Product USING (product_id)
GROUP BY customer_id
HAVING SUM(IF(MONTH(order_date) = 6, quantity, 0) * price) >= 100
   AND SUM(IF(MONTH(order_date) = 7, quantity, 0) * price) >= 100