from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import colorchooser
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
import pickle
import sqlite3 as s
from PIL import ImageTk, Image
#adlogin:admin login:employee

class Application():
	def __init__(self):
		self.app = Tk()
		self.bg = ImageTk.PhotoImage(file = 'background.png')
		self.sbg = ImageTk.PhotoImage(file = 'sbackground.png')
		self.see = PhotoImage(file = 'see.png')
		self.dont_see = PhotoImage(file = "don't_see.png")
		self.cc = 1
		self.scc = 1
		self.scc1 = 1
		self.as_c = 1
		self.as_c1 = 1

	def resizer(self,event):
		self.bg0 = Image.open('background.png')
		self.bg1 = self.bg0.resize((event.width,event.height),Image.ANTIALIAS)
		self.bg2 = ImageTk.PhotoImage(self.bg1)
		self.frame1.create_image(0,0, image = self.bg2,anchor = 'nw')

	def Focus1(self,event):
		self.en2.focus_set()

	def Focus2(self,event):
		self.signin()

	def See(self):
		if self.cc == 0:
			self.bu2['image'] = self.see
			self.cc = 1
			self.en2['show'] = '*'
		else:
			self.bu2['image'] = self.dont_see
			self.cc = 0
			self.en2['show'] = ''

	def signin(self):
		self.con = s.connect('user.db')
		self.cur = self.con.cursor()
		self.cur.execute('select*from login')
		self.userdata = self.cur.fetchall()
		self.con.close()
		self.con = s.connect('admin.db')
		self.cur = self.con.cursor()
		self.cur.execute('select*from adlogin')
		self.admindata = self.cur.fetchall()
		self.con.close()
		if self.en1.get()!='' and self.en2.get()!='':
			if (self.en1.get(),self.en2.get()) in self.userdata:
				self.frame1.destroy()
				self.app.title('Text Editor')
				self.Frame3()
			elif (self.en1.get(),self.en2.get()) in self.admindata:
				self.frame1.destroy()
				self.app.title('Encrypt/Decrypt')
				self.Frame2()
			else:
				messagebox.showerror('Error','Incorrect username or password')
		else:
			messagebox.showerror('Error','All the fields must be filled')

	def sresizer(self,event):
		self.sbg0 = Image.open('sbackground.png')
		self.sbg1 = self.sbg0.resize((event.width,event.height),Image.ANTIALIAS)
		self.sbg2 = ImageTk.PhotoImage(self.sbg1)
		self.frame0.create_image(0,0, image = self.sbg2,anchor = 'nw')

	def adduser(self):
		if self.sen.get()!='' and self.sen1.get()!='' and self.sen2.get()!='':
			self.file = s.connect('admin.db')
			self.cur1 = self.file.cursor()
			self.cur1.execute('select*from adlogin')
			self.data1 = self.cur1.fetchall()
			self.file.close()
			self.con = s.connect('user.db')
			self.cur = self.con.cursor()
			self.cur.execute('select*from login')
			self.data = self.cur.fetchall()
			if (self.sen.get(),self.sen1.get()) not in self.data1:
				if (self.sen.get(),self.sen1.get()) not in self.data and self.sen1.get()==self.sen2.get():
					self.yn = messagebox.askokcancel('Verification','Username and password will be saved')
					if self.yn==True:
						self.cur.execute(f"insert into login values('{self.sen.get()}','{self.sen1.get()}')")
						self.con.commit()
						self.con.close()
						messagebox.askokcancel('Information','Signed up successfully!!!')
						self.win.focus_set()
					else:
						self.con.close()
						messagebox.askokcancel('Information','User data not added')
						self.win.focus_set()
				else:
					messagebox.showerror('Error','User already exists!!!\nor password not confirmed!!!')
					self.con.close()
					self.win.focus_set()
			else:
				messagebox.showerror('Error','User cannot be added')
				self.win.focus_set()
		else:
			messagebox.showerror('Error','All fields must be filled!!!')
			self.win.focus_set()

	def sSee1(self):
		if self.scc1 == 0:
			self.sbu2['image'] = self.see
			self.scc1 = 1
			self.sen2['show'] = '*'
		else:
			self.sbu2['image'] = self.dont_see
			self.scc1 = 0
			self.sen2['show'] = ''

	def sSee(self):
		if self.scc == 0:
			self.sbu1['image'] = self.see
			self.scc = 1
			self.sen1['show'] = '*'
		else:
			self.sbu1['image'] = self.dont_see
			self.scc = 0
			self.sen1['show'] = ''

	def Focus0(self,event):
		self.sen1.focus_set()

	def Focus01(self,event):
		self.sen2.focus_set()

	def Focus02(self,event):
		self.adduser()

	def on_closing(self):
		self.bu['state'] = 'normal'
		self.scc = 1
		self.scc1 = 1
		self.win.destroy()

	def signup(self):
		self.bu['state'] = 'disabled'
		self.win = Toplevel(self.app)
		self.win.geometry('800x600')
		self.win.state('zoomed')
		self.win.title('Sign-up')
		self.frame0 = Canvas(self.win,highlightthickness = 0)
		self.frame0.pack(fill = 'both',expand = True)
		self.frame0.create_image(0,0, image = self.sbg,anchor = 'nw')
		self.frame0.bind('<Configure>',self.sresizer)
		self.sen = Entry(self.win,width = 15,font = ('Arial Rounded MT Bold',20))
		self.sen.place(relx = 0.325,rely = 0.45)
		self.sen1 = Entry(self.win,width = 15,font = ('Arial Rounded MT Bold',20),show = '*')
		self.sen1.place(relx = 0.325,rely = 0.585)
		self.sen2 = Entry(self.win,width = 15,font = ('Arial Rounded MT Bold',20),show = '*')
		self.sen2.place(relx = 0.325,rely = 0.715)
		self.sbu = Button(self.win,text = 'Sign-up',bg = '#FFC102',activebackground = '#FFC102',relief = 'flat',fg = '#8C7CA3',font = ('Arial Rounded MT Bold',20),width = 6,height = 1,activeforeground = '#8C7CA3',command = self.adduser)
		self.sbu.place(relx = 0.45,rely = 0.8)
		self.sbu1 = Button(self.win,image = self.see,borderwidth = 0,bg = '#A16CB2',activebackground = '#A16CB2',command = self.sSee)
		self.sbu1.place(relx = 0.515,rely = 0.5895)
		self.sbu2 = Button(self.win,image = self.see,borderwidth = 0,bg = '#A16CB2',activebackground = '#A16CB2',command = self.sSee1)
		self.sbu2.place(relx = 0.515,rely = 0.7195)
		self.sen.focus_set()
		self.sen.bind('<Return>',self.Focus0)
		self.sen1.bind('<Return>',self.Focus01)
		self.sen2.bind('<Return>',self.Focus02)
		self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.win.mainloop()

	def Frame1(self):
		self.db_a = s.connect('admin.db')
		self.cur_a = self.db_a.cursor()
		self.cur_a.execute('select*from adlogin')
		self.data = self.cur_a.fetchall()
		self.db_a.close()
		if ('Supraj', 'admin') not in self.data:
			self.app.destroy()
		self.app.title('User login')
		self.app.state('zoomed')
		self.frame1 = Canvas(self.app,highlightthickness = 0)
		self.frame1.pack(fill = 'both',expand = True)
		self.frame1.create_image(0,0, image = self.bg,anchor = 'nw')
		self.frame1.bind('<Configure>',self.resizer)
		self.en1 = Entry(self.frame1,width = 15,font = ('Arial Rounded MT Bold',20))
		self.en1.place(relx = 0.325,rely = 0.525)
		self.en2 = Entry(self.frame1,width = 15,font = ('Arial Rounded MT Bold',20),show = '*')
		self.en2.place(relx = 0.325,rely = 0.665)
		self.bu = Button(self.frame1,text = 'Forgot password?',relief = 'groove',bg = '#8C7CA3',activebackground = '#8C7CA3',fg = '#FFC102',font = ('Arial Rounded MT Bold',10),activeforeground = '#FFC102',command = self.signup,borderwidth = 0)
		self.bu.place(relx = 0.325,rely = 0.72)
		self.bu1 = Button(self.frame1,text = 'Sign-in',bg = '#FFC102',activebackground = '#FFC102',relief = 'flat',fg = '#8C7CA3',font = ('Arial Rounded MT Bold',20),width = 6,height = 1,activeforeground = '#8C7CA3',command = self.signin)
		self.bu1.place(relx = 0.45,rely = 0.8)
		self.bu2 = Button(self.frame1,image = self.see,borderwidth = 0,bg = '#A16CB2',activebackground = '#A16CB2',command = self.See)
		self.bu2.place(relx = 0.515,rely = 0.675)
		self.en1.focus_set()
		self.en1.bind('<Return>',self.Focus1)
		self.en2.bind('<Return>',self.Focus2)

	def Encrypt(self):
		self.out.config(state = NORMAL)
		self.out.delete(1.0,END)
		self.file = open('code.dat','rb')
		self.data = pickle.load(self.file)
		self.file.close()
		self.data1 = self.inp.get(1.0, END)
		self.lis = self.data1.split('\n')
		for i in self.lis:
			self.out.config(state = NORMAL)
			self.str1 = ''
			for j in range(len(i)):
				self.str1+=self.data[i[j]]
			self.out.insert(END,self.str1+'\n')
			self.out.config(state = DISABLED)

	def Clear(self):
		self.out.config(state = NORMAL)
		self.out.delete(1.0,END)
		self.out.config(state = DISABLED)

	def saf(self):
		if self.inp.get('1.0',END)!='\n' and self.out.get('1.0',END)!='\n':
			self.text_file = filedialog.asksaveasfilename(defaultextension = '.*',initialdir = 'C:/Users/user/Desktop/Project',title = 'Save As',filetypes = (('Text Files','*.txt'),('Python','*.py'),('All Files','*.*')))
			if self.text_file:
				self.name = self.text_file
				self.name = self.name.replace('C:/Users/user/Desktop/','')
				self.text_file = open(self.text_file,'w')
				self.text_file.write('Input:\n'+self.inp.get('1.0',END)+'\n\nOutput:\n'+self.out.get('1.0',END))
				self.text_file.close()
				messagebox.askokcancel('Information','Data Saved As File')
		else:
			messagebox.showerror('Error','Complete Data Not Found!!!')

	def on_closing_as(self):
		self.admin_set['state'] = 'normal'
		as_c = 1
		as_c1 = 1
		self.win_as.destroy()

	def Focus_as0(self,event):
		self.ps_as.focus_set()

	def Focus_as1(self,event):
		self.ps_as25.focus_set()

	def See_as(self):
		if self.as_c == 0:
			self.sd['image'] = self.see
			self.as_c = 1
			self.ps_as['show'] = '*'
		else:
			self.sd['image'] = self.dont_see
			self.as_c = 0
			self.ps_as['show'] = ''

	def See_as1(self):
		if self.as_c1 == 0:
			self.sd25['image'] = self.see
			self.as_c1 = 1
			self.ps_as25['show'] = '*'
		else:
			self.sd25['image'] = self.dont_see
			self.as_c1 = 0
			self.ps_as25['show'] = ''

	def Update(self):
		self.as_info['state'] = 'normal'
		self.as_info.delete('1.0',END)
		self.db_a = s.connect('admin.db')
		self.cur_a = self.db_a.cursor()
		self.cur_a.execute('select*from adlogin')
		self.data = self.cur_a.fetchall()
		self.db_a.close()
		self.as_info.insert(END,'    Admin(s):\n')
		if len(self.data) == 1:
			self.as_info.insert(END,'(No Admin Records Found!!!)\n')
		else:
			for i in range(1,len(self.data)):
				self.as_info.insert(END,'  Username: '+self.data[i][0]+'\n')
				self.as_info.insert(END,'  Password: '+self.data[i][1]+'\n\n')
		self.file = s.connect('user.db')
		self.cur_f = self.file.cursor()
		self.cur_f.execute('select*from login')
		self.data = self.cur_f.fetchall()
		self.file.close()
		self.as_info.insert(END,'\n    User(s):\n')
		if len(self.data) == 0:
			self.as_info.insert(END,'(No User Records Found!!!)\n')
		else:
			for j in range(len(self.data)):
				self.as_info.insert(END,'  Username: '+self.data[j][0]+'\n')
				self.as_info.insert(END,'  Password: '+self.data[j][1]+'\n\n')
		self.as_info['state'] = 'disabled'

	def make_ad(self):
		if self.un_as.get()!='' and self.ps_as.get()!='' and self.ps_as25.get()!='':
			if self.ps_as.get()==self.ps_as25.get():
				self.file = s.connect('admin.db')
				self.cur = self.file.cursor()
				self.cur.execute('select*from adlogin')
				self.data = self.cur.fetchall()
				self.file1 = s.connect('user.db')
				self.cur1 = self.file1.cursor()
				self.cur1.execute('select*from login')
				self.data1 = self.cur1.fetchall()
				self.file1.close()
				if (self.un_as.get(),self.ps_as.get()) not in self.data1:
					if (self.un_as.get(),self.ps_as.get()) in self.data:
						messagebox.showerror('Error','Admin already exists!!!')
						self.file.close()
						self.win_as.focus_set()
					else:
						self.cur.execute(f'insert into adlogin values("{self.un_as.get()}","{self.ps_as.get()}")')
						self.file.commit()
						self.file.close()
						messagebox.askokcancel('Information','Admin added')
						self.Update()
						self.win_as.focus_set()
				else:
					messagebox.showerror('Error','Admin cannot be added')
					self.file.close()
					self.win_as.focus_set()
			else:
				messagebox.showerror('Error','Password not confirmed!!!')
				self.win_as.focus_set()

		else:
			messagebox.showerror('Error','All fields must be filled!!!')
			self.win_as.focus_set()

	def remove_ad(self):
		if self.ps_as.get() !='' and self.ps_as25.get() !='' and self.un_as.get() !='':
			if self.ps_as.get()==self.ps_as25.get():
				self.file = s.connect('admin.db')
				self.cur = self.file.cursor()
				self.cur.execute('select*from adlogin')
				self.data = self.cur.fetchall()
				self.file1 = s.connect('user.db')
				self.cur1 = self.file1.cursor()
				self.cur1.execute('select*from login')
				self.data1 = self.cur1.fetchall()
				if (self.un_as.get(),self.ps_as.get()) in self.data1:
					self.file.close()
					self.cur1.execute(f'DELETE FROM login WHERE username = "{self.un_as.get()}" and password = "{self.ps_as.get()}"')
					self.file1.commit()
					self.file1.close()
					messagebox.askokcancel('Information','User data removed')
					self.Update()
					self.win_as.focus_set()
				elif (self.un_as.get(),self.ps_as.get()) in self.data and (self.un_as.get(),self.ps_as.get()) != ('Supraj','admin'):
					self.file1.close()
					self.cur.execute(f'DELETE FROM adlogin WHERE username = "{self.un_as.get()}" and password = "{self.ps_as.get()}"')
					self.file.commit()
					self.file.close()
					messagebox.askokcancel('Information','Admin data removed')
					self.Update()
					self.win_as.focus_set()
				else:
					messagebox.showerror('Error','User data not found!!!')
					self.win_as.focus_set()
			else:
				messagebox.showerror('Error','Password not confirmed!!!')
				self.win_as.focus_set()
		else:
			messagebox.showerror('Error','All fields must be filled!!!')
			self.win_as.focus_set()

	def ad_set(self):
		self.admin_set['state'] = 'disabled'
		self.win_as = Toplevel(self.app,bg = '#3b3838')
		self.win_as.title('Admin Settings')
		self.win_as.state('zoomed')
		Label(self.win_as,text = 'Information',bg = '#3b3838',font = ('segoe ui black',25),fg = '#cdcdcd').place(relx =0.455,rely = 0)
		self.as_info = ScrolledText(self.win_as,width = 132,height = 24,bg = '#262626',fg = '#00b0f0',insertbackground = '#ffffff',borderwidth = 0,font = ('Arial Rounded MT Bold',))
		self.as_info.place(relx = 0.01,rely = 0.06)
		self.db_a = s.connect('admin.db')
		self.cur_a = self.db_a.cursor()
		self.cur_a.execute('select*from adlogin')
		self.data = self.cur_a.fetchall()
		self.db_a.close()
		self.as_info.insert(END,'    Admin(s):\n')
		if len(self.data) == 1:
			self.as_info.insert(END,'(No Admin Records Found!!!)\n')
		else:
			for i in range(1,len(self.data)):
				self.as_info.insert(END,'  Username: '+self.data[i][0]+'\n')
				self.as_info.insert(END,'  Password: '+self.data[i][1]+'\n\n')
		self.file = s.connect('user.db')
		self.cur_f = self.file.cursor()
		self.cur_f.execute('select*from login')
		self.data = self.cur_f.fetchall()
		self.file.close()
		self.as_info.insert(END,'\n    User(s):\n')
		if len(self.data) == 0:
			self.as_info.insert(END,'(No User Records Found!!!)\n')
		else:
			for j in range(len(self.data)):
				self.as_info.insert(END,'  Username: '+self.data[j][0]+'\n')
				self.as_info.insert(END,'  Password: '+self.data[j][1]+'\n\n')
		self.as_info['state'] = 'disabled'
		Label(self.win_as,text = 'Username',bg = '#3b3838',font = ('segoe ui black',15),fg = '#cdcdcd',width = 10).place(relx = 0.034,rely = 0.69)
		self.un_as = Entry(self.win_as,font = ('Arial Rounded MT Bold',15),bg = '#262626',fg = '#e94545',insertbackground = '#ffffff',borderwidth = 0)
		self.un_as.place(relx = 0.0425,rely = 0.73)
		self.un_as.focus_set()
		Label(self.win_as,text = 'Password',bg = '#3b3838',font = ('segoe ui black',15),fg = '#cdcdcd').place(relx = 0.04,rely = 0.795)
		self.ps_as = Entry(self.win_as,show = '*',font = ('Arial Rounded MT Bold',15),bg = '#262626',fg = '#e94545',insertbackground = '#ffffff',borderwidth = 0)
		self.ps_as.place(relx = 0.0425,rely = 0.835)
		self.sd = Button(self.win_as,image = self.see,borderwidth = 0,bg = '#3b3838',activebackground = '#3b3838',command = self.See_as)
		self.sd.place(relx = 0.2425,rely = 0.835)
		Label(self.win_as,text = 'Confirm Password',bg = '#3b3838',font = ('segoe ui black',15),fg = '#cdcdcd').place(relx = 0.04,rely = 0.9)
		self.ps_as25 = Entry(self.win_as,show = '*',font = ('Arial Rounded MT Bold',15),bg = '#262626',fg = '#e94545',insertbackground = '#ffffff',borderwidth = 0)
		self.ps_as25.place(relx = 0.0425,rely = 0.94)
		self.sd25 = Button(self.win_as,image = self.see,command = self.See_as1,borderwidth = 0,bg = '#3b3838',activebackground = '#3b3838')
		self.sd25.place(relx = 0.2425,rely = 0.94)
		self.image_file = PhotoImage(file = 'logo.png')
		Label(self.win_as,image = self.image_file,borderwidth = 0).place(relx = 0.375,rely =0.725)
		self.ma = Button(self.win_as,width = 12,height = 1,text = 'MAKE ADMIN',relief = 'groove',font = ('segoe ui black',15),bg = '#878181',activebackground = '#878181',borderwidth = 0,command = self.make_ad)
		self.ma.place(relx = 0.65,rely =0.75)
		self.ra = Button(self.win_as,width = 12,height = 1,text = 'REMOVE USER',relief = 'groove',font = ('segoe ui black',15),bg = '#878181',activebackground = '#878181',borderwidth = 0,command = self.remove_ad)
		self.ra.place(relx = 0.65,rely = 0.9)
		self.un_as.bind('<Return>',self.Focus_as0)
		self.ps_as.bind('<Return>',self.Focus_as1)
		self.win_as.protocol("WM_DELETE_WINDOW", self.on_closing_as)

	def logout(self):
		self.frame2.destroy()
		self.Frame1()

	def open_file_f2(self):
		self.inp.delete('1.0',END)
		self.out['state'] = 'normal'
		self.out.delete('1.0',END)
		self.out['state'] = 'disabled'
		self.text_file = filedialog.askopenfilename(initialdir = 'C:/Users/user/Desktop/Project/Saved Files',title = 'Open File',filetypes = (('Text Files','*.txt'),('Python','*.py'),('All Files','*.*')))
		if self.text_file:
			self.text_file = open(self.text_file,'r')
			self.data = self.text_file.read()
			self.text_file.close()
			self.inp.insert(END,self.data)
			self.Encrypt()

	def Frame2(self):
		self.frame2 = Frame(self.app)
		self.frame2.pack(fill = 'both',expand = 1)
		self.frame21 = Frame(self.frame2)
		self.frame21.pack(side = 'top',expand = 1,fill = 'both')
		self.frame211 = Frame(self.frame21,bg = '#3b3838')
		self.frame211.pack(side = 'left',fill = 'both',expand = 1)
		Button(self.frame211,text = 'INPUT',relief = 'groove',font = ('segoe ui black',10),bg = '#878181',activebackground = '#878181',borderwidth = 0).pack(side = 'top',fill = 'both',expand = 1,padx = 300)
		self.inp = ScrolledText(self.frame211,bg = '#262626',fg = '#00b0f0',insertbackground = '#ffffff',borderwidth = 0,height = 30,font = ('Arial Rounded MT Bold',),width = 69)
		self.inp.pack(fill = 'both',expand = 1,padx = 3,pady = 3)
		self.frame212 = Frame(self.frame21,bg = '#3b3838')
		self.frame212.pack(fill = 'both',expand = 1)
		Button(self.frame212,text = 'OUTPUT',relief = 'groove',font = ('segoe ui black',10),bg = '#878181',activebackground = '#878181',borderwidth = 0).pack(side = 'top',expand = 1,fill = 'both',padx = 275)
		self.out = ScrolledText(self.frame212,bg = '#262626',fg = '#e94545',insertbackground = '#ffffff',borderwidth = 0,height = 30,font = ('Arial Rounded MT Bold',))
		self.out.pack(fill = 'both',expand = 1,pady = 3)
		self.frame22 = Frame(self.frame2,bg = '#3b3838')
		self.frame22.pack(fill = 'both',expand = 1)
		self.enc = Button(self.frame22,text = 'ENCRYPT',command = self.Encrypt,relief = 'groove',font = ('segoe ui black',10),activebackground = '#4d4d4d',bg = '#4d4d4d',borderwidth = 0,fg = '#cdcdcd')
		self.enc.pack(side = 'left',expand = 1,fill = 'both',padx = 4,pady = 4)
		self.c = Button(self.frame22,text = 'CLEAR',command = self.Clear,relief = 'groove',font = ('segoe ui black',10),activebackground = '#4d4d4d',bg = '#4d4d4d',borderwidth = 0,fg = '#cdcdcd')
		self.c.pack(expand = 1,fill = 'both',side = 'left',padx = 4,pady = 4)
		self.dec = Button(self.frame22,text = 'DECRYPT',command = self.Encrypt,relief = 'groove',font = ('segoe ui black',10),activebackground = '#4d4d4d',bg = '#4d4d4d',borderwidth = 0,fg = '#cdcdcd')
		self.dec.pack(expand = 1,fill = 'both',side = 'right',padx = 4,pady = 4)
		self.frame23 = Frame(self.frame2,bg = '#3b3838')
		self.frame23.pack(side = 'bottom',fill = 'both',expand = 1)
		self.admin_set = Button(self.frame23,text = 'ADMIN SETTINGS',command = self.ad_set,relief = 'groove',font = ('segoe ui black',10),activebackground = '#4d4d4d',bg = '#4d4d4d',borderwidth = 0,fg = '#cdcdcd')
		self.admin_set.pack(expand = 1,side = 'left',fill = 'both',padx = 4,pady = 4)
		self.sf = Button(self.frame23,text = 'SAVE AS FILE',command = self.saf,relief = 'groove',font = ('segoe ui black',10),activebackground = '#4d4d4d',bg = '#4d4d4d',borderwidth = 0,fg = '#cdcdcd')
		self.sf.pack(expand = 1,fill = 'both',side = 'left',padx = 4,pady = 4)
		self.op = Button(self.frame23,text = 'OPEN FILE',command = self.open_file_f2,relief = 'groove',font = ('segoe ui black',10),activebackground = '#4d4d4d',bg = '#4d4d4d',borderwidth = 0,fg = '#cdcdcd')
		self.op.pack(expand = 1,side = 'left',fill = 'both',padx = 4,pady = 4)
		self.log_out = Button(self.frame23,command = self.logout,text = 'LOG-OUT',width = 15,relief = 'groove',font = ('segoe ui black',10),activebackground = '#4d4d4d',bg = '#4d4d4d',borderwidth = 0,fg = '#cdcdcd')
		self.log_out.pack(expand = 1,fill = 'both',side = 'right',padx = 4,pady = 4)
		self.inp.focus_set()
		self.out['state'] = 'disabled'

	def open_file(self):
		self.editor.delete('1.0',END)
		self.text_file = filedialog.askopenfilename(initialdir = 'C:/Users/user/Desktop/Project/Saved Files',title = 'Open File',filetypes = (('Text Files','*.txt'),('Python','*.py'),('All Files','*.*')))
		if self.text_file:
			self.name = self.text_file
			self.name = self.name.replace('C:/Users/user/Desktop/','')
			self.app.title(f'{self.name} - Text Editor')
			self.text_file = open(self.text_file,'r')
			self.data = self.text_file.read()
			self.text_file.close()
			self.editor.insert(END,self.data)

	def new_file(self):
		self.editor.delete('1.0',END)
		self.app.title('New File - Text Editor')

	def save_as_file(self):
		if self.editor.get('1.0',END)!='\n':
			self.text_file = filedialog.asksaveasfilename(defaultextension = '.*',initialdir = 'C:/Users/user/Desktop/Project/Saved Files',title = 'Save As',filetypes = (('Text Files','*.txt'),('Python','*.py'),('All Files','*.*')))
			if self.text_file:
				self.name = self.text_file
				self.name = self.name.replace('C:/Users/user/Desktop/','')
				self.app.title(f'{self.name} - Text Editor')
				self.text_file = open(self.text_file,'w')
				self.text_file.write(self.editor.get('1.0',END))
				self.text_file.close()
				messagebox.askokcancel('Information','File Saved')
		else:
			messagebox.showerror('Error','No Data To Be Saved')

	def font_pick(self,event):
		self.font_fs.config(family = self.list_f.get(self.list_f.curselection()))
		self.editor.focus_set()

	def font_size_pick(self,event):
		self.font_fs.config(size = self.list_fsz.get(self.list_fsz.curselection()))
		self.editor.focus_set()

	def font_style_pick(self,event):
		self.style = self.list_fst.get(self.list_fst.curselection()).lower()
		if self.style == 'bold':
			self.font_fs.config(weight = 'bold')
			self.editor.focus_set()
		elif self.style == 'regular':
			self.font_fs.config(weight = 'normal',overstrike = 0,underline = 0,slant = 'roman')
			self.editor.focus_set()
		elif self.style == 'italic':
			self.font_fs.config(slant = 'italic')
			self.editor.focus_set()
		elif self.style == 'bold & italic':
			self.font_fs.config(slant = 'italic',weight = 'bold')
			self.editor.focus_set()
		elif self.style == 'underline':
			self.font_fs.config(underline = 1)
			self.editor.focus_set()
		elif self.style == 'strike':
			self.font_fs.config(overstrike = 1)
			self.editor.focus_set()

	def c_bg(self):
		self.my_colour = colorchooser.askcolor()
		self.editor['bg'] = self.my_colour[1]

	def c_txt(self):
		self.my_colour = colorchooser.askcolor()
		self.editor['fg'] = self.my_colour[1]

	def light(self):
		self.panel0['bg'] = '#f9b04a'
		self.editor['bg'] = '#FAEEE0'
		self.frame_e['bg'] = '#f9b04a'
		self.l0.config(bg = '#f9b04a')
		self.l0.config(fg = '#3b3838')
		self.l1.config(bg = '#f9b04a')
		self.l1.config(fg = '#3b3838')
		self.l2.config(bg = '#f9b04a')
		self.l2.config(fg = '#3b3838')
		self.list_f['bg'] = '#FAEEE0'
		self.list_fsz['bg'] = '#FAEEE0'
		self.list_fst['bg'] = '#FAEEE0'
		self.editor['insertbackground'] = '#000000'
		self.list_f['fg'] = '#000000'
		self.list_fsz['fg'] = '#000000'
		self.list_fst['fg'] = '#000000'
		self.editor['fg'] = '#000000'

	def dark(self):
		self.panel0['bg'] = '#3b3838'
		self.editor['bg'] = '#262626'
		self.editor['fg'] = '#cdcdcd'
		self.editor['insertbackground'] = '#ffffff'
		self.frame_e['bg'] = '#3b3838'
		self.l0.config(bg = '#404040')
		self.l0.config(fg = '#cdcdcd')
		self.l1.config(bg = '#404040')
		self.l1.config(fg = '#cdcdcd')
		self.l2.config(bg = '#404040')
		self.l2.config(fg = '#cdcdcd')
		self.list_f['bg'] = '#595757'
		self.list_fsz['bg'] = '#595757'
		self.list_fst['bg'] = '#595757'
		self.list_f['fg'] = '#cdcdcd'
		self.list_fsz['fg'] = '#cdcdcd'
		self.list_fst['fg'] = '#cdcdcd'

	def logout_emp(self):
		self.frame3.destroy()
		self.Frame1()

	def Frame3(self):
		self.frame3 = Frame(self.app)
		self.frame3.pack(fill = 'both',expand = 1)
		self.menu_bar = Menu(self.frame3)
		self.file = Menu(self.menu_bar,tearoff = 0)
		self.file.add_command(label = 'Save As File',command = self.save_as_file)
		self.file.add_command(label = 'New File',command = self.new_file)
		self.file.add_command(label = 'Open',command = self.open_file)
		self.file.add_command(label = 'Log-Out',command = self.logout_emp)
		self.menu_bar.add_cascade(label = 'File',menu = self.file)

		self.cp = Menu(self.menu_bar,tearoff = 0)
		self.cp.add_command(label = 'Background Colour',command = self.c_bg)
		self.cp.add_command(label = 'Font Colour',command = self.c_txt)
		self.cp.add_command(label = 'Reset',command = self.light)
		self.menu_bar.add_cascade(label = 'Edit Colour',menu = self.cp)

		self.ts = Menu(self.menu_bar,tearoff = 0)
		self.ts.add_command(label = 'Light',command = self.light)
		self.ts.add_command(label = 'Dark',command = self.dark)
		self.menu_bar.add_cascade(label = 'Theme',menu = self.ts)

		self.app.config(menu=self.menu_bar)

		self.panel0 = PanedWindow(self.frame3,bg = '#f9b04a',sashpad = 5,sashrelief = 'groove',sashwidth = 5,relief = 'groove')
		self.panel0.pack(side = 'left',fill = 'both',expand = 1)

		self.font_fs = font.Font(family = 'Helvetica',size = 10)

		self.editor = ScrolledText(self.panel0,font = self.font_fs,width = 170,bd = 5,relief = 'groove',bg = '#FAEEE0')
		self.panel0.add(self.editor)
		self.editor.focus_set()
		
		self.frame_e = Frame(self.panel0,bg = '#f9b04a',width = 5)
		self.panel0.add(self.frame_e)
		
		self.l0 = Label(self.frame_e,text = 'Font',font = ('segoe ui black',15),bg = '#f9b04a',fg = '#3b3838')
		self.l0.pack(side = 'top',fill = 'x',expand = 1)
		self.list_f = Listbox(self.frame_e,selectmode = SINGLE,relief = 'groove',bd = 5,bg = '#FAEEE0')
		self.list_f.pack(side = 'top',fill = 'both',expand = 1)
		self.l1 = Label(self.frame_e,text = 'Font Size',font = ('segoe ui black',15),bg = '#f9b04a',fg = '#3b3838')
		self.l1.pack(side = 'top',fill = 'x',expand = 1)
		self.list_fsz = Listbox(self.frame_e,selectmode = SINGLE,relief = 'groove',bd = 5,bg = '#FAEEE0')
		self.list_fsz.pack(side = 'top',fill = 'both',expand = 1)
		self.l2 = Label(self.frame_e,text = 'Font Style',font = ('segoe ui black',15),bg = '#f9b04a',fg = '#3b3838')
		self.l2.pack(side = 'top',fill = 'x',expand = 1)
		self.list_fst = Listbox(self.frame_e,selectmode = SINGLE,relief = 'groove',bd = 5,bg = '#FAEEE0')
		self.list_fst.pack(side = 'bottom',fill = 'both',expand = 1)
		for i in font.families():
			self.list_f.insert('end',i)
		for j in range(8,73,2):
			self.list_fsz.insert('end',j)
		self.fs = ['Regular','Bold','Italic','Bold & Italic','Underline','Strike']
		for a in self.fs:
			self.list_fst.insert('end',a)

		self.list_f.bind('<ButtonRelease-1>',self.font_pick)
		self.list_fsz.bind('<ButtonRelease-1>',self.font_size_pick)
		self.list_fst.bind('<ButtonRelease-1>',self.font_style_pick)
		
MyApp = Application()
MyApp.Frame1()
MyApp.app.mainloop()
