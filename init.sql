CREATE TABLE IF NOT EXISTS movies (
    movie_id serial PRIMARY KEY,
    preference_key INTEGER NOT NULL,
    movie_title VARCHAR NOT NULL,
    rating DOUBLE NOT NULL,
    year INTEGER NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY,
    email VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    name VARCHAR NOT NULL,
    magic_number = INTEGER NOT NULL
);