# Write your MySQL query statement below
DELETE FROM Person p1
WHERE p1.id NOT IN (
    SELECT id FROM (
        SELECT MIN(id) AS id
        FROM Person
        GROUP BY email
    ) AS p3
    );