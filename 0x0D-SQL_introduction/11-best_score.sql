-- listing all the records with 10 and above score\
-- the list will be in descending order

SELECT `score`, `name` 
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
