CREATE PROCEDURE solution()
BEGIN
    SELECT count(*)
    FROM departments
    WHERE trim(description) IN ('NULL', 'nil', '-')
       OR description IS NULL;
END