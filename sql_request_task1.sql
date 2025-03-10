SELECT c.login,
       COUNT(O.id) AS count_of_orderd
FROM "Couriers" AS c 
LEFT JOIN "Orders" AS o ON c.id = o."courierId" 
WHERE o."inDelivery" = true
GROUP BY c.login;

