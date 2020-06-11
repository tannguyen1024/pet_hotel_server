# Install psycopg2 using: pip3 install psycopg2
import psycopg2

# Establishes connection with postgres
con = psycopg2.connect(
            host="localhost",
            database="pet_hotel",
            user = "postgres",
            password = "postgres",
            port = 5432)

#cursors are the vessel/command in which you communicate with the database.

# cursor
cur = con.cursor()

cur.execute("select id, name")


# You need to CLOSE the connection!
con.close()