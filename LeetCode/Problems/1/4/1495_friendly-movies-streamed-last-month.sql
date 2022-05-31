SELECT DISTINCT title
FROM Content AS c
         LEFT JOIN TVProgram AS t
                   ON c.content_id = t.content_id
WHERE MONTH(program_date) = 6
  AND YEAR(program_date) = 2020
  AND Kids_content = 'Y'
  AND content_type = 'Movies';