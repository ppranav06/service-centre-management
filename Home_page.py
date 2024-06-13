import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import *
from tkinter import ttk
import re

root1=tk.Tk()
root1.geometry("1000x500")
root1.title("Vehicle Service Centre")
options_frame=tk.Frame(root1,bg="#A89DC7")

main_frame = tk.Frame(root1, bg="#A89DC7")
main_frame.pack(fill="both", expand=True)



def validate_vehicle_number(vehicle_number):
    # Regular expression to match Indian vehicle number format
    pattern = r'^[A-Z]{2}[0-9]{1,2}[A-Z]{2}[0-9]{1,4}$'

    # Compile the regex pattern
    regex = re.compile(pattern)

    # Check if the provided vehicle number matches the pattern
    if not regex.match(vehicle_number):
        return False
    
    # Additional validation for the state code (first two characters)
    state_codes = ['AP', 'AR', 'AS', 'BR', 'CG', 'GA', 'GJ', 'HR', 'HP', 'JH', 'KA', 'KL', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OD', 'PB', 'RJ', 'SK', 'TN', 'TS', 'TR', 'UP', 'UK', 'WB', 'AN', 'CH', 'DH', 'DD', 'DL', 'LD', 'PY']

    state_code = vehicle_number[:2]
    if state_code not in state_codes:
        return False

    return True

# Function to validate customer name
def validate_customer_name(customer_name):
    # Regular expression to match alphabetic characters and spaces
    pattern = r'^[a-zA-Z\s]+$'

    # Compile the regex pattern
    regex = re.compile(pattern)

    # Check if the provided customer name matches the pattern
    if not regex.match(customer_name):
        return False

    return True

def job_page():
    root = tk.Tk()
    root.title("Job Card")

    spare_parts = ["Spark plugs", "Air filter", "Oil filter", "Brake pads", "Chain sprockets", "Engine oil", "Clutch cable", "Brake cable", "Tyres", "Battery"]
    service_types = ["Ignition system service", "Tune-up", "Engine service", "Brake replacement", "Transmission service", "Brake service", "Tyre rotation", "Electrical system check"]
    spare_part_rates = {"Spark plugs": 200, "Air filter": 300, "Oil filter": 150, "Brake pads": 500, "Chain sprockets": 800, "Engine oil": 400,
                        "Clutch cable": 100, "Brake cable": 120, "Tyres": 2000, "Battery": 1500}
    service_type_rates = {"Ignition system service": 500, "Tune-up": 600, "Engine service": 1000, "Brake replacement": 800, "Transmission service": 1200, "Brake service": 700,
                          "Tyre rotation": 300, "Electrical system check": 400}

    # Inventory management
    spare_parts_inventory = {part: 20 for part in spare_parts}  # Example initial inventory
    original_inventory = spare_parts_inventory.copy()  # Original inventory snapshot

    job_card_frame = ttk.Frame(root)
    job_card_frame.pack(padx=10, pady=10)

    def calculate_rate():
        total = 0
        for row in range(len(spare_part_combos)):
            part = spare_part_combos[row].get().split(' - ')[0]
            quantity = quantity_entries[row].get()
            service = service_type_combos[row].get()
            if part and service and quantity.isdigit():
                total += spare_part_rates.get(part, 0) * int(quantity) + service_type_rates.get(service, 0)
        total_label.config(text=f"Total: {total}")

    def update_combobox_values():
        for combo in spare_part_combos:
            current_value = combo.get()
            inventory_labels = [f"{item} - {spare_parts_inventory[item]}" for item in spare_parts]
            combo['values'] = inventory_labels
            combo.set(current_value)

    table_canvas = tk.Canvas(job_card_frame)
    table_canvas.pack(side=tk.LEFT)

    scrollbar = ttk.Scrollbar(job_card_frame, orient="vertical", command=table_canvas.yview)
    scrollbar.pack(side=tk.LEFT, fill=tk.Y)

    table_canvas.configure(yscrollcommand=scrollbar.set)

    table_frame = ttk.Frame(table_canvas)
    table_canvas.create_window((0, 0), window=table_frame, anchor="nw")

    spare_part_combos = []
    service_type_combos = []
    quantity_entries = []

    def delayed_filter(event, combo, values):
        def filter_combobox():
            value = combo.get().split(' - ')[0].lower()
            data = [item for item in values if value in item.lower()]
            if values == spare_parts:
                inventory_labels = [f"{item} - {spare_parts_inventory[item]}" for item in data]
                combo['values'] = inventory_labels
            else:
                combo['values'] = data
            combo.event_generate('<Down>')
            combo.icursor(tk.END)
            combo.selection_clear()

        if hasattr(combo, 'after_id'):
            combo.after_cancel(combo.after_id)
        combo.after_id = combo.after(1000, filter_combobox)

    def add_row():
        row = len(spare_part_combos)

        spare_part_combo = ttk.Combobox(table_frame)
        service_type_combo = ttk.Combobox(table_frame)
        quantity_entry = ttk.Entry(table_frame, width=5)

        spare_part_combo.grid(row=row, column=0, padx=5, pady=5)
        quantity_entry.grid(row=row, column=1, padx=5, pady=5)
        service_type_combo.grid(row=row, column=2, padx=5, pady=5)

        spare_part_combos.append(spare_part_combo)
        service_type_combos.append(service_type_combo)
        quantity_entries.append(quantity_entry)

        update_combobox_values()
        service_type_combo['values'] = service_types

        def update_inventory(event):
            selected_part = spare_part_combo.get().split(' - ')[0]
            quantity = quantity_entry.get()
            if selected_part in spare_parts_inventory and quantity.isdigit():
                total_quantity_needed = sum(int(q.get()) for q in quantity_entries if q.get().isdigit() and spare_part_combos[quantity_entries.index(q)].get().split(' - ')[0] == selected_part)
                new_quantity = original_inventory[selected_part] - total_quantity_needed
                if new_quantity >= 0:
                    spare_parts_inventory[selected_part] = new_quantity
                    update_combobox_values()
                    calculate_rate()
                else:
                    messagebox.showerror("Error", f"Not enough {selected_part} in inventory.")
                    spare_part_combo.set('')
                    quantity_entry.delete(0, tk.END)

        spare_part_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, spare_part_combo, spare_parts))
        service_type_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, service_type_combo, service_types))

        spare_part_combo.bind("<<ComboboxSelected>>", update_inventory)
        service_type_combo.bind("<<ComboboxSelected>>", lambda event: calculate_rate())
        quantity_entry.bind("<FocusOut>", update_inventory)

    for _ in range(10):
        add_row()

    total_label = ttk.Label(job_card_frame, text="Total: 0")
    total_label.pack(pady=5)

    def generate_bill():
        vehicle_number = vehicle_entry.get().strip()
        customer_name = customer_entry.get().strip()

        # Validate vehicle number and customer name
        if not validate_vehicle_number(vehicle_number):
            messagebox.showerror("Error", "Invalid vehicle number format. Please enter in the format: TN30BX1234")
            return
        
        if not validate_customer_name(customer_name):
            messagebox.showerror("Error", "Invalid customer name. Please use only alphabets and spaces.")
            return

        bill_text = f"Bill for {customer_name} (Vehicle No: {vehicle_number}):\n\n"
        for row in range(len(spare_part_combos)):
            part = spare_part_combos[row].get().split(' - ')[0]
            quantity = quantity_entries[row].get()
            service = service_type_combos[row].get()
            if part and service and quantity.isdigit():
                rate = spare_part_rates.get(part, 0) * int(quantity) + service_type_rates.get(service, 0)
                bill_text += f"{part} x {quantity} - {service}: {rate}\n"
        bill_text += f"\nTotal: {total_label.cget('text').split(': ')[1]}"
        bill_label.config(text=bill_text)

    def clear_fields():
        vehicle_entry.delete(0, tk.END)
        customer_entry.delete(0, tk.END)
        for combo in spare_part_combos:
            combo.set("")
        for entry in quantity_entries:
            entry.delete(0, tk.END)
        for combo1 in service_type_combos:
            combo1.set("")
        total_label.config(text="Total: 0")
        bill_label.config(text="")

    # Input fields for customer name and vehicle number
    input_frame = ttk.Frame(root)
    input_frame.pack(padx=10, pady=10)

    ttk.Label(input_frame, text="Vehicle Number:").grid(row=0, column=0, padx=5, pady=5)
    vehicle_entry = ttk.Entry(input_frame)
    vehicle_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(input_frame, text="Customer Name:").grid(row=1, column=0, padx=5, pady=5)
    customer_entry = ttk.Entry(input_frame)
    customer_entry.grid(row=1, column=1, padx=5, pady=5)

    # Buttons for generating bill, clearing fields, and saving bill
    generate_button = ttk.Button(input_frame, text="Generate Bill", command=generate_bill)
    generate_button.grid(row=2, column=0, pady=10)

    clear_button = ttk.Button(input_frame, text="Clear Fields", command=clear_fields)
    clear_button.grid(row=2, column=1, pady=10)

	# Bill display label
    bill_label = ttk.Label(root, text="", justify="left")
    bill_label.pack(pady=10)

	# Update the scroll region
    def update_scroll_region(event):
        table_canvas.configure(scrollregion=table_canvas.bbox("all"))

    table_frame.bind("<Configure>", update_scroll_region)

    root.mainloop()

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

