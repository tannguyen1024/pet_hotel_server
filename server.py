# Install psycopg2 using: pip3 install psycopg2
# Install flask using: pip3 install flask
# Import flask and psycopg2 (for postgres database)
import psycopg2
from flask import Flask, jsonify, request

# Establishes connection with postgres
con = psycopg2.connect(
    host="localhost",
    database="pet_hotel",
    port=5432)

# Activate Cursor:
cur = con.cursor()

# Initiates the app as Flask name
app = Flask(__name__)

# Get Route for Pets with Owner Name JOIN Statement
@app.route('/pets', methods=['GET'])
def get_pets():
    try:
        cur.execute("SELECT pets.id as pet_id, pet_name, breed, color, owners_id, checkin, date, owner_name FROM pets JOIN owners on owners_id = owners.id ORDER BY pet_name;")
        # return the rows
        rows = cur.fetchall()
        result = {'status': 'CREATED'}
        return jsonify(rows)
    except Exception as e:
        print(e)
        return ()

# Get Route for Owners
@app.route('/owners', methods=['GET'])
def get_owners():
    try:
        cur.execute("SELECT * FROM owners ORDER BY id;")
        # Return the Rows
        rows = cur.fetchall()
        result = {'status': 'CREATED'}
        return jsonify(rows)
    except Exception as e:
        print(e)
        return ()

# If you want to return as object instead of array do this:
# from psycopg2.extras import RealDictCursor
# cur = conn.cursor(cursor_factory=RealDictCursor)

# Post Route
@app.route('/pets', methods=['POST'])
def add_pets():
    try:
        cur.execute("INSERT INTO pets (pet_name, breed, color, owners_id) VALUES (%s, %s, %s, %s)", (request.json['name'], request.json['breed'], request.json['color'], request.json['owner_id']))
        con.commit()
        return request.json
    except Exception as e:
        print(e)
        return ()

# Delete Route
@app.route('/pets/<id>', methods=['DELETE'])
def delete_pets(id):
    try:
        cur.execute("DELETE FROM pets WHERE ID={}".format(id))  
        con.commit()
        return 'deleted'
    except Exception as e:
        print(e)
        return ()

# Put Route
@app.route('/pets/update/<int:id>', methods=['PUT'])
def update_pets(id):
    try: 
        if request.json[5]:
           cur.execute("UPDATE pets SET checkin=FALSE WHERE ID={}".format(id))
           con.commit()
           return 'updated to FALSE'
        else:
             cur.execute("UPDATE pets SET checkin=TRUE, date=NOW() WHERE ID={}".format(id))
             con.commit()
             return 'updated to TRUE'     
        return 'updated'
    except Exception as e:
        print(e)
        return 'error'

if __name__ == '__main__':
    app.run()
