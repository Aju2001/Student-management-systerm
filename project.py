# python project.
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *
import socket
import bs4 #library for pulling data out of html and xml
import requests
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk,Image


# code for taking the temperature of the city
try:
	socket.create_connection(("www.google.com",80))
	print("u r connected")
	res = requests.get("http://ipinfo.io")
	print(res)
	data = res.json()
	print(data)
	city = data['city']
	print("your location is ",city)
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q="+ city
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	api_address = a1 + a2 + a3
	res1 = requests.get(api_address)
	data = res1.json()
	main = data['main']
	temp = main['temp']
	print("Temp = ",temp)
	temp1 = str(temp)
	print(type(temp1))
	city_temp = city+" "+temp1
	print(city+" "+temp1)	
except OSError:
	print("check network")

# code for printing the quote
res2 = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
print(res2)
soup = bs4.BeautifulSoup(res2.text,'lxml')
quote = soup.find('img',{"class":"p-qotd" })
print(quote)
print("hello")
msg = quote['alt'].strip()
print(msg)

root = Tk()
root.title("S.M.S")
root.geometry("1300x600+100+100")
root.configure(background="LightBlue1")


def f1():
	root.withdraw()
	vist.deiconify()

# function for view button on root
def f2():
	root.withdraw()
	view.deiconify()
	stViewData.delete(1.0,END)
	con = None
	try:
		con = connect("system/abc123")
		cursor = con.cursor()
		sql = "select rno, name, marks from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		for d in data:
			msg = msg + "rno = "+ str(d[0]) + "  name = "+str(d[1]) + "  marks = "+ str(d[2]) + "\n"
		stViewData.insert(INSERT, msg)
	except DatabaseError as e:
		messagebox.showerror("galat kiya ",e)
	finally:
		if con is not None:
			con.close()


def f3():
	root.withdraw()
	update.deiconify()

# function for save button on add window 
def f4():
	con = None
	try:
		con = connect("system/abc123")
		r=adRol.get()
		if r == "":
			raise Exception("you entered nothing in roll no")
		if r.isalpha():
			raise Exception("Roll no can not be characters")
		rno = int(r)
		if rno == 0 or rno < 0:
			raise Exception("Invalid roll no")
		name = adName.get()
		if len(name) <=1 or name.isdigit():
			raise Exception("Invalid name")
		print(name)
		if name == "":
			raise Exception("You entered nothing in name")
		m=adMarks.get()
		if m == "":
			raise Exception("You entered nothing in marks")
		if m.isalpha():
			raise Exception("Marks can not be characters")
		marks = int(m)	
		if marks > 100:
			raise exception("marks can not be greater than 100")		
		print(m,type(m))

	except ValueError as e:
		messagebox.showerror("Error"," you entered something wrong")
	except DatabaseError as e:
		messagebox.showerror("Issue"," Something went wrong")
		con.rollback() 

			
	except Exception:
			if r == "":
				messagebox.showerror("Invalid marks"," You  entered nothing in Roll no")
			elif r.isalpha():
				messagebox.showerror("Invalid marks"," Rollno can not be characters")
				adRol.delete(0,END)
			elif rno==0 or rno < 0:
				messagebox.showerror("Invalid roll no","rno is not a vaild rollno")
				adRol.delete(0,END)
			elif name == "":
				messagebox.showerror("Invalid name"," You entered nothing in name")
			elif len(name) <=1 or name.isdigit():
				messagebox.showerror("Invalid Name","name is not a valid name")
				adName.delete(0,END)
			elif m == "":
				messagebox.showerror("Invalid marks"," You entered nothing in marks")
			elif m.isalpha():
				messagebox.showerror("Invalid marks","marks can not be characters")
				adMarks.delete(0,END)
			elif marks>100:
				messagebox.showerror("Invalid marks","marks can not be greater than 100")
				adMarks.delete(0,END)
			else:
				messagebox.showerror("Error","Bad entry")
				adRol.delete(0,END)
				adName.delete(0,END)
				adMarks.delete(0,END)
				
	else:	
		args=(rno, name, marks)
		cursor = con.cursor()
		sql = "insert into student values('%d','%s','%d')"
		cursor.execute(sql % args)
		messagebox.showinfo("Add"," Value added")
		adRol.delete(0,END)
		adName.delete(0,END)
		adMarks.delete(0,END)		
		con.commit()
		print(cursor.rowcount, "records inserted")
	finally:
		if con is not None:
			con.close()
		print("disconnected")

# function for opening delete window 
def f5():
	root.withdraw()
	delete.deiconify()

