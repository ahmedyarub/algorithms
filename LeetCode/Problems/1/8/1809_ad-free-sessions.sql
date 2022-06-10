SELECT session_id
FROM Playback
         LEFT JOIN Ads
                   ON Playback.customer_id = Ads.customer_id AND timestamp BETWEEN start_time and end_time
WHERE ad_id IS NULL;