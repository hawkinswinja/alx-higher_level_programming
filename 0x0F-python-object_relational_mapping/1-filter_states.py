#!/usr/bin/python3
"""module to use MySQLdb to query databases"""


if __name__ == '__main__':
    import MySQLdb
    import sys
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states\
                   WHERE BINARY states.name LIKE 'N%'\
                   ORDER BY states.id")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    for result in results:
        print(result)
