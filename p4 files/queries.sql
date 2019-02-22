
------- ADD QUERIES -------
-- ADD USER --
INSERT INTO users (name, username, password) values (?,?,?);

-- ADD SERIE --
INSERT INTO serie (name, start_date, synopse, category_id) VALUES (?,?,?,?);

-- ADD EPISODE --
INSERT INTO episode (name, description, serie_id) VALUES (?,?,?);

------- REMOVE QUERIES -------
-- REMOVE USER --
DELETE FROM users WHERE id = ?;

-- REMOVE SERIE --
DELETE FROM serie WHERE id = ?;

-- REMOVE EPISODE --
DELETE FROM episode WHERE id = ?;

-- REMOVE ALL USERS--
DELETE FROM users;

-- REMOVE ALL SERIES --
DELETE FROM serie;

-- REMOVE ALL EPISODES --
DELETE FROM episode;

------- SHOW QUERIES -------
-- SHOW ALL USERS --
SELECT * FROM users;

-- SHOW ALL SERIES --
SELECT * FROM serie;

-- SHOW ALL EPISODE __
SELECT * FROM episode;

-- SHOW ALL CATEGORIES --
SELECT * FROM category;

-- SHOW ALL CLASSIFICATIONS --
SELECT * FROM classification;


------- UPDATE QUERIES -------
-- UPDATE USERS --
UPDATE users SET name = ?, username = ?, password = ? WHERE id = ?;
-- UPDATE SERIES --
UPDATE serie SET synopse = ? WHERE id = ? AND  category_id = ?;
