SELECT m.symbol metal, n.symbol nonmetal
FROM Elements m INNER JOIN Elements n
ON m.type='Metal' AND n.type='Nonmetal';