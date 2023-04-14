#!/usr/bin/python3
"""Displays all states from the database hbtn_0e_0_usa
where name matches the argument"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], )

    # Create cursor to execute SQL queries
    cursor = db.cursor()

    # Define the SQL query to select all states where name matches the argument
    state_name = sys.argv[4]
    query ="SELECT * FROM states WHERE name='{}'ORDER BY id ASC".format(state_name)

    # Execute the SQL query
    cursor.execute(query)

    # Fetch all rows and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connections
    cursor.close()
    db.close()
