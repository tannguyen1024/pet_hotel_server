# Import flask
from flask import Flask
app = Flask(__name__)

# Install psycopg2 using: pip3 install psycopg2
import psycopg2

# Establishes connection with postgres
con = psycopg2.connect(
            host="localhost",
            database="pet_hotel",
            port = 5432)

#cursors are the vessel/command in which you communicate with the database.

# cursor
cur = con.cursor()

# executes our POST with sanitization
cur.execute("INSERT INTO pets (pet_name, breed, color, owners_id) VALUES (%s, %s, %s, %s)", ("Billy", "Greyhound", "Brown", 3))

# executes our GET
cur.execute("SELECT pets.id as pet_id, pet_name, breed, color, owners_id, checkin, date, owner_name FROM pets JOIN owners on owners_id = owners.id;")

# return the rows
rows = cur.fetchall()

# Loop through the rows and show it in Terminal
for r in rows:
    print(f"pet_name {r[1]} breed {r[2]} color {r[3]} checkin {r[5]} owner_name {r[7]}")

# This commits the changes from the INSERT statement
con.commit()

# Close the cursor!
cur.close()

# You need to CLOSE the connection!
con.close()
