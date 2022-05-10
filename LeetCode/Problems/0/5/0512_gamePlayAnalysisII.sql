# Write your MySQL query statement below
SELECT player_id, device_id
FROM Activity as ac1
WHERE event_date = (SELECT MIN(event_date) FROM Activity as ac2 WHERE ac1.player_id = ac2.player_id);