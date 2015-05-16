import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

conn.close()