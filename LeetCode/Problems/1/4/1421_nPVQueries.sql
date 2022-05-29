select q.id, q.year, coalesce(n.npv, 0) as npv
from npv n
         right join queries q
                    on n.id = q.id and n.year = q.year