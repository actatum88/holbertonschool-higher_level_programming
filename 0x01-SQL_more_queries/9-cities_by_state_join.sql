-- Lists all cities with their state
-- sorted by city id
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states ON cities.state_id = states.id
