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

    name = sys.argv[4]
    cu = db.cursor()
    cu.execute("""SELECT * FROM states WHERE name
                = %s""", (name))
    rows = cu.fetchall()
    for r in rows:
        print(r)
    cu.close()
    db.close()