#def assign_page():
	# assign_frame=tk.Frame(main_frame)
	# lb=tk.Label(assign_frame,text="ASSIGNED",font=("Bold",30))
	# lb.pack()
	# assign_frame.pack(pady=20)
# Example data: list of tuples (job_id, mechanic, task, status)
assigned_jobs = [
    (1, "Mechanic 1", "Engine oil change", "Assigned"),
    (2, "Mechanic 2", "Brake replacement", "Assigned"),
    (3, "Mechanic 3", "Tyre rotation", "In Progress"),
    (4, "Mechanic 4", "Clutch cable replacement", "Assigned"),
	(5,"Mechanic 5","Tyre replacemnt","Assigned")
]

def assign_page():
    assign_frame = tk.Frame(main_frame)
    lb = tk.Label(assign_frame, text="Assigned Work", font=("Ariel", 15))
    lb.pack()

    tree = ttk.Treeview(assign_frame)

    tree['columns'] = ("Job ID", "Mechanic", "Task", "Status")

    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Job ID", anchor=tk.W, width=80)
    tree.column("Mechanic", anchor=tk.W, width=120)
    tree.column("Task", anchor=tk.W, width=180)
    tree.column("Status", anchor=tk.W, width=100)

    tree.heading("#0", text="", anchor=tk.W) 
    tree.heading("Job ID", text="Job ID", anchor=tk.W)
    tree.heading("Mechanic", text="Mechanic", anchor=tk.W)
    tree.heading("Task", text="Task", anchor=tk.W)
    tree.heading("Status", text="Status", anchor=tk.W)

    for job in assigned_jobs:
        tree.insert("", tk.END, values=job)

    tree.pack(expand=True, fill='both')

    assign_frame.pack(pady=20)

def unassign_page():
	unassign_frame=tk.Frame(main_frame)
	lb=tk.Label(unassign_frame,text="Unassigned Work",font=("Ariel",15))
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