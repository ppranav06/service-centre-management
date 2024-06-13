#job card page with intial comboboxes 
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


#job card with new comboboxes with not so user friendly search
def job_page():
	root = tk.Tk()
	root.title("Job Card")

	spare_parts = ["Spark plugs","Air filter","Oil filter","Brake pads","Chain sprockets","Engine oil","Clutch cable","Brake cable","Tyres","Battery"]
	service_types =  ["Ignition system service", "Tune-up", "Engine service", "Brake replacement", "Transmission service", "Engine service", "Brake service", "Tyre rotation", "Electrical system check"]
	spare_part_rates = {"Spark plugs": 200,"Air filter": 300,"Oil filter": 150,"Brake pads": 500,"Chain sprockets": 800,"Engine oil": 400,
    "Clutch cable": 100,"Brake cable": 120,"Tyres": 2000,"Battery": 1500}
	service_type_rates = {"Ignition system service": 500,"Tune-up": 600,"Engine service": 1000,"Brake replacement": 800,"Transmission service": 1200,"Brake service": 700,
    "Tyre rotation": 300,"Electrical system check": 400}

	job_card_frame = ttk.Frame(root)
	job_card_frame.pack(padx=10, pady=10)

	def calculate_rate():
		total = 0
		for row in range(len(spare_part_combos)):
			part = spare_part_combos[row].get()
			service = service_type_combos[row].get()
			if part and service:
				total += spare_part_rates[part] + service_type_rates[service]
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
		
		spare_part_combo = ttk.Combobox(table_frame, values=spare_parts, state="readonly")
		service_type_combo = ttk.Combobox(table_frame, values=service_types, state="readonly")
		
		spare_part_combo.grid(row=row, column=0, padx=5, pady=5)
		service_type_combo.grid(row=row, column=1, padx=5, pady=5)
		
		spare_part_combos.append(spare_part_combo)
		service_type_combos.append(service_type_combo)
		
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

	# Vehicle number and customer name input
	input_frame = ttk.Frame(root)
	input_frame.pack(padx=10, pady=10)

	ttk.Label(input_frame, text="Vehicle Number:").grid(row=0, column=0, padx=5, pady=5)
	vehicle_entry = ttk.Entry(input_frame)
	vehicle_entry.grid(row=0, column=1, padx=5, pady=5)

	ttk.Label(input_frame, text="Customer Name:").grid(row=1, column=0, padx=5, pady=5)
	customer_entry = ttk.Entry(input_frame)
	customer_entry.grid(row=1, column=1, padx=5, pady=5)

	# Generate Bill Button
	generate_button = ttk.Button(input_frame, text="Generate Bill", command=generate_bill)
	generate_button.grid(row=2, columnspan=2, pady=10)

	# Bill display label
	bill_label = ttk.Label(root, text="", justify="left")
	bill_label.pack(pady=10)

	# Update the scroll region
	def update_scroll_region(event):
		table_canvas.configure(scrollregion=table_canvas.bbox("all"))

	table_frame.bind("<Configure>", update_scroll_region)

	root.mainloop()
	
#3rd update of job card
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
    def delayed_filter(event, combo, values):
        def filter_combobox():
            value = combo.get().lower()
            data = [item for item in values if value in item.lower()]
            combo['values'] = data
            combo.event_generate('<Down>')
            combo.icursor(tk.END)
            combo.selection_clear()
        if hasattr(combo, 'after_id'):
                combo.after_cancel(combo.after_id)  # Cancel previous scheduled call if any
        combo.after_id = combo.after(300, filter_combobox)
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
        spare_part_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, spare_part_combo, spare_parts))
        service_type_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, service_type_combo, service_types))

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