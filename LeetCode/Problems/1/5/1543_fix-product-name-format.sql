SELECT LOWER(TRIM(product_name)) product_name, DATE_FORMAT(sale_date, "%Y-%m") sale_date, count(sale_id) total
FROM sales
GROUP BY 1, 2
ORDER BY 1, 2