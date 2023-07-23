CREATE TABLE app_users (
    email TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    first_name TEXT,
    birthdate TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE app_mails (
    id INT AUTOINCREMENT PRIMARY KEY,
    source TEXT REFERENCES users(email) NOT NULL,
    destination TEXT REFERENCES users(email) NOT NULL,
    object TEXT NOT NULL,
    content TEXT NOT NULL,
    action_date TEXT NOT NULL,
    state INT NOT NULL, -- 0 = not read, 1 = read, 2 = deleted
    is_spam INT NOT NULL -- 0 = not spam, 1 = spam
);

-- for the new model
CREATE TABLE pending_mail_modification (
    id INT AUTOINCREMENT PRIMARY KEY,
    mail_id INT REFERENCES mails(id) NOT NULL
);