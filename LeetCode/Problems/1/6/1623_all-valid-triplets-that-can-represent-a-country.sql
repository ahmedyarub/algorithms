SELECT a.student_name AS member_A,
       b.student_name AS member_B,
       c.student_name AS member_c
FROM schoolA a
         JOIN schoolB b
              ON a.student_name != b.student_name AND a.student_id != b.student_id
         JOIN schoolC c
              ON b.student_name != c.student_name AND a.student_name != c.student_name
                  AND b.student_id != c.student_id AND a.student_id != c.student_id