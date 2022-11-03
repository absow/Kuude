-- list all the records in the database
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
