SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits
         LEFT JOIN Transactions USING (visit_id)
WHERE transaction_id IS NULL
GROUP BY customer_id;