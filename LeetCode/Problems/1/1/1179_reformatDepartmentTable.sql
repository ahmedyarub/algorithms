WITH ids AS
         (SELECT DISTINCT id
          FROM Department)
SELECT ids.id,
       d_jan.revenue AS Jan_Revenue,
       d_feb.revenue AS Feb_Revenue,
       d_mar.revenue AS Mar_Revenue,
       d_apr.revenue AS Apr_Revenue,
       d_may.revenue AS May_Revenue,
       d_jun.revenue AS Jun_Revenue,
       d_jul.revenue AS Jul_Revenue,
       d_aug.revenue AS Aug_Revenue,
       d_sep.revenue AS Sep_Revenue,
       d_oct.revenue AS Oct_Revenue,
       d_nov.revenue AS Nov_Revenue,
       d_dec.revenue AS Dec_Revenue
FROM ids
         LEFT JOIN Department d_jan ON d_jan.id = ids.id AND d_jan.month = 'Jan'
         LEFT JOIN Department d_feb ON d_feb.id = ids.id AND d_feb.month = 'Feb'
         LEFT JOIN Department d_mar ON d_mar.id = ids.id AND d_mar.month = 'Mar'
         LEFT JOIN Department d_apr ON d_apr.id = ids.id AND d_apr.month = 'Apr'
         LEFT JOIN Department d_may ON d_may.id = ids.id AND d_may.month = 'May'
         LEFT JOIN Department d_jun ON d_jun.id = ids.id AND d_jun.month = 'Jun'
         LEFT JOIN Department d_jul ON d_jul.id = ids.id AND d_jul.month = 'Jul'
         LEFT JOIN Department d_aug ON d_aug.id = ids.id AND d_aug.month = 'Aug'
         LEFT JOIN Department d_sep ON d_sep.id = ids.id AND d_sep.month = 'Sep'
         LEFT JOIN Department d_oct ON d_oct.id = ids.id AND d_oct.month = 'Oct'
         LEFT JOIN Department d_nov ON d_nov.id = ids.id AND d_nov.month = 'Nov'
         LEFT JOIN Department d_dec ON d_dec.id = ids.id AND d_dec.month = 'Dec'