import sqlite3
conn = sqlite3.connect("db.sqlite")

c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS content (title VARCHAR)")

conn.commit()

c = conn.cursor()
c.execute("INSERT INTO content (title) VALUES ('France')")

conn.commit()

c.execute("SELECT * FROM content")
c.fetchall()

c.close()
conn.close()