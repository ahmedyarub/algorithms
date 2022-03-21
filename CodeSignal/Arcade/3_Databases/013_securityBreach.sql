CREATE PROCEDURE solution()
BEGIN
    SELECT first_name, second_name, attribute
    FROM users
    WHERE attribute LIKE BINARY concat('_%\%', first_name, '\_', second_name, '\%%');
END