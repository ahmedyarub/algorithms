CREATE PROCEDURE solution()
BEGIN
    SELECT id, name, surname
    FROM Suspect
    WHERE name like 'b%'
      and surname like 'Gre_n'
      and height <= 170;
END