#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query and fetch all rows
    query = "SELECT * FROM cities ORDER BY id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close cursor and database connections
    cursor.close()
    db.close()
