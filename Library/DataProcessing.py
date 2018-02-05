import sqlite3

#Database Class
class Database:

    #Create connection to DB, and create a library table containing an id, title, author, year, and isbn for a book
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    #Return all books in the library
    def view(self):
        self.cur.execute("SELECT * FROM library")
        rows = self.cur.fetchall()
        return rows

    #Search and return book that meets certain criteria
    def search(self, title= "", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM library WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    #Insert new book into library
    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO library VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    #Update certain book's data
    def update(self, id, title, author, year, isbn) :
        self.cur.execute("UPDATE library SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    #Delete certain book from library
    def delete(self, id):
        self.cur.execute("DELETE FROM library WHERE id=?", (id,))
        self.conn.commit()

    #Close connection to db
    def __del__(self):
        self.conn.close()
