__author__ = 'selver'

import pymysql

class dbCacheHandler:
    tables = dict()
    connection = None
    cursor = None
    def __init__(self, connection):
        self.connection = connection
        cursor = self.connection.cursor()

    def tableColumns(self, tablename):
        if len(tablename) == 0:
            return ''
        if len(self.tables[tablename]) == 0:
            try:
                self.cursor.execute('desc ' + tablename)
                self.tables[tablename] = self.cursor.fetchall()
            except RuntimeError:
                print('Error ' + tablename)
                return ''
        return self.tables[tablename]

class dbHandler:
    connection = None
    cursor = None
    #TODO: make this configurable
    host='localhost'
    user ='root'
    password ='selver365'
    db = 'spielmodell'
    cacheHandler = None

    def __init__(self, h = self.host, u = self.user, p = self.password, db = self.db):
        try:
            self.connection = pymysql.connect(h, u, p, db)

        except pymysql.DatabaseError:
            print('Error connecting to database')
        self.cursor = self.connection.cursor()
        self.cacheHandler = dbCacheHandler(self.connection)

    def insertRecordFromList(self, tablename, list):
        l = len(list)
        if l == 0 or len(tablename):
            return 0
        self.cacheHandler
        statement = 'insert into ' + tablename + ' '

cur.execute("SELECT team1, team2 FROM results LIMIT 10")


for r in cur.fetchall():
   print(r)

cur.close()
conn.close()