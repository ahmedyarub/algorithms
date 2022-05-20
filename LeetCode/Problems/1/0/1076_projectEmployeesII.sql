SELECT project_id
FROM Project
GROUP BY project_id
HAVING count(*) = (SELECT count(*)
                             FROM Project
                             GROUP BY project_id
                             ORDER BY count(*) DESC
                             LIMIT 1);