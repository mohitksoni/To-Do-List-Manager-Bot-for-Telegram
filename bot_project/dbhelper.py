import sqlite3


# Database Class
class DBHelper:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        print("creating table")
        tblstmt = "CREATE TABLE IF NOT EXISTS items (description text, owner text)"
        itemidx = "CREATE INDEX IF NOT EXISTS itemIndex ON items (description ASC)"
        ownidx = "CREATE INDEX IF NOT EXISTS ownIndex ON items (owner ASC)"
        self.conn.execute(tblstmt)
        self.conn.execute(itemidx)
        self.conn.execute(ownidx)
        self.conn.commit()


    def add_item(self, item_text, item_chat):
        stmt = "INSERT INTO items (description, owner) VALUES (?,?)"
        args = (item_text, item_chat)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text,item_chat):
        stmt = "DELETE FROM items WHERE description = (?) AND owner = (?)"
        args = (item_text, item_chat)
        self.conn.execute(stmt, args)
        self.conn.commit()
    #
    def get_items(self, item_chat):
        stmt = "SELECT description FROM items WHERE owner = (?)"
        args=(item_chat,)
        return [x[0] for x in self.conn.execute(stmt,args)]