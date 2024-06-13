import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import *
from tkinter import ttk

root1=tk.Tk()
root1.geometry("1000x500")
root1.title("Vehicle Service Centre")
options_frame=tk.Frame(root1,bg="#A89DC7")

main_frame = tk.Frame(root1, bg="#A89DC7")
main_frame.pack(fill="both", expand=True)

def job_page():
    root = tk.Tk()
    root.title("Job Card")

    spare_parts = ["Spark plugs", "Air filter", "Oil filter", "Brake pads", "Chain sprockets", "Engine oil", "Clutch cable", "Brake cable", "Tyres", "Battery"]
    service_types = ["Ignition system service", "Tune-up", "Engine service", "Brake replacement", "Transmission service", "Brake service", "Tyre rotation", "Electrical system check"]
    spare_part_rates = {"Spark plugs": 200, "Air filter": 300, "Oil filter": 150, "Brake pads": 500, "Chain sprockets": 800, "Engine oil": 400,
                        "Clutch cable": 100, "Brake cable": 120, "Tyres": 2000, "Battery": 1500}
    service_type_rates = {"Ignition system service": 500, "Tune-up": 600, "Engine service": 1000, "Brake replacement": 800, "Transmission service": 1200, "Brake service": 700,
                          "Tyre rotation": 300, "Electrical system check": 400}

    job_card_frame = ttk.Frame(root)
    job_card_frame.pack(padx=10, pady=10)

    def calculate_rate():
        total = 0
        for row in range(len(spare_part_combos)):
            part = spare_part_combos[row].get()
            service = service_type_combos[row].get()
            if part and service:
                total += spare_part_rates.get(part, 0) + service_type_rates.get(service, 0)
        total_label.config(text=f"Total: {total}")

    table_canvas = tk.Canvas(job_card_frame)
    table_canvas.pack(side=tk.LEFT)

    scrollbar = ttk.Scrollbar(job_card_frame, orient="vertical", command=table_canvas.yview)
    scrollbar.pack(side=tk.LEFT, fill=tk.Y)

    table_canvas.configure(yscrollcommand=scrollbar.set)

    table_frame = ttk.Frame(table_canvas)
    table_canvas.create_window((0, 0), window=table_frame, anchor="nw")

    spare_part_combos = []
    service_type_combos = []

    def filter_combobox(event, combo, values):
        value = combo.get().lower()
        data = [item for item in values if value in item.lower()]
        combo['values'] = data
        combo.event_generate('<Down>')

    def add_row():
        row = len(spare_part_combos)

        spare_part_combo = ttk.Combobox(table_frame)
        spare_part_combo['values'] = spare_parts  
        service_type_combo = ttk.Combobox(table_frame)
        service_type_combo['values'] = service_types

        spare_part_combo.grid(row=row, column=0, padx=5, pady=5)
        service_type_combo.grid(row=row, column=1, padx=5, pady=5)

        spare_part_combos.append(spare_part_combo)
        service_type_combos.append(service_type_combo)

        # search option
        spare_part_combo.bind('<KeyRelease>', lambda event: filter_combobox(event, spare_part_combo, spare_parts))
        service_type_combo.bind('<KeyRelease>', lambda event: filter_combobox(event, service_type_combo, service_types))

        def update_cell(event):
            calculate_rate()

        spare_part_combo.bind("<<ComboboxSelected>>", update_cell)
        service_type_combo.bind("<<ComboboxSelected>>", update_cell)

    for _ in range(10):
        add_row()

    total_label = ttk.Label(job_card_frame, text="Total: 0")
    total_label.pack(pady=5)

    def generate_bill():
        vehicle_number = vehicle_entry.get()
        customer_name = customer_entry.get()
        bill_text = f"Bill for {customer_name} (Vehicle No: {vehicle_number}):\n\n"
        for row in range(len(spare_part_combos)):
            part = spare_part_combos[row].get()
            service = service_type_combos[row].get()
            if part and service:
                rate = spare_part_rates[part] + service_type_rates[service]
                bill_text += f"{part} - {service}: {rate}\n"
        bill_text += f"\nTotal: {total_label.cget('text').split(': ')[1]}"
        bill_label.config(text=bill_text)

    input_frame = ttk.Frame(root)
    input_frame.pack(padx=10, pady=10)

    ttk.Label(input_frame, text="Vehicle Number:").grid(row=0, column=0, padx=5, pady=5)
    vehicle_entry = ttk.Entry(input_frame)
    vehicle_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(input_frame, text="Customer Name:").grid(row=1, column=0, padx=5, pady=5)
    customer_entry = ttk.Entry(input_frame)
    customer_entry.grid(row=1, column=1, padx=5, pady=5)

    generate_button = ttk.Button(input_frame, text="Generate Bill", command=generate_bill)
    generate_button.grid(row=2, columnspan=2, pady=10)

    # Bill display label
    bill_label = ttk.Label(root, text="", justify="left")
    bill_label.pack(pady=10)

    def update_scroll_region(event):
        table_canvas.configure(scrollregion=table_canvas.bbox("all"))

    table_frame.bind("<Configure>", update_scroll_region)

    root.mainloop()


	# root = tk.Tk()
	# root.title("Job Card")

	# spare_parts = ["Spark plugs","Air filter","Oil filter","Brake pads","Chain sprockets","Engine oil","Clutch cable","Brake cable","Tyres","Battery"]
	# service_types =  ["Ignition system service", "Tune-up", "Engine service", "Brake replacement", "Transmission service", "Engine service", "Brake service", "Tyre rotation", "Electrical system check"]
	# spare_part_rates = {"Spark plugs": 200,"Air filter": 300,"Oil filter": 150,"Brake pads": 500,"Chain sprockets": 800,"Engine oil": 400,
    # "Clutch cable": 100,"Brake cable": 120,"Tyres": 2000,"Battery": 1500}
	# service_type_rates = {"Ignition system service": 500,"Tune-up": 600,"Engine service": 1000,"Brake replacement": 800,"Transmission service": 1200,"Brake service": 700,
    # "Tyre rotation": 300,"Electrical system check": 400}

	# job_card_frame = ttk.Frame(root)
	# job_card_frame.pack(padx=10, pady=10)

	# def calculate_rate():
	# 	total = 0
	# 	for row in range(len(spare_part_combos)):
	# 		part = spare_part_combos[row].get()
	# 		service = service_type_combos[row].get()
	# 		if part and service:
	# 			total += spare_part_rates[part] + service_type_rates[service]
	# 	total_label.config(text=f"Total: {total}")

	# table_canvas = tk.Canvas(job_card_frame)
	# table_canvas.pack(side=tk.LEFT)

	# scrollbar = ttk.Scrollbar(job_card_frame, orient="vertical", command=table_canvas.yview)
	# scrollbar.pack(side=tk.LEFT, fill=tk.Y)

	# table_canvas.configure(yscrollcommand=scrollbar.set)

	# table_frame = ttk.Frame(table_canvas)
	# table_canvas.create_window((0, 0), window=table_frame, anchor="nw")

	# spare_part_combos = []
	# service_type_combos = []

	# def filter_combobox(event, combo, values):
	# 		value = combo.get().lower()
	# 		data = [item for item in values if value in item.lower()]
	# 		combo['values'] = data
	# 		combo.event_generate('<Down>')

	# def add_row():
	# 	row = len(spare_part_combos)
		
	# 	spare_part_combo = ttk.Combobox(table_frame, values=spare_parts, state="readonly")
	# 	service_type_combo = ttk.Combobox(table_frame, values=service_types, state="readonly")
		
	# 	spare_part_combo.grid(row=row, column=0, padx=5, pady=5)
	# 	service_type_combo.grid(row=row, column=1, padx=5, pady=5)
		
	# 	spare_part_combos.append(spare_part_combo)
	# 	service_type_combos.append(service_type_combo)
		
	# 	spare_part_combo.bind('<KeyRelease>', lambda event: filter_combobox(event, spare_part_combo, spare_parts))
	# 	service_type_combo.bind('<KeyRelease>', lambda event: filter_combobox(event, service_type_combo, service_types))

	# 	def update_cell(event):
	# 		calculate_rate()
		
	# 	spare_part_combo.bind("<<ComboboxSelected>>", update_cell)
	# 	service_type_combo.bind("<<ComboboxSelected>>", update_cell)

	# for _ in range(10):
	# 	add_row()

	# total_label = ttk.Label(job_card_frame, text="Total: 0")
	# total_label.pack(pady=5)

	# def generate_bill():
	# 	vehicle_number = vehicle_entry.get()
	# 	customer_name = customer_entry.get()
	# 	bill_text = f"Bill for {customer_name} (Vehicle No: {vehicle_number}):\n\n"
	# 	for row in range(len(spare_part_combos)):
	# 		part = spare_part_combos[row].get()
	# 		service = service_type_combos[row].get()
	# 		if part and service:
	# 			rate = spare_part_rates[part] + service_type_rates[service]
	# 			bill_text += f"{part} - {service}: {rate}\n"
	# 	bill_text += f"\nTotal: {total_label.cget('text').split(': ')[1]}"
	# 	bill_label.config(text=bill_text)

	# # Vehicle number and customer name input
	# input_frame = ttk.Frame(root)
	# input_frame.pack(padx=10, pady=10)

	# ttk.Label(input_frame, text="Vehicle Number:").grid(row=0, column=0, padx=5, pady=5)
	# vehicle_entry = ttk.Entry(input_frame)
	# vehicle_entry.grid(row=0, column=1, padx=5, pady=5)

	# ttk.Label(input_frame, text="Customer Name:").grid(row=1, column=0, padx=5, pady=5)
	# customer_entry = ttk.Entry(input_frame)
	# customer_entry.grid(row=1, column=1, padx=5, pady=5)

	# # Generate Bill Button
	# generate_button = ttk.Button(input_frame, text="Generate Bill", command=generate_bill)
	# generate_button.grid(row=2, columnspan=2, pady=10)

	# # Bill display label
	# bill_label = ttk.Label(root, text="", justify="left")
	# bill_label.pack(pady=10)

	# # Update the scroll region
	# def update_scroll_region(event):
	# 	table_canvas.configure(scrollregion=table_canvas.bbox("all"))

	# table_frame.bind("<Configure>", update_scroll_region)

	# root.mainloop()

