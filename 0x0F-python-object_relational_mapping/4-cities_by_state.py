#!/usr/bin/python3

"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
with conn.cursor() as cur:
    cur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)
    query_rows = cur.fetchall()
for row in query_rows:
    print(row)
