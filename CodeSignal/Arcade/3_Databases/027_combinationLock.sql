CREATE PROCEDURE solution()
BEGIN
    SELECT ROUND(EXP(SUM(LOG(LENGTH(characters))))) AS combinations
    FROM discs;
END