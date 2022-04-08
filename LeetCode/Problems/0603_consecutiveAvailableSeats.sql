SELECT c1.seat_id
FROM Cinema AS c1
WHERE c1.free = 1
  AND ((SELECT free FROM Cinema AS c2 WHERE c1.seat_id - 1 = c2.seat_id) = 1 OR
       (SELECT free FROM Cinema AS c2 WHERE c1.seat_id + 1 = c2.seat_id) = 1);