DROP SCHEMA IF EXISTS ws CASCADE;

BEGIN;

CREATE SCHEMA ws;

CREATE TABLE ws.users ( --WORKSHOP.users
  uid SERIAL PRIMARY KEY, --User_ID
  username varchar(20) UNIQUE CHECK (username ~ '[^\s]+'),
  password text NOT NULL,
  address text NOT NULL
);

CREATE TABLE ws.categories (
  cid SERIAL PRIMARY KEY, --CATEGORY_ID
  name text UNIQUE NOT NULL
);

CREATE TABLE ws.products (
  pid SERIAL PRIMARY KEY, --PRODUCT_ID
  name text NOT NULL,
  price float NOT NULL CHECK (price >= 0),
  cid int REFERENCES ws.categories(cid),
  description text
);


CREATE TABLE ws.orders (
  oid SERIAL PRIMARY KEY,
  uid int REFERENCES ws.users(uid),
  pid int REFERENCES ws.products(pid),
  num int NOT NULL,
  date date NOT NULL,
  payed int NOT NULL CHECK (payed = 0 OR payed = 1)
);

COMMIT;
