#!/usr/bin/python3
"""module to use MySQLdb to query databases"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT cities.name FROM cities\
        JOIN states\
        ON cities.state_id = states.id\
        WHERE states.name = %s\
        ORDER BY cities.id", (sys.argv[4],))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    cities = ''
    for i in range(0, len(results)):
        cities += results[i][0]
        if i + 1 != len(results):
            cities += ', '
    print(cities)
