CREATE PROCEDURE solution()
BEGIN
    SELECT id, name, surname
    FROM Suspect
    WHERE NOT (height > 170
        AND name LIKE 'B%'
        AND surname LIKE 'Gre_n');
END