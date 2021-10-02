CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(256),
    password TEXT
);

CREATE TABLE IF NOT EXISTS log (
    id SERIAL PRIMARY KEY,
    user_id INTEGER(11),
    message_text TEXT,
    verified INT(1),
    creation_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    modification_datetime TIMESTAMP
);