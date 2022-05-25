SELECT DISTINCT s1.sub_id                        as post_id,
                (SELECT COUNT(DISTINCT s2.sub_id)
                 FROM Submissions as s2
                 WHERE s2.parent_id = s1.sub_id) as number_of_comments
FROM Submissions as s1
WHERE parent_id IS NULL
ORDER BY s1.sub_id;