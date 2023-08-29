SELECT u.user_id, u.name, COALESCE(SUM(distance), 0) AS `traveled distance`
FROM Users as u
         LEFT JOIN Rides as r
                   ON u.user_id = r.user_id
GROUP BY user_id
ORDER BY user_id;