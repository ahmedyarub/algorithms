# Write your MySQL query statement below
SELECT b.buyer_id
FROM Product AS a
         JOIN Sales AS b
              ON a.product_id = b.product_id
GROUP BY b.buyer_id
HAVING SUM(a.product_name = 'S8') > 0
   and SUM(a.product_name = 'iPhone') = 0;