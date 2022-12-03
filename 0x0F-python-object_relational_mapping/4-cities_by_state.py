#!/usr/bin/python3
"""module to use MySQLdb to query databases"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states\
        ON cities.state_id = states.id\
        ORDER BY cities.id")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    for result in results:
        print(result)
