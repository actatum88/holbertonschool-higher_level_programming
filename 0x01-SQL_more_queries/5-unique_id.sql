-- creates the table 'unique_id'
-- id defaults to 1 and must be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));.
