#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT c.name FROM cities AS c \
                JOIN states AS s ON s.id = c.state_id \
                WHERE s.name = %s", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        for col in row:
            print(col + ", ", end='')
    print("")
    cur.close()
    conn.close()
