#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query and fetch all rows
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name=%s ORDER BY cities.id ASC"
    state_name = (sys.argv[4],)
    cursor.execute(query, state_name)
    rows = cursor.fetchall()

    # Print the results
    print(", ".join(city[0] for city in rows))

    # Close cursor and database connections
    cursor.close()
    db.close()
