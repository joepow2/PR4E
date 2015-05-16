import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title,plays) VALUES ("Kobe Bryant",19)')
conn.commit()

conn.close()