SELECT (CASE
            WHEN (SELECT COUNT(score) FROM NewYork WHERE score >= 90) >
                 (SELECT COUNT(score) FROM California WHERE score >= 90) THEN 'New York University'
            WHEN (SELECT COUNT(score) FROM NewYork WHERE score >= 90) <
                 (SELECT COUNT(score) FROM California WHERE score >= 90) THEN 'California University'
            ELSE 'No Winner' END) AS WINNER;