select "[0-5>" as bin, sum(case when duration / 60 between 0 and 5 then 1 else 0 end) Total
from sessions
union
select "[5-10>", sum(case when duration / 60 between 5 and 10 then 1 else 0 end)
from sessions
union
select "[10-15>", sum(case when duration / 60 between 10 and 15 then 1 else 0 end)
from sessions
union
select "15 or more", sum(case when duration / 60 > 15 then 1 else 0 end)
from sessions;