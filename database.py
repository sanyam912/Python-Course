import sqlite3
db = sqlite3.connect('a.db')
cr = db.cursor()
#a=input("")
#b=input("")
#cr.execute('''create table a1(id text,name text)''')
#cr.execute(f'''insert into a1 values('{a}','{b}')''')
cr.execute('''select * from a1 where id = 'bye' ''')
#u=cr.fetchall() #or
u=cr.fetchone()
print(u)
db.commit()
