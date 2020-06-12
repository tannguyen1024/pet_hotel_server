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

#If you want to return as object instead of array do this:
#from psycopg2.extras import RealDictCursor
#cur = conn.cursor(cursor_factory=RealDictCursor)

# GET ROUTE FOR PETS AND OWNER OF PET
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

# GET ROUTE FOR OWNERS
@app.route('/owners', methods=['GET'])
def get_owners():
    try:
        cur.execute("SELECT * FROM owners ORDER BY id;")
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


        

# executes our POST with sanitization
# 

if __name__ == '__main__':
    app.run()
