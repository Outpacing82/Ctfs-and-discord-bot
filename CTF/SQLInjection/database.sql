DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  password TEXT NOT NULL,
  is_admin BOOLEAN DEFAULT FALSE,
  flag TEXT
);

INSERT INTO users (username, password, is_admin, flag)
VALUES ('admin', 'supersecret', 1, 'flag{sql_injection_ftw}');