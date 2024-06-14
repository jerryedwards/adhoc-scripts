SELECT o.name AS organization_name, SUM(d.amount) AS amount_raised
FROM donations d
INNER JOIN organizations o ON d.organization_id = o.id
WHERE d.date_received = '2023-12-03'
AND d.status = 'paid'
GROUP BY o.name