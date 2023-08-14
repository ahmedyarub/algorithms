select distinct emp_id,
                firstname,
                lastname,
                max(salary) over (partition by emp_id) salary,
                department_id
from Salary