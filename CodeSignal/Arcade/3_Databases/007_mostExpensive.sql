CREATE PROCEDURE solution()
BEGIN
	SELECT name
    FROM Products
    ORDER BY price * quantity DESC, name
    LIMIT 1;
END