-- display all record with same value.
SELECT COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
