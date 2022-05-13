SELECT id, movie, description, rating
FROM Cinema
WHERE id MOD 2 = 1
  AND description != "boring"
ORDER BY rating DESC;