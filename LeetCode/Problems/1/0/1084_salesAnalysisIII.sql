SELECT Product.product_id, product_name
FROM Product
         LEFT JOIN Sales ON Product.product_id = Sales.product_id
GROUP BY product_id
HAVING SUM(sale_date >= '2019-01-01' AND sale_date <= '2019-03-31') > 0
   AND SUM(sale_date < '2019-01-01' OR sale_date > '2019-03-31') = 0;