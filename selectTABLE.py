import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

print 'Tracks:'
cur.execute('SELECT title,plays FROM Tracks')

for row in cur:
	print row

conn.close()