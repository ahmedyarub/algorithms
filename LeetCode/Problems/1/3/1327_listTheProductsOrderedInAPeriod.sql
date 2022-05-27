select product_name, sum(unit) as unit
from Products a
         left join Orders b on a.product_id = b.product_id
where month(order_date) = 2
  and year(order_date) = '2020'
group by a.product_id
Having unit >= 100