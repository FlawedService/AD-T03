
#already maded queries

add = {
    'ADD USERS': "INSERT INTO users (name, username, password) VALUES (?,?,?)",
    'ADD SERIES': 'INSERT INTO serie (name, start_date, synopse, category_id) VALUES (?,?,?,?)',
    'ADD EPISODE': 'INSERT INTO episode (name, description, serie_id) VALUES (?,?,?)',
    'ADD CLASSIFICATION': 'INSERT INTO classification (initials, description) VALUES (?,?)',
    'ADD CATEGORY': 'INSERT INTO category(name, description) VALUES (?,?)',
    'ADD SERIE_U': 'INSERT INTO list_series (user_id, classification_id, serie_id) VALUES (?,?,?)'
}
#removes should be done by id, but not working for the timebeing
remove = {
    'REMOVE USERS': 'DELETE FROM users WHERE users.name = ?;',
    'REMOVE SERIE': 'DELETE FROM serie WHERE serie.name = ?;',
    'REMOVE EPISODE': 'DELETE FROM episode WHERE episode.name = ?;',
    'REMOVE SERIE_U': 'DELETE FROM list_series WHERE list_series.user_id = ?;'
}

remove_all = {
    'REMOVE ALL USERS': 'DELETE FROM users;',
    'REMOVE ALL SERIES': 'DELETE FROM serie;',
    'REMOVE ALL EPISODES': 'DELETE FROM episode;'
}

show_all ={
    'SHOW ALL USERS': 'SELECT * FROM users;',
    'SHOW ALL SERIES': 'SELECT * FROM serie;',
    'SHOW ALL EPISODES': 'SELECT * FROM episode;',
    'SHOW ALL CATEGORY': 'SELECT * FROM category;',
    'SHOW ALL CLASSIFICATION': 'SELECT * FROM classification;',
    'SHOW ALL SERIE_U': 'SELECT * FROM list_series;'
}
show = {
    'SHOW SERIES USER': 'SELECT * FROM serie INNER JOIN list_series on list_series.user_id = ? and list_series.serie_id = serie.id',
    'SHOW USERS': 'SELECT * FROM users WHERE users.id = ?',
    'SHOW SERIES': 'SELECT * FROM serie WHERE serie.id = ?',
    'SHOW EPISODIOS': 'SELECT * FROM episode WHERE episode.id = ?'
}

update = {
    'UPDATE USER': 'UPDATE users SET password = ? WHERE id = ?;',
    'UPDATE SERIE_U': 'UPDATE list_series SET classification_id = ? WHERE serie_id = ? AND user_id = ?;'
}

showID = {
    'SHOW USER': 'SELECT * FROM users WHERE users.id=?;',
    'SHOW SERIE': 'SELECT * FROM serie where serie.id=?;',
    'SHOW EPISODE': 'SELECT * FROM episode where episode.id=?;',
    'SHOW USER ID': 'SELECT * FROM users where users.username=?;'
}
