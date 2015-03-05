__author__ = 'selver'

import pymysql

class dbCacheHandler:
    tables = dict()
    connection = None
    cursor = None
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def tableColumns(self, tablename):
        if len(tablename) == 0:
            return ''
        if len(self.tables.items()) == 0:
            try:
                self.cursor.execute('desc ' + tablename)
                self.tables[tablename] = self.cursor.fetchall()
                print(type(self.tables[tablename]))
            except RuntimeError:
                print('Error ' + tablename)
                return ''
        return self.tables[tablename]

class dbHandler:
    connection = None
    #TODO: make this configurable
    host='localhost'
    user ='root'
    password ='selver365'
    db = 'spielmodell'
    cacheHandler = None

    def __init__(self):
        try:
            self.connection = pymysql.connect(self.host, self.user, self.password, self.db)

        except pymysql.DatabaseError:
            print('Error connecting to database')

        self.cacheHandler = dbCacheHandler(self.connection)

    def __init__(self, h, u, p, db):
        try:
            self.connection = pymysql.connect(h, u, p, db)

        except pymysql.DatabaseError:
            print('Error connecting to database')
        self.cacheHandler = dbCacheHandler(self.connection)

    def insertRecordFromList(self, tablename, list):
        l = len(list)
        print(tablename, list)
        if l == 0 or len(tablename) == 0:
            return 0
        statement = 'insert into ' + tablename + ' ('
        for r in self.cacheHandler.tableColumns(tablename):
            statement += r[0] + ','
        statement = statement[:-1]
        statement += ') values('
        for r in list:
            if 'varchar' in r:
                statement += r + ','
            else:
                statement += '\'' + r + '\','
        statement += ')'
        print('statement: ', statement)
        ret = None
        try:
            cur = self.connection.cursor()
            ret = cur.execute(statement)
            cur.close()
        except RuntimeError:
            print('Error exec statment', statement)
        return ret

    def __del__(self):
        self.connection.close()
