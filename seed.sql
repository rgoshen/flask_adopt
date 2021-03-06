
DROP DATABASE IF EXISTS  adopt_db;

CREATE DATABASE adopt_db;

\c adopt_db

CREATE TABLE pets
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  species TEXT NOT NULL,
  photo_url TEXT,
  age INT,
  notes TEXT,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO pets
  (name, species, photo_url, age, notes, available)
VALUES
  ('Woofly', 'dog', 'https://bingvsdevportalprodgbl.blob.core.windows.net/demo-images/c5c7398b-850b-4a7d-b0d9-ef5e10d97bc0.jpg', 3, 'Incredibly adorable.', 't'),
  ('Porchetta', 'porcupine', 'http://kids.sandiegozoo.org/sites/default/files/2017-12/porcupine-incisors.jpg', 4, 'Somewhat spiky!', 't'),
  ('Snargle', 'cat', 'https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg', null, null, 't'),
  ('Dr. Claw', 'cat', null, null, null, 't');

