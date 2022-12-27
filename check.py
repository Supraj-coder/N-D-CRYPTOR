'''import pickle
data = {}
y = 255
for x in range(32,256):
	data[chr(x)] = chr(y)
	y-=1
file = open('code.dat','rb')
data=pickle.load(file)
file.close()
print(data)
'''
'''
import sqlite3 as s
con = s.connect('user.db')
cur = con.cursor()
#cur.execute('insert into login values("supraj","1234")')
#con.commit()

#cur.execute('create table login(username text,password text)')
#con.commit()
cur.execute('select*from login')
data = cur.fetchall()
con.close()
print(data)
'''

import sqlite3 as s

con = s.connect('admin.db')
cur = con.cursor()
#cur.execute('create table adlogin (username text,password text)')
#cur.execute('insert into adlogin values("Supraj","admin")')
cur.execute('select * from adlogin')
x = cur.fetchall()
print(x)
#cur.execute('drop table adlogin')
con.commit()
con.close()


'''
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from TkinterDnD2 import DND_FILES,TkinterDnD


def drop_inside_text_box(event):
	print('data: ',event.data)
	data = event.data[1:-1]
	print('data1: ',data)
	if event.data.endswith('.txt}'):
		with open(data,'r') as file:
			for i in file:
				tbox.insert(END,f'{i}\n')
	else:
				tbox.insert(END,'Nothing')

root = TkinterDnD.Tk()
tbox = ScrolledText(root)
tbox.pack()
tbox.drop_target_register(DND_FILES)
tbox.dnd_bind('<<Drop>>',drop_inside_text_box)

root.mainloop()
'''
