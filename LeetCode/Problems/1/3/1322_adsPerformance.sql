SELECT ad_id,
       IFNULL(ROUND(AVG(CASE
                            WHEN action = 'Clicked' THEN 1
                            WHEN action = 'Viewed' THEN 0 END) * 100, 2), 0) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id