SELECT contest_id, ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(*) FROM Users) * 100, 2) percentage
FROM Register
GROUP BY contest_id
ORDER BY 2 DESC, 1;