# function for save button on delete window for deleting the record from the table 
def f7():	
	con = None
	try:
		con = connect("system/abc123")
		print("connected")
		r=delRno.get()
		rno1 = int(r)
		if rno1 == "":
			raise Exception("You entered nothing in rollno")
		if rno1 == 0 or rno1 <=0:
			raise Exception("you entered invalid rollno")
		rno1 = int(r)
	except ValueError as e:
		messagebox.showerror("Invalid roll no"," You entered something wrong in rollno")
		con.rollback()
	except DatabaseError as e:
		print("issue ",e)
		con.rollback() 
	except Exception:
		if rno1 == "":
			messagebox.showerror("Invalid roll no"," You entered nothing in roll no")
		if rno1 == 0 or r <=0:
			messagebox.showerror("Invalid roll no"," You entered invalid rollno") 
	else:
		args=(rno1)
		cursor = con.cursor()
		sql = "DELETE from student WHERE rno=('%d')"
		cursor.execute(sql % args )
		messagebox.showinfo("delete","Value deleted")
		delRno.delete(0,END)
		con.commit()

	finally:
		if con is not None:
			con.close()
		print("disconnected")

# for back button on delete window
def f8():
	delete.withdraw()
	root.deiconify()

# for back button on view window
def f9():
	view.withdraw()
	root.deiconify()

# for save button on update window
def f10():
	con = None
	try:
		con = connect("system/abc123")
		print("connected")
		r=entAddRno.get()
		if r == "":
			raise Exception("you entered nothing in roll no")
		if r.isalpha():
			raise Exception("Roll  no can not be characters")
		rno1 = int(r)
		name1 = entName.get()
		if name1 == "":
			raise Exception("you entered nothing in name")
		if len(name1) <=1 or name1.isdigit():
			raise Exception("Invalid name")
		print(name1)
		m=entMarks.get()
		print("Hello guys")
		if m == "":
			raise Exception("you entered nothing in marks")
		if m.isalpha():
			raise Exception("Marks can not be characters")
		if m.isdigit():
			marks1 = int(m)
		else:
			raise Exception("you entered something wrong in marks")
		if marks1 > 100:
			raise Exception("Marks can not be greater than 100")
	except ValueError as e:
		messagebox.showerror("Error"," You entered something wrong ")
		con.rollback()
	except DatabaseError as e:
		messagebox.showerror("Issue","Something went wrong")
		con.rollback()

	except Exception:
			if r == "":
				messagebox.showerror("Invalid roll no"," You entered nothing in roll no")
			elif r.isalpha():
				messagebox.showerror("Invalid Rollno"," Rollno can not be characters")
				entAddRno.delete(0,END)
			elif rno1.isdigit():
				rno1 = int(r)
			elif rno1==0 or rno1 < 0:
				messagebox.showerror("Invalid roll no","rno is not a vaild rollno")
				entAddRno.delete(0,END)
			else:
				messagebox.showerror("Error","You entered something wrong")
			if name1 == "":
				messagebox.showerror("Invalid marks"," You entered nothing in name")
			elif len(name1) <=1 or name1.isdigit():
				messagebox.showerror("Invalid Name","name is not a valid name")
				entName.delete(0,END)
			else:
				messagebox.showerror("Error","Bad entry")

			if m == "":
				messagebox.showerror("Invalid marks","You entered nothing in marks ")

			elif m.isalpha():
				messagebox.showerror("Invalid marks","marks can not be characters")
				entMarks.delete(0,END)
			elif marks1>100:
				messagebox.showerror("Invalid marks","marks can not be greater than 100")
				entMarks.delete(0,END)
			else:
				messagebox.showerror("Error","Bad entry")
				entAddRno.delete(0,END)
				entName.delete(0,END)
				entMarks.delete(0,END)
	else:
		cursor = con.cursor()
		sql_up = "update student set name = '%s', marks = '%d' where rno = '%d'"
		print("hello")
		args=(name1, marks1, rno1)
		print("hey")
		cursor.execute(sql_up % args )
		messagebox.showinfo("update"," value updated")
		entAddRno.delete(0,END)
		entName.delete(0,END)
		entMarks.delete(0,END)
		con.commit()
		print("record updated") 
	finally:
		if con is not None:
			con.close()
		print("disconnected")

# for back window on update window
def f11():
	update.withdraw()
	root.deiconify()

# for back button on add window
def f12():
	vist.withdraw()
	root.deiconify()

