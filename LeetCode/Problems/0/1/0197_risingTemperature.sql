# Write your MySQL query statement below
SELECT w1.id
FROM Weather AS w1
         LEFT JOIN Weather AS w2 ON w1.recordDate = DATE_ADD(w2.recordDate, interval 1 day)
WHERE w1.temperature > w2.temperature;