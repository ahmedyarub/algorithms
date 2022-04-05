SELECT us.product_id, round(sum(units * price) / sum(units), 2) as average_price
FROM UnitsSold as us
         LEFT JOIN Prices as p ON us.product_id = p.product_id
WHERE (purchase_date BETWEEN start_date AND end_date)
GROUP BY us.product_id;