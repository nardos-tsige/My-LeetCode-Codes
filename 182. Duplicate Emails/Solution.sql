# Write your MySQL query statement below
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(1) > 1;
