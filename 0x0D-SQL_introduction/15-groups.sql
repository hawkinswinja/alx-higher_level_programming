-- count and group by implementation
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score;
