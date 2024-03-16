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

    cities_name = sys.argv[4]
    cu = db.cursor()
    cu.execute(
        """SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states 
            ON states.id = cities.state_id
            WHERE cities.name = %s
            ORDER BY cities.id""", (cities_name,)
    )
    rows = cu.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cu.close()
    db.close()
