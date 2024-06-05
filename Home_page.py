import tkinter as tk


from tkinter import messagebox
import sqlite3
from tkinter import *
from tkinter import ttk

root=tk.Tk()
root.geometry("1000x500")
root.title("Vehicle Service Centre")
options_frame=tk.Frame(root,bg="#A89DC7")

main_frame = tk.Frame(root, bg="#A89DC7")
main_frame.pack(fill="both", expand=True)

def job_page():

	def on_select(event):
		selected_value = com.get()
		print(f"Selected: {selected_value}")

	def on_select1(event):
		selected_value = com1.get()
		print(f"Selected: {selected_value}")

	def on_select2(event):
		selected_value = com2.get()
		print(f"Selected: {selected_value}")

	job_frame=tk.Frame(main_frame)

	label_vehicle_service=tk.Label(main_frame,text="service type",font=("Ariel",12),bg="#ccc")
	label_vehicle_service.place(width=100,height=20,x=25,y=200)

	var=StringVar()
	com=ttk.Combobox(main_frame,width=27,textvariable=var)
	com["values"]=("engine oil", "tyre", "others")
	com.current()
	com.bind("<<ComboboxSelected>>", on_select)
	#com.place(x=150,y=200)
	com.place(x=150,y=200)

	label_vehicle_no=tk.Label(main_frame,text="vehicle number",font=("Ariel",12),bg="#ccc")
	label_vehicle_no.place(width=120,height=20,x=25,y=250)

	var1=StringVar()
	com1=ttk.Combobox(main_frame,width=27)
	com1["values"]=("123","345","678","367","900")
	com1.current()
	com1.bind("<<ComboboxSelected>>", on_select1)

	com1.place(x=150,y=250)

	label_others=tk.Label(main_frame,text="others",font=("Ariel",12),bg="#ccc")
	label_others.place(width=75,height=20,x=25,y=300)

	var2=StringVar()
	com2=ttk.Combobox(main_frame,width=27)
	com2["values"]=("others 1","others2","others3")
	com2.current()
	com2.bind("<<ComboboxSelected>>", on_select2)
	com2.place(x=150,y=300)
	job_frame=tk.Frame(main_frame)
	lb=tk.Label(job_frame,text="JOB CARD\n\n",font=("Bold",30))
	lb.pack()
	job_frame.pack(pady=20)

def cus_page():
	"""Page for entry of customer data"""

	cus_frame=tk.Frame(main_frame)
	lb=tk.Label(cus_frame,text="CUSTOMER CARD",font=("Bold",30))
	
	
	db = sqlite3.connect('service-centre.db')
	c = db.cursor()
	
	c.execute('''CREATE TABLE IF NOT EXISTS customers(vehicle_no varchar(10) PRIMARY KEY, 
			  name TEXT NOT NULL, address TEXT NOT NULL, mail_id VARCHAR, phone_no integer NOT NULL, phone_no_alt integer);''')
	db.commit()

	font = ("Arial", 12)
	label_color = "#ccc"
	entry_color = "#ccc"
	
	vehicle_label = tk.Label(main_frame, text="Vehicle Number:",font=font,bg=label_color)
	vehicle_label.place(x=200, y=100)
	vehicle_entry = tk.Entry(main_frame, width=30,font=font,bg=entry_color)
	vehicle_entry.place(x=350, y=100)

	name_label = tk.Label(main_frame, text="Name:",font=font,bg=label_color)
	name_label.place(x=200, y=140)
	name_entry = tk.Entry(main_frame, width=30,font=font,bg=entry_color)
	name_entry.place(x=350, y=140)

	address_label = tk.Label(main_frame, text="Address:",font=font,bg=label_color)
	address_label.place(x=200, y=180)
	address_entry1 = tk.Entry(main_frame, width=30, font=font, bg=entry_color)
	address_entry1.place(x=350, y=180)
	address_entry2 = tk.Entry(main_frame, width=30, font=font, bg=entry_color)
	address_entry2.place(x=350, y=220)
	address_entry3 = tk.Entry(main_frame, width=30, font=font, bg=entry_color)
	address_entry3.place(x=350, y=260)

	mail_label = tk.Label(main_frame, text="Mail ID:",font=font,bg=label_color)
	mail_label.place(x=200, y=300)
	mail_entry = tk.Entry(main_frame, width=30,font=font,bg=entry_color)
	mail_entry.place(x=350, y=300)

	phone_no_label = tk.Label(main_frame, text="Whatsapp Number:",font=font,bg=label_color)
	phone_no_label.place(x=200, y=340)
	phone_no_entry = tk.Entry(main_frame, width=30,font=font,bg=entry_color)
	phone_no_entry.place(x=350, y=340)

	alternate_phone_label = tk.Label(main_frame, text="Alternate Number:",font=font,bg=label_color)
	alternate_phone_label.place(x=200, y=380)
	alternate_phone_entry = tk.Entry(main_frame, width=30,font=font,bg=entry_color)
	alternate_phone_entry.place(x=350, y=380)
	def add_customer():
		vehicle_number = vehicle_entry.get()
		name = name_entry.get()
		address = f"{address_entry1.get()} {address_entry2.get()} {address_entry3.get()}"
		mail_id = mail_entry.get()
		phone_no = phone_no_entry.get()
		alternate = alternate_phone_entry.get()
		
		c.execute("INSERT INTO customers (vehicle_no, name, address, mail_id, phone_no, phone_no_alt) VALUES (?, ?, ?, ?, ?, ?)",
			 (vehicle_number, name, address, mail_id, phone_no, alternate))
		db.commit()
		
		print("Customer added successfully!")
		messagebox.showinfo("Message", "Customer added successfully!")
	 
	add_button = tk.Button(main_frame, text="Add Customer",font=font,fg="#000000",command=add_customer)
	add_button.place(x=350, y=440)
	lb.pack()
	cus_frame.pack(pady=20)
	
   
