SELECT LEFT(order_date, 7)         AS month,
       COUNT(DISTINCT order_id)    AS order_count,
       COUNT(DISTINCT customer_id) AS customer_count
FROM Orders
WHERE invoice > 20
GROUP BY 1;