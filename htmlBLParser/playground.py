__author__ = 'selver'
import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='selver365', db='spielmodell')

cur = conn.cursor()

#let's look at IDs and names coming from the database
cur.execute("SELECT ID, team1, team2 FROM results LIMIT 10")

# r = cur.fetchall()
# print r
# ...or...
for r in cur.fetchall():
   print(r[0], r[1], "\t-\t", r[2])

cur.close()
conn.close()

s = "this is a string with a ,"

nocomma = s[:-3]

print(nocomma)