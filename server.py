# Import flask
import psycopg2
from flask import Flask, jsonify

# Install psycopg2 using: pip3 install psycopg2

# Establishes connection with postgres
con = psycopg2.connect(
    host="localhost",
    database="pet_hotel",
    port=5432)

# cursor
cur = con.cursor()

app = Flask(__name__)

# GET ROUTE FOR PETS AND OWNER OF PET
@app.route('/pets', methods=['GET'])
def get_pets():
    try:
        cur.execute("SELECT pets.id as pet_id, pet_name, breed, color, owners_id, checkin, date, owner_name FROM pets JOIN owners on owners_id = owners.id;")
        # return the rows
        rows = cur.fetchall()
        result = {'status': 'CREATED'}
        return jsonify(rows)
    except Exception as e:
        print(e)
        return ()


# executes our POST with sanitization
# cur.execute("INSERT INTO pets (pet_name, breed, color, owners_id) VALUES (%s, %s, %s, %s)", ("Billy", "Greyhound", "Brown", 3))

if __name__ == '__main__':
    app.run()