CREATE TABLE "owners" 
("id" SERIAL PRIMARY KEY, 
"owner_name" VARCHAR (80) UNIQUE NOT NULL);

CREATE TABLE "pets" 
("id" SERIAL PRIMARY KEY, 
"pet_name" VARCHAR (80) NOT NULL, 
"breed" VARCHAR (80) NOT NULL, 
"color" VARCHAR (80) NOT NULL, 
"checkin" BOOLEAN DEFAULT FALSE, 
"date" TIMESTAMP DEFAULT NOW(),
"owners_id" INT,
FOREIGN KEY ("owners_id") REFERENCES "owners" ("id"));

INSERT INTO "owners" (owner_name) VALUES ('Natalie'), ('Tan'), ('Mike'), ('Chinmaya');

INSERT INTO "pets" (pet_name, breed, color, owners_id) VALUES 
('Artemis', 'Blue Heeler', 'Black', 1),
('Apollo', 'Border Collie', 'Black', 1),
('Kina', 'Yorkie Poodle', 'Black', 2),
('Bullet', 'Greyhound', 'Blondish', 3),
('Dunno', 'Corgi', 'Brown', 4);