def assign_page():
	assign_frame=tk.Frame(main_frame)
	lb=tk.Label(assign_frame,text="ASSIGNED",font=("Bold",30))
	lb.pack()
	assign_frame.pack(pady=20)

def unassign_page():
	unassign_frame=tk.Frame(main_frame)
	lb=tk.Label(unassign_frame,text="UNASSIGNED",font=("Bold",30))
	lb.pack()
	unassign_frame.pack(pady=20)

def employee_page():
	employee_frame=tk.Frame(main_frame)
	lb=tk.Label(employee_frame,text="EMPLOYEE",font=("Bold",30))
	lb.pack()
	employee_frame.pack(pady=20)

def hide_indicators():
	job_indicate.config(bg="#c3c3c3")
	cus_indicate.config(bg="#c3c3c3")
	assign_indicate.config(bg="#c3c3c3")
	unassigned_indicate.config(bg="#c3c3c3")
	employee_indicate.config(bg="#c3c3c3")
def delete_pages():
	for frame in main_frame.winfo_children():
		frame.destroy()
def indicate(lb,page):
	hide_indicators()
	lb.config(bg="#0B0707")
	delete_pages()
	page()

job_btn=tk.Button(options_frame,text="Job Card",font=("Bold",15),fg="#000000",bd=0,bg="#c3c3c3",command=lambda: indicate(job_indicate,job_page))
job_btn.place(x=10,y=350)

job_indicate=tk.Label(options_frame,text="",bg="#c3c3c3")
job_indicate.place(x=3,y=350,width=5,height=40)

cus_btn=tk.Button(options_frame,text="CustomerCard",font=("Bold",15),fg="#000000",bd=0,bg="#c3c3c3",command=lambda: indicate(cus_indicate,cus_page))
cus_btn.place(x=10,y=400)

cus_indicate=tk.Label(options_frame,text="",bg="#c3c3c3")
cus_indicate.place(x=3,y=400,width=5,height=40)

assigned_btn=tk.Button(options_frame,text="Assigned",font=("Bold",15),fg="#000000",bd=0,bg="#c3c3c3",command=lambda: indicate(assign_indicate,assign_page))
assigned_btn.place(x=10,y=50)

assign_indicate=tk.Label(options_frame,text="",bg="#c3c3c3")
assign_indicate.place(x=3,y=50,width=5,height=40)

employee_btn=tk.Button(options_frame,text= "Employee",font=("Bold",15),fg="#000000",bd=0,bg="#c3c3c3",command=lambda: indicate(employee_indicate,employee_page))
employee_btn.place(x=10,y=150)

employee_indicate=tk.Label(options_frame,text="",bg="#c3c3c3")
employee_indicate.place(x=3,y=150,width=5,height=40)

unassigned_btn=tk.Button(options_frame,text="Unassigned",font=("Bold",15),fg="#000000",bd=0,bg="#c3c3c3",command=lambda:indicate(unassigned_indicate,unassign_page))
unassigned_btn.place(x=10,y=100)

unassigned_indicate=tk.Label(options_frame,text="",bg="#c3c3c3")
unassigned_indicate.place(x=3,y=100,width=5,height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=150,height=500)

main_frame=tk.Frame(root,highlightbackground="black",highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=1000,height=500)

root.mainloop()
