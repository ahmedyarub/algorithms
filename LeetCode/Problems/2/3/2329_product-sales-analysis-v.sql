SELECT s.user_id,
       SUM(quantity * price) as spending
FROM Sales s
         INNER JOIN Product p USING (product_id)
GROUP BY s.user_id
ORDER BY 2 desc