CREATE PROCEDURE solution()
    SELECT id, IF (given_answer IS NULL, 'no answer',IF(correct_answer = given_answer, 'correct', 'incorrect')) AS checks
    FROM answers
    ORDER BY id;