# '''def on_select(event):
#           selected_value = com.get()
#           print(f"Selected: {selected_value}")

#      def on_select1(event):
#           selected_value = com1.get()
#           print(f"Selected: {selected_value}")

# 	def on_select2(event):
# 		selected_value = com2.get()
# 		print(f"Selected: {selected_value}")

#      job_frame=tk.Frame(main_frame)

#      label_vehicle_service=tk.Label(main_frame,text="service type",font=("Ariel",12),bg="#ccc")
#      label_vehicle_service.place(width=100,height=20,x=25,y=200)

#      var=StringVar()
#      com=ttk.Combobox(main_frame,width=27,textvariable=var)
#      com["values"]=("engine oil", "tyre", "others")
#      com.current()
#      com.bind("<<ComboboxSelected>>", on_select)
#      #com.place(x=150,y=200)
#      com.place(x=150,y=200)

#      label_vehicle_no=tk.Label(main_frame,text="vehicle number",font=("Ariel",12),bg="#ccc")
#      label_vehicle_no.place(width=120,height=20,x=25,y=250)

#      var1=StringVar()
#      com1=ttk.Combobox(main_frame,width=27)
#      com1["values"]=("123","345","678","367","900")
#      com1.current()
#      com1.bind("<<ComboboxSelected>>", on_select1)

