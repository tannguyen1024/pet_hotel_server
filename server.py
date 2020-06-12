# Import flask
import psycopg2
from flask import Flask, jsonify, request

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

@app.route('/pets', methods=['POST'])
def add_pets():
    try:
        cur.execute("INSERT INTO pets (pet_name, breed, color, owners_id) VALUES (%s, %s, %s, %s)", (request.json['name'], request.json['breed'], request.json['color'], request.json['owner_id']))
        con.commit()
        return request.json
    except Exception as e:
        print(e)
        return ()

# Working on figuruing out the url for our delete
@app.route('/pets/<id>', methods=['DELETE'])
def delete_pets(id):
    try:
        cur.execute("DELETE FROM pets WHERE ID={}".format(id))  
        con.commit()
        return 'deleted'
    except Exception as e:
        print(e)
        return ()
        

# executes our POST with sanitization
# 

if __name__ == '__main__':
    app.run()