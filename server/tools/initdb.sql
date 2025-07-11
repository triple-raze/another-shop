CREATE TYPE GENDER as ENUM('male', 'female');

CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(50) NOT NULL, 
    gender GENDER NOT NULL, 
    email VARCHAR(150) NOT NULL, 
    password VARCHAR(30) NOT NULL, 
    registration_timestamp DATE DEFAULT CURRENT_DATE
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(100) NOT NULL,
    description VARCHAR(1000),
    price INT NOT NULL, 
    old_price INT
);

CREATE TABLE cart_products (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id), 
    product_id INT REFERENCES products(id)
)