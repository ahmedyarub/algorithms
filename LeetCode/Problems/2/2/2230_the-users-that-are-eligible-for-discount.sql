select distinct user_id
from purchases
where time_stamp >= startDate
  and time_stamp <= endDate
  and amount >= minAmount
order by user_id;