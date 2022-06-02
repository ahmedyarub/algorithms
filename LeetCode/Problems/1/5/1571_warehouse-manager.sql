SELECT name AS warehouse_name, SUM(Width * Length * Height * units) volume
FROM Warehouse
         LEFT JOIN Products
                   USING (product_id)
GROUP BY name;