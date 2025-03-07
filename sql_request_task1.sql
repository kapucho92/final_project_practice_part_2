SELECT c.login,
       COUNT(O.id) AS count_of_orderd
FROM "Couriers" AS c 
LEFT JOIN "Orderd" AS o ON c.id = o.courier.Id 
WHERE o.inDelivery = true
GROUP BY c.login;

