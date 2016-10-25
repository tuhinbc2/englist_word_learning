import sqlite3


sqlite_file = "data.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

class db:
    def __init__(self, tableName):
        self.tableName = tableName
        self.createTable()

    def createTable(self):
        c.execute("create table if not exists {}(id integer PRIMARY KEY autoincrement, word varchar(100))".format
            (self.tableName))
        conn.commit()
        #print("done")

    def add(self, data):
        if self.find(data) == False:
            c.execute("insert into {}(word) values('{}')".format(self.tableName, data))
            conn.commit()

    def remove(self, data):
        c.execute("delete from {} where word='{}'".format(self.tableName, data))
        conn.commit()

    def printall(self):
        c.execute("select * from {}".format(self.tableName))
        rows = c.fetchall()
        print(rows)

    def find(self, data):
        c.execute("select * from {} where word='{}'".format(self.tableName, data))
        rows = c.fetchall()
        if len(rows) < 1:
            return False
        #return rows[0][0]
        return True

    def fetchtop5(self):
        c.execute("select * from {} limit 5;".format(self.tableName))
        return c.fetchall()


#c.execute("drop table list")

#c.execute("insert into list(word) values('tuhin')")
#c.execute("delete from list where id=3")

# c.execute("select * from list")
# all_rows = c.fetchall()
# print('1):', all_rows)
# conn.commit()
# conn.close()