# for graph button on root
def f13():
	con = None
	try:
		con = connect("system/abc123")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		print(cursor.rowcount)
		rno = []
		name = []
		marks = []
		count = 0
		for d in data:
			marks.append(d[2]) 
		for d in data:
			name.append(d[1])
		for d in data:
			rno.append(d[0])
			count = count + 1
		x = np.arange(len(rno))
		print(x)
		if count == 0:
			raise Exception("Row count is 0")
	except Exception:
		if count == 0:
			messagebox.showerror("Table empty","there are no entries in the table")
		else:
			messagebox.showerror("something went wrong")
	except DatabaseError as e:
		messagebox.showerror("galat kiya ",e)
	else:
		plt.bar(x,marks,label="marks of student",width=0.30)
		plt.xticks(x,name)
		plt.title('Marks of students')
		plt.xlabel('Names',fontsize = 10)
		plt.ylabel('Marks',fontsize = 10)
		plt.legend()
		plt.grid()
		plt.show()
		
	finally:
		if con is not None:
			con.close()

lblname = Label(root,text = "STUDENT MANAGEMENT SYSTEM",font=("Ink Free",20,'bold'))
btnAdd = Button(root, text="Add",font=("courier",20,'bold'),command=f1)
btnView = Button(root, text="View",font=("courier",20,'bold'),command=f2)
btnUpdate = Button(root, text="Update",font=("courier",20,'bold'),command=f3)
btnDelete = Button(root, text="Delete",font=("courier",20,'bold'),command=f5)
btnGraph = Button(root, text="Graph",font=("courier",20,'bold'),command=f13)
lblcity_temp = Label(root,text = city_temp,font=("courier",20))
lblmsg = Label(root,text = msg,font=("courier",20))

lblname.place(x=840,y=30)
btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)
lblcity_temp.pack(pady=10)
lblmsg.pack(pady=10)

# making the window of add student

vist = Toplevel(root)
vist.title("Add st.")
vist.geometry("700x700+400+100")
vist.configure(background="thistle1")
vist.withdraw()

lblAddRno = Label(vist, text="Enter rollno ",font=("courier",20,'bold'))
adRol = Entry(vist,bd=10,font=("courier",30,'bold'))
lblName = Label(vist, text="Enter Name ",font=("courier",20,'bold'))
adName = Entry(vist,bd=10,font=("courier",30,'bold'))
lblMarks = Label(vist, text="Enter Marks ",font=("courier",20,'bold'))
adMarks = Entry(vist,bd=10,font=("courier",20,'bold'))

btnSave = Button(vist, text="Save",font=("courier",30,'bold'),command=f4)
btnBack = Button(vist, text="Back",font=("courier",30,'bold'),command=f12)

lblAddRno.pack(pady=10)
adRol.pack(pady=10)
lblName.pack(pady=10)
adName.pack(pady=10)
lblMarks.pack(pady=10)
adMarks.pack(pady=10)
btnSave.pack(pady=10)
btnBack.pack(pady=10)

#for making view window 
view = Toplevel(root)
view.title("View st.")
view.geometry("700x700+400+100")
view.configure(background="light goldenrod yellow")
view.withdraw()

stViewData = scrolledtext.ScrolledText(view,width=50,height=20)
btnBack = Button(view, text="Back",font=("courier",30,'bold'),command=f9)

stViewData.pack(pady=10)
btnBack.pack(pady=10)

update = Toplevel(root)
update.title("Update st.")
update.geometry("700x700+400+100")
update.configure(background="Dark SeaGreen2")
update.withdraw()


lblAddRno = Label(update, text="Enter rollno ",font=("courier",20,'bold'))
entAddRno = Entry(update,bd=10,font=("courier",30,'bold'))
lblName = Label(update, text="Enter Name ",font=("courier",20,'bold'))
entName = Entry(update,bd=10,font=("courier",30,'bold'))
lblMarks = Label(update, text="Enter Marks ",font=("courier",20,'bold'))
entMarks = Entry(update,bd=10,font=("courier",20,'bold'))

btnSave = Button(update, text="Save",font=("courier",30,'bold'),command=f10)
btnBack = Button(update, text="Back",font=("courier",30,'bold'),command=f11)

lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblName.pack(pady=10)
entName.pack(pady=10)
lblMarks.pack(pady=10)
entMarks.pack(pady=10)
btnSave.pack(pady=10)
btnBack.pack(pady=10)

delete = Toplevel(root)
delete.title("Delete st.")
delete.geometry("500x500+400+200")
delete.configure(background="Wheat2")
delete.withdraw()

lblAddRno = Label(delete, text="Enter rollno ",font=("courier",20,'bold'))
delRno = Entry(delete,bd=10,font=("courier",30,'bold'))
btnSave = Button(delete, text="Save",font=("courier",30,'bold'),command=f7)
btnBack = Button(delete, text="Back",font=("courier",30,'bold'),command=f8)

lblAddRno.pack(pady=10)
delRno.pack(pady=10)
btnSave.pack(pady=10)
btnBack.pack(pady=10)


root.mainloop()
