-- groups by scores
SELECT score, COUNT(score) 'number' FROM second_table GROUP BY score ORDER BY score DESC