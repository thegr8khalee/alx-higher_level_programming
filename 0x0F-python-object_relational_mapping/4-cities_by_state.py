#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
    )

    cu = db.cursor()
    cu.execute(
        "SELECT states.id, states.name, cities.name FROM states INNER JOIN cities ON states.id = cities.state_id"
    )
    rows = cu.fetchall()
    for r in rows:
        print(r)
    cu.close()
    db.close()