#      com1.place(x=150,y=250)

#      label_others=tk.Label(main_frame,text="others",font=("Ariel",12),bg="#ccc")
#      label_others.place(width=75,height=20,x=25,y=300)

#      var2=StringVar()
#      com2=ttk.Combobox(main_frame,width=27)
#      com2["values"]=("others 1","others2","others3")
#      com2.current()
#      com2.bind("<<ComboboxSelected>>", on_select2)
#      com2.place(x=150,y=300)
#      job_frame=tk.Frame(main_frame)
#      lb=tk.Label(job_frame,text="JOB CARD\n\n",font=("Bold",30))
#      lb.pack()
#      job_frame.pack(pady=20)'''

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
		
		
		
		db.commit()
		
		print("Customer added successfully!")
		messagebox.showinfo("Message", "Customer added successfully!")
		print("Vehicle Number:",vehicle_number)
		print("Name:",name)
		print("Address:",address)
		print("Mail ID:",mail_id)
		print("Whatsapp Number:",phone_no)
		print("Alternate Number:",alternate)
		clear_form()
	 
	add_button = tk.Button(main_frame, text="Add Customer",font=font,fg="#000000",command=add_customer)
	add_button.place(x=350, y=440)
	lb.pack()
	cus_frame.pack(pady=20)

	def clear_form():
		vehicle_entry.delete(0,tk.END)
		name_entry.delete(0, tk.END)
		address_entry1.delete(0,tk.END)
		address_entry2.delete(0,tk.END)
		address_entry3.delete(0,tk.END)
		mail_entry.delete(0,tk.END)
		phone_no_entry.delete(0,tk.END)
		alternate_phone_entry.delete(0,tk.END)
	 
	 
	 
   
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
	def create_employee_list(root):
		tree = ttk.Treeview(root, columns=("id", "name", "designation","department","experience"), show='headings')
		tree.column("id", anchor=tk.CENTER, width=50)
		tree.heading("id", text="ID")
		tree.column("name", anchor=tk.CENTER, width=100)
		tree.heading("name", text="Name")
		tree.column("designation", anchor=tk.CENTER, width=150)
		tree.heading("designation", text="Designation")
		tree.column("department", anchor=tk.CENTER, width=200)
		tree.heading("department", text="Department")
		tree.column("experience", anchor=tk.CENTER, width=200)
		tree.heading("experience", text="Experience")

		
		tree.pack()
		employees = [
	   {"id":"088", "name": "Pranav", "designation": "Mechanic","department":"Sales","experience":"5 Years"},
	   {"id":"085", "name": "Painthamizhan", "designation": "Customer Service","department":"Service","experience":"6 Years"},
	   {"id":"087", "name": "Poornima", "designation": "Manager","department":"Service","experience":"8 Years"},
	   {"id":"086", "name": "Pavithran", "designation": "Mechanic","department":"Sales","experience":"7 Years"}
	   
	]

            for employee in employees:
                tree.insert("", tk.END, values=(employee["id"], employee["name"], employee["designation"],employee["department"],employee["experience"]))
                tree.bind("<Double-1>", lambda event: open_employee_details(tree, event))

            def open_employee_details(tree, event):
                    item = tree.item(tree.focus())
                    employee_id = item["values"][0]
                    employees = [
        {"id":"088", "name": "Pranav", "designation": "Mechanic","department":"Service","experience":"5 Years"},
        {"id":"085", "name": "Painthamizhan", "designation": "Customer Service","department":"Sales","experience":"6 Years"},
        {"id":"087", "name": "Poornima", "designation": "Manager","department":"Sales","experience":"8 Years"},
        {"id":"086", "name": "Pavithran", "designation": "Mechanic","department":"Service","experience":"7 Years"}
        
    ]
                    
                    employee = next((e for e in employees if e["id"] == employee_id), None)
                    if employee:
                        details_window = tk.Toplevel(root)
                        details_window.title("Employee Details")
                        label = tk.Label(details_window, text=f"ID: {employee['id']}\nName: {employee['name']}\nDesignation: {employee['designation']}\nDepartment:{employee['department']}\nExperience:{employee['experience']}")
                        label.pack()
     root  = tk.Tk()
     root.title("Employee List")
     root= tk.Frame(root)
     root.pack(fill="both", expand=True)
     create_employee_list(root)

                                    

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

main_frame=tk.Frame(root1,highlightbackground="black",highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=1000,height=500)

root1.mainloop()