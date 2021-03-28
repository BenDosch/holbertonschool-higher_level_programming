#!/usr/bin/python3
""" Write a script that lists all cities from the database hbtn_0e_4_usa
Your script should take 3 arguments:
mysql username, mysql password and database name
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities AS c \
                JOIN states AS s ON s.id = c.state_id \
                ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
