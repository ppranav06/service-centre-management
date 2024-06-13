import tkinter as tk
from tkinter import ttk

# def job_page():
#     root = tk.Tk()
#     root.title("Job Card")

#     spare_parts = ["Spark plugs", "Air filter", "Oil filter", "Brake pads", "Chain sprockets", "Engine oil", "Clutch cable", "Brake cable", "Tyres", "Battery"]
#     service_types = ["Ignition system service", "Tune-up", "Engine service", "Brake replacement", "Transmission service", "Brake service", "Tyre rotation", "Electrical system check"]
#     spare_part_rates = {"Spark plugs": 200, "Air filter": 300, "Oil filter": 150, "Brake pads": 500, "Chain sprockets": 800, "Engine oil": 400,
#                         "Clutch cable": 100, "Brake cable": 120, "Tyres": 2000, "Battery": 1500}
#     service_type_rates = {"Ignition system service": 500, "Tune-up": 600, "Engine service": 1000, "Brake replacement": 800, "Transmission service": 1200, "Brake service": 700,
#                           "Tyre rotation": 300, "Electrical system check": 400}

#     job_card_frame = ttk.Frame(root)
#     job_card_frame.pack(padx=10, pady=10)

#     def calculate_rate():
#         total = 0
#         for row in range(len(spare_part_combos)):
#             part = spare_part_combos[row].get()
#             service = service_type_combos[row].get()
#             if part and service:
#                 total += spare_part_rates.get(part, 0) + service_type_rates.get(service, 0)
#         total_label.config(text=f"Total: {total}")

#     table_canvas = tk.Canvas(job_card_frame)
#     table_canvas.pack(side=tk.LEFT)

#     scrollbar = ttk.Scrollbar(job_card_frame, orient="vertical", command=table_canvas.yview)
#     scrollbar.pack(side=tk.LEFT, fill=tk.Y)

#     table_canvas.configure(yscrollcommand=scrollbar.set)

#     table_frame = ttk.Frame(table_canvas)
#     table_canvas.create_window((0, 0), window=table_frame, anchor="nw")

#     spare_part_combos = []
#     service_type_combos = []

#     # Updated function with better dynamic filtering
#     def delayed_filter(event, combo, values):
#         value = combo.get().lower()
#         data = [item for item in values if value in item.lower()]
#         combo['values'] = data
#         if data:
#             combo.event_generate('<Down>')  # Keep dropdown open

#     def add_row():
#         row = len(spare_part_combos)

#         spare_part_combo = ttk.Combobox(table_frame)
#         spare_part_combo['values'] = spare_parts  # Set initial values
#         service_type_combo = ttk.Combobox(table_frame)
#         service_type_combo['values'] = service_types  # Set initial values

#         spare_part_combo.grid(row=row, column=0, padx=5, pady=5)
#         service_type_combo.grid(row=row, column=1, padx=5, pady=5)

#         spare_part_combos.append(spare_part_combo)
#         service_type_combos.append(service_type_combo)

#         # Bind KeyRelease to dynamically filter options
#         spare_part_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, spare_part_combo, spare_parts))
#         service_type_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, service_type_combo, service_types))

#         def update_cell(event):
#             calculate_rate()

#         spare_part_combo.bind("<<ComboboxSelected>>", update_cell)
#         service_type_combo.bind("<<ComboboxSelected>>", update_cell)

#     for _ in range(10):
#         add_row()

#     total_label = ttk.Label(job_card_frame, text="Total: 0")
#     total_label.pack(pady=5)

#     def generate_bill():
#         vehicle_number = vehicle_entry.get()
#         customer_name = customer_entry.get()
#         bill_text = f"Bill for {customer_name} (Vehicle No: {vehicle_number}):\n\n"
#         for row in range(len(spare_part_combos)):
#             part = spare_part_combos[row].get()
#             service = service_type_combos[row].get()
#             if part and service:
#                 rate = spare_part_rates[part] + service_type_rates[service]
#                 bill_text += f"{part} - {service}: {rate}\n"
#         bill_text += f"\nTotal: {total_label.cget('text').split(': ')[1]}"
#         bill_label.config(text=bill_text)

#     # Vehicle number and customer name input
#     input_frame = ttk.Frame(root)
#     input_frame.pack(padx=10, pady=10)

#     ttk.Label(input_frame, text="Vehicle Number:").grid(row=0, column=0, padx=5, pady=5)
#     vehicle_entry = ttk.Entry(input_frame)
#     vehicle_entry.grid(row=0, column=1, padx=5, pady=5)

#     ttk.Label(input_frame, text="Customer Name:").grid(row=1, column=0, padx=5, pady=5)
#     customer_entry = ttk.Entry(input_frame)
#     customer_entry.grid(row=1, column=1, padx=5, pady=5)

#     # Generate Bill Button
#     generate_button = ttk.Button(input_frame, text="Generate Bill", command=generate_bill)
#     generate_button.grid(row=2, columnspan=2, pady=10)

#     # Bill display label
#     bill_label = ttk.Label(root, text="", justify="left")
#     bill_label.pack(pady=10)

#     # Update the scroll region
#     def update_scroll_region(event):
#         table_canvas.configure(scrollregion=table_canvas.bbox("all"))

#     table_frame.bind("<Configure>", update_scroll_region)

#     root.mainloop()

# job_page()


# import tkinter as tk
# from tkinter import ttk

# def job_page():
#     root = tk.Tk()
#     root.title("Job Card")

#     spare_parts = ["Spark plugs", "Air filter", "Oil filter", "Brake pads", "Chain sprockets", "Engine oil", "Clutch cable", "Brake cable", "Tyres", "Battery"]
#     service_types = ["Ignition system service", "Tune-up", "Engine service", "Brake replacement", "Transmission service", "Brake service", "Tyre rotation", "Electrical system check"]
#     spare_part_rates = {"Spark plugs": 200, "Air filter": 300, "Oil filter": 150, "Brake pads": 500, "Chain sprockets": 800, "Engine oil": 400,
#                         "Clutch cable": 100, "Brake cable": 120, "Tyres": 2000, "Battery": 1500}
#     service_type_rates = {"Ignition system service": 500, "Tune-up": 600, "Engine service": 1000, "Brake replacement": 800, "Transmission service": 1200, "Brake service": 700,
#                           "Tyre rotation": 300, "Electrical system check": 400}

#     job_card_frame = ttk.Frame(root)
#     job_card_frame.pack(padx=10, pady=10)

#     def calculate_rate():
#         total = 0
#         for row in range(len(spare_part_combos)):
#             part = spare_part_combos[row].get()
#             service = service_type_combos[row].get()
#             if part and service:
#                 total += spare_part_rates.get(part, 0) + service_type_rates.get(service, 0)
#         total_label.config(text=f"Total: {total}")

#     table_canvas = tk.Canvas(job_card_frame)
#     table_canvas.pack(side=tk.LEFT)

#     scrollbar = ttk.Scrollbar(job_card_frame, orient="vertical", command=table_canvas.yview)
#     scrollbar.pack(side=tk.LEFT, fill=tk.Y)

#     table_canvas.configure(yscrollcommand=scrollbar.set)

#     table_frame = ttk.Frame(table_canvas)
#     table_canvas.create_window((0, 0), window=table_frame, anchor="nw")

#     spare_part_combos = []
#     service_type_combos = []

#     def delayed_filter(event, combo, values):
#         def filter_combobox():
#             value = combo.get().lower()
#             data = [item for item in values if value in item.lower()]
#             combo['values'] = data
#             combo.event_generate('<Down>')  # Keep dropdown open
            
#             # Keep the combobox's input focused so the user can keep typing
#             combo.icursor(tk.END)
#             combo.selection_clear()

#         if hasattr(combo, 'after_id'):
#             combo.after_cancel(combo.after_id)  # Cancel previous scheduled call if any
#         combo.after_id = combo.after(300, filter_combobox)  # Schedule new filtering after 300ms

#     def add_row():
#         row = len(spare_part_combos)

#         spare_part_combo = ttk.Combobox(table_frame)
#         spare_part_combo['values'] = spare_parts  # Set initial values
#         service_type_combo = ttk.Combobox(table_frame)
#         service_type_combo['values'] = service_types  # Set initial values

#         spare_part_combo.grid(row=row, column=0, padx=5, pady=5)
#         service_type_combo.grid(row=row, column=1, padx=5, pady=5)

#         spare_part_combos.append(spare_part_combo)
#         service_type_combos.append(service_type_combo)

#         # Bind KeyRelease to dynamically filter options
#         spare_part_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, spare_part_combo, spare_parts))
#         service_type_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, service_type_combo, service_types))

#         def update_cell(event):
#             calculate_rate()

#         spare_part_combo.bind("<<ComboboxSelected>>", update_cell)
#         service_type_combo.bind("<<ComboboxSelected>>", update_cell)

#     for _ in range(10):
#         add_row()

#     total_label = ttk.Label(job_card_frame, text="Total: 0")
#     total_label.pack(pady=5)

#     def generate_bill():
#         vehicle_number = vehicle_entry.get()
#         customer_name = customer_entry.get()
#         bill_text = f"Bill for {customer_name} (Vehicle No: {vehicle_number}):\n\n"
#         for row in range(len(spare_part_combos)):
#             part = spare_part_combos[row].get()
#             service = service_type_combos[row].get()
#             if part and service:
#                 rate = spare_part_rates[part] + service_type_rates[service]
#                 bill_text += f"{part} - {service}: {rate}\n"
#         bill_text += f"\nTotal: {total_label.cget('text').split(': ')[1]}"
#         bill_label.config(text=bill_text)

#     # Vehicle number and customer name input
#     input_frame = ttk.Frame(root)
#     input_frame.pack(padx=10, pady=10)

#     ttk.Label(input_frame, text="Vehicle Number:").grid(row=0, column=0, padx=5, pady=5)
#     vehicle_entry = ttk.Entry(input_frame)
#     vehicle_entry.grid(row=0, column=1, padx=5, pady=5)

#     ttk.Label(input_frame, text="Customer Name:").grid(row=1, column=0, padx=5, pady=5)
#     customer_entry = ttk.Entry(input_frame)
#     customer_entry.grid(row=1, column=1, padx=5, pady=5)

#     # Generate Bill Button
#     generate_button = ttk.Button(input_frame, text="Generate Bill", command=generate_bill)
#     generate_button.grid(row=2, columnspan=2, pady=10)

#     # Bill display label
#     bill_label = ttk.Label(root, text="", justify="left")
#     bill_label.pack(pady=10)

#     # Update the scroll region
#     def update_scroll_region(event):
#         table_canvas.configure(scrollregion=table_canvas.bbox("all"))

#     table_frame.bind("<Configure>", update_scroll_region)

#     root.mainloop()

# job_page()


# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox

# # Simulated spare parts inventory
# spare_parts_inventory = {
#     "Spark plugs": 50,
#     "Air filter": 30,
#     "Oil filter": 20,
#     "Brake pads": 40,
#     "Chain sprockets": 10,
#     "Engine oil": 100,
#     "Clutch cable": 25,
#     "Brake cable": 30,
#     "Tyres": 15,
#     "Battery": 20
# }

# def job_page():
#     root = tk.Tk()
#     root.title("Job Card")

#     spare_parts = ["Spark plugs", "Air filter", "Oil filter", "Brake pads", "Chain sprockets", "Engine oil", "Clutch cable", "Brake cable", "Tyres", "Battery"]
#     service_types = ["Ignition system service", "Tune-up", "Engine service", "Brake replacement", "Transmission service", "Brake service", "Tyre rotation", "Electrical system check"]
#     spare_part_rates = {"Spark plugs": 200, "Air filter": 300, "Oil filter": 150, "Brake pads": 500, "Chain sprockets": 800, "Engine oil": 400,
#                         "Clutch cable": 100, "Brake cable": 120, "Tyres": 2000, "Battery": 1500}
#     service_type_rates = {"Ignition system service": 500, "Tune-up": 600, "Engine service": 1000, "Brake replacement": 800, "Transmission service": 1200, "Brake service": 700,
#                           "Tyre rotation": 300, "Electrical system check": 400}

#     job_card_frame = ttk.Frame(root)
#     job_card_frame.pack(padx=10, pady=10)

#     def calculate_rate():
#         total = 0
#         for row in range(len(spare_part_combos)):
#             part = spare_part_combos[row].get()
#             service = service_type_combos[row].get()
#             if part and service:
#                 total += spare_part_rates.get(part.split(' - ')[0], 0) + service_type_rates.get(service, 0)
#         total_label.config(text=f"Total: {total}")

#     table_canvas = tk.Canvas(job_card_frame)
#     table_canvas.pack(side=tk.LEFT)

#     scrollbar = ttk.Scrollbar(job_card_frame, orient="vertical", command=table_canvas.yview)
#     scrollbar.pack(side=tk.LEFT, fill=tk.Y)

#     table_canvas.configure(yscrollcommand=scrollbar.set)

#     table_frame = ttk.Frame(table_canvas)
#     table_canvas.create_window((0, 0), window=table_frame, anchor="nw")

#     spare_part_combos = []
#     service_type_combos = []

#     def update_combobox_values(combo, values):
#         inventory_labels = [f"{item} - {spare_parts_inventory[item]}" for item in values]
#         combo['values'] = inventory_labels

#     def delayed_filter(event, combo, values):
#         def filter_combobox():
#             value = combo.get().split(' - ')[0].lower()
#             data = [item for item in values if value in item.lower()]
#             inventory_labels = [f"{item} - {spare_parts_inventory[item]}" for item in data]
#             combo['values'] = inventory_labels
#             combo.event_generate('<Down>')  # Keep dropdown open
            
#             # Keep the combobox's input focused so the user can keep typing
#             combo.icursor(tk.END)
#             combo.selection_clear()

#         if hasattr(combo, 'after_id'):
#             combo.after_cancel(combo.after_id)  # Cancel previous scheduled call if any
#         combo.after_id = combo.after(300, filter_combobox)  # Schedule new filtering after 300ms

#     def add_row():
#         row = len(spare_part_combos)

#         spare_part_combo = ttk.Combobox(table_frame)
#         update_combobox_values(spare_part_combo, spare_parts)  # Set initial values with inventory
#         service_type_combo = ttk.Combobox(table_frame)
#         service_type_combo['values'] = service_types  # Set initial values

#         spare_part_combo.grid(row=row, column=0, padx=5, pady=5)
#         service_type_combo.grid(row=row, column=1, padx=5, pady=5)

#         spare_part_combos.append(spare_part_combo)
#         service_type_combos.append(service_type_combo)

#         def update_inventory(event):
#             selected_part = spare_part_combo.get().split(' - ')[0]
#             if selected_part in spare_parts_inventory:
#                 spare_parts_inventory[selected_part] -= 1
#                 update_combobox_values(spare_part_combo, spare_parts)
#                 calculate_rate()

#         # Bind KeyRelease to dynamically filter options
#         spare_part_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, spare_part_combo, spare_parts))
#         service_type_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, service_type_combo, service_types))

#         # Bind combobox selection to update inventory and calculate rate
#         spare_part_combo.bind("<<ComboboxSelected>>", update_inventory)
#         service_type_combo.bind("<<ComboboxSelected>>", lambda event: calculate_rate())

#     for _ in range(10):
#         add_row()

#     total_label = ttk.Label(job_card_frame, text="Total: 0")
#     total_label.pack(pady=5)

#     def generate_bill():
#         vehicle_number = vehicle_entry.get()
#         customer_name = customer_entry.get()
#         bill_text = f"Bill for {customer_name} (Vehicle No: {vehicle_number}):\n\n"
#         for row in range(len(spare_part_combos)):
#             part = spare_part_combos[row].get().split(' - ')[0]
#             service = service_type_combos[row].get()
#             if part and service:
#                 rate = spare_part_rates[part] + service_type_rates[service]
#                 bill_text += f"{part} - {service}: {rate}\n"
#         bill_text += f"\nTotal: {total_label.cget('text').split(': ')[1]}"
#         bill_label.config(text=bill_text)

#     # Vehicle number and customer name input
#     input_frame = ttk.Frame(root)
#     input_frame.pack(padx=10, pady=10)

#     ttk.Label(input_frame, text="Vehicle Number:").grid(row=0, column=0, padx=5, pady=5)
#     vehicle_entry = ttk.Entry(input_frame)
#     vehicle_entry.grid(row=0, column=1, padx=5, pady=5)

#     ttk.Label(input_frame, text="Customer Name:").grid(row=1, column=0, padx=5, pady=5)
#     customer_entry = ttk.Entry(input_frame)
#     customer_entry.grid(row=1, column=1, padx=5, pady=5)

#     # Generate Bill Button
#     generate_button = ttk.Button(input_frame, text="Generate Bill", command=generate_bill)
#     generate_button.grid(row=2, columnspan=2, pady=10)

#     # Bill display label
#     bill_label = ttk.Label(root, text="", justify="left")
#     bill_label.pack(pady=10)

#     # Update the scroll region
#     def update_scroll_region(event):
#         table_canvas.configure(scrollregion=table_canvas.bbox("all"))

#     table_frame.bind("<Configure>", update_scroll_region)

#     root.mainloop()

# job_page()


# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox

# # Simulated spare parts inventory
# spare_parts_inventory = {"Spark plugs": 50,"Air filter": 30,"Oil filter": 20,"Brake pads": 40,"Chain sprockets": 10,
#     "Engine oil": 100,"Clutch cable": 25,"Brake cable": 30,"Tyres": 15,"Battery": 20}

# def job_page():
#     root = tk.Tk()
#     root.title("Job Card")

#     spare_parts = ["Spark plugs", "Air filter", "Oil filter", "Brake pads", "Chain sprockets", "Engine oil", "Clutch cable", "Brake cable", "Tyres", "Battery"]
#     service_types = ["Ignition system service", "Tune-up", "Engine service", "Brake replacement", "Transmission service", "Brake service", "Tyre rotation", "Electrical system check"]
#     spare_part_rates = {"Spark plugs": 200, "Air filter": 300, "Oil filter": 150, "Brake pads": 500, "Chain sprockets": 800, "Engine oil": 400,
#                         "Clutch cable": 100, "Brake cable": 120, "Tyres": 2000, "Battery": 1500}
#     service_type_rates = {"Ignition system service": 500, "Tune-up": 600, "Engine service": 1000, "Brake replacement": 800, "Transmission service": 1200, "Brake service": 700,
#                           "Tyre rotation": 300, "Electrical system check": 400}

#     job_card_frame = ttk.Frame(root)
#     job_card_frame.pack(padx=10, pady=10)

#     def calculate_rate():
#         total = 0
#         for row in range(len(spare_part_combos)):
#             part = spare_part_combos[row].get()
#             quantity = quantity_entries[row].get()
#             service = service_type_combos[row].get()
#             if part and service and quantity:
#                 total += spare_part_rates.get(part.split(' - ')[0], 0) * int(quantity) + service_type_rates.get(service, 0)
#         total_label.config(text=f"Total: {total}")

#     table_canvas = tk.Canvas(job_card_frame)
#     table_canvas.pack(side=tk.LEFT)

#     scrollbar = ttk.Scrollbar(job_card_frame, orient="vertical", command=table_canvas.yview)
#     scrollbar.pack(side=tk.LEFT, fill=tk.Y)

#     table_canvas.configure(yscrollcommand=scrollbar.set)

#     table_frame = ttk.Frame(table_canvas)
#     table_canvas.create_window((0, 0), window=table_frame, anchor="nw")

#     spare_part_combos = []
#     service_type_combos = []
#     quantity_entries = []

#     def update_combobox_values(combo, values):
#         inventory_labels = [f"{item} - {spare_parts_inventory[item]}" for item in values]
#         combo['values'] = inventory_labels

#     def delayed_filter(event, combo, values):
#         def filter_combobox():
#             value = combo.get().split(' - ')[0].lower()
#             data = [item for item in values if value in item.lower()]
#             inventory_labels = [f"{item} - {spare_parts_inventory[item]}" for item in data]
#             combo['values'] = inventory_labels
#             combo.event_generate('<Down>')  # Keep dropdown open
            
#             # Keep the combobox's input focused so the user can keep typing
#             combo.icursor(tk.END)
#             combo.selection_clear()

#         if hasattr(combo, 'after_id'):
#             combo.after_cancel(combo.after_id)  # Cancel previous scheduled call if any
#         combo.after_id = combo.after(300, filter_combobox)  # Schedule new filtering after 300ms

#     def add_row():
#         row = len(spare_part_combos)

#         spare_part_combo = ttk.Combobox(table_frame)
#         update_combobox_values(spare_part_combo, spare_parts)  # Set initial values with inventory
#         service_type_combo = ttk.Combobox(table_frame)
#         service_type_combo['values'] = service_types  # Set initial values

#         quantity_entry = ttk.Entry(table_frame, width=5)

#         spare_part_combo.grid(row=row, column=0, padx=5, pady=5)
#         quantity_entry.grid(row=row, column=1, padx=5, pady=5)
#         service_type_combo.grid(row=row, column=2, padx=5, pady=5)

#         spare_part_combos.append(spare_part_combo)
#         service_type_combos.append(service_type_combo)
#         quantity_entries.append(quantity_entry)

#         def update_inventory(event):
#             selected_part = spare_part_combo.get().split(' - ')[0]
#             quantity = quantity_entry.get()
#             if selected_part in spare_parts_inventory and quantity.isdigit():
#                 new_quantity = spare_parts_inventory[selected_part] - int(quantity)
#                 if new_quantity >= 0:
#                     spare_parts_inventory[selected_part] = new_quantity
#                     update_combobox_values(spare_part_combo, spare_parts)
#                 else:
#                     messagebox.showerror("Error", f"Not enough {selected_part} in inventory.")
#                     spare_part_combo.set('')
#                     quantity_entry.delete(0, tk.END)

#             calculate_rate()

#         # Bind KeyRelease to dynamically filter options
#         spare_part_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, spare_part_combo, spare_parts))
#         service_type_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, service_type_combo, service_types))

#         # Bind combobox selection to update inventory and calculate rate
#         spare_part_combo.bind("<<ComboboxSelected>>", update_inventory)
#         service_type_combo.bind("<<ComboboxSelected>>", lambda event: calculate_rate())
#         quantity_entry.bind("<FocusOut>", update_inventory)

#     for _ in range(10):
#         add_row()

#     total_label = ttk.Label(job_card_frame, text="Total: 0")
#     total_label.pack(pady=5)

#     def generate_bill():
#         vehicle_number = vehicle_entry.get()
#         customer_name = customer_entry.get()
#         bill_text = f"Bill for {customer_name} (Vehicle No: {vehicle_number}):\n\n"
#         for row in range(len(spare_part_combos)):
#             part = spare_part_combos[row].get().split(' - ')[0]
#             service = service_type_combos[row].get()
#             quantity = quantity_entries[row].get()
#             if part and service and quantity:
#                 rate = spare_part_rates[part] * int(quantity) + service_type_rates[service]
#                 bill_text += f"{part} x{quantity} - {service}: {rate}\n"
#         bill_text += f"\nTotal: {total_label.cget('text').split(': ')[1]}"
#         bill_label.config(text=bill_text)

#     # Vehicle number and customer name input
#     input_frame = ttk.Frame(root)
#     input_frame.pack(padx=10, pady=10)

#     ttk.Label(input_frame, text="Vehicle Number:").grid(row=0, column=0, padx=5, pady=5)
#     vehicle_entry = ttk.Entry(input_frame)
#     vehicle_entry.grid(row=0, column=1, padx=5, pady=5)

#     ttk.Label(input_frame, text="Customer Name:").grid(row=1, column=0, padx=5, pady=5)
#     customer_entry = ttk.Entry(input_frame)
#     customer_entry.grid(row=1, column=1, padx=5, pady=5)

#     # Generate Bill Button
#     generate_button = ttk.Button(input_frame, text="Generate Bill", command=generate_bill)
#     generate_button.grid(row=2, columnspan=2, pady=10)

#     # Bill display label
#     bill_label = ttk.Label(root, text="", justify="left")
#     bill_label.pack(pady=10)

#     # Update the scroll region
#     def update_scroll_region(event):
#         table_canvas.configure(scrollregion=table_canvas.bbox("all"))

#     table_frame.bind("<Configure>", update_scroll_region)

#     root.mainloop()

# job_page()



# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox

# # Simulated spare parts inventory
# spare_parts_inventory = {
#     "Spark plugs": 50,
#     "Air filter": 30,
#     "Oil filter": 20,
#     "Brake pads": 40,
#     "Chain sprockets": 10,
#     "Engine oil": 100,
#     "Clutch cable": 25,
#     "Brake cable": 30,
#     "Tyres": 15,
#     "Battery": 20
# }

# # A copy of the original inventory to reset after each operation
# original_inventory = spare_parts_inventory.copy()

# def job_page():
#     root = tk.Tk()
#     root.title("Job Card")

#     spare_parts = ["Spark plugs", "Air filter", "Oil filter", "Brake pads", "Chain sprockets", "Engine oil", "Clutch cable", "Brake cable", "Tyres", "Battery"]
#     service_types = ["Ignition system service", "Tune-up", "Engine service", "Brake replacement", "Transmission service", "Brake service", "Tyre rotation", "Electrical system check"]
#     spare_part_rates = {"Spark plugs": 200, "Air filter": 300, "Oil filter": 150, "Brake pads": 500, "Chain sprockets": 800, "Engine oil": 400,
#                         "Clutch cable": 100, "Brake cable": 120, "Tyres": 2000, "Battery": 1500}
#     service_type_rates = {"Ignition system service": 500, "Tune-up": 600, "Engine service": 1000, "Brake replacement": 800, "Transmission service": 1200, "Brake service": 700,
#                           "Tyre rotation": 300, "Electrical system check": 400}

#     job_card_frame = ttk.Frame(root)
#     job_card_frame.pack(padx=10, pady=10)

#     def calculate_rate():
#         total = 0
#         for row in range(len(spare_part_combos)):
#             part = spare_part_combos[row].get()
#             quantity = quantity_entries[row].get()
#             service = service_type_combos[row].get()
#             if part and service and quantity.isdigit():
#                 total += spare_part_rates.get(part.split(' - ')[0], 0) * int(quantity) + service_type_rates.get(service, 0)
#         total_label.config(text=f"Total: {total}")

#     def update_combobox_values():
#         for combo in spare_part_combos:
#             current_value = combo.get()
#             inventory_labels = [f"{item} - {spare_parts_inventory[item]}" for item in spare_parts]
#             combo['values'] = inventory_labels
#             combo.set(current_value)

#     table_canvas = tk.Canvas(job_card_frame)
#     table_canvas.pack(side=tk.LEFT)

#     scrollbar = ttk.Scrollbar(job_card_frame, orient="vertical", command=table_canvas.yview)
#     scrollbar.pack(side=tk.LEFT, fill=tk.Y)

#     table_canvas.configure(yscrollcommand=scrollbar.set)

#     table_frame = ttk.Frame(table_canvas)
#     table_canvas.create_window((0, 0), window=table_frame, anchor="nw")

#     spare_part_combos = []
#     service_type_combos = []
#     quantity_entries = []

#     def delayed_filter(event, combo, values):
#         def filter_combobox():
#             value = combo.get().split(' - ')[0].lower()
#             data = [item for item in values if value in item.lower()]
#             inventory_labels = [f"{item} - {spare_parts_inventory[item]}" for item in data]
#             combo['values'] = inventory_labels
#             combo.event_generate('<Down>')  # Keep dropdown open
            
#             # Keep the combobox's input focused so the user can keep typing
#             combo.icursor(tk.END)
#             combo.selection_clear()

#         if hasattr(combo, 'after_id'):
#             combo.after_cancel(combo.after_id)  # Cancel previous scheduled call if any
#         combo.after_id = combo.after(300, filter_combobox)  # Schedule new filtering after 300ms

#     def add_row():
#         row = len(spare_part_combos)

#         spare_part_combo = ttk.Combobox(table_frame)
#         service_type_combo = ttk.Combobox(table_frame)
#         quantity_entry = ttk.Entry(table_frame, width=5)

#         spare_part_combo.grid(row=row, column=0, padx=5, pady=5)
#         quantity_entry.grid(row=row, column=1, padx=5, pady=5)
#         service_type_combo.grid(row=row, column=2, padx=5, pady=5)

#         spare_part_combos.append(spare_part_combo)
#         service_type_combos.append(service_type_combo)
#         quantity_entries.append(quantity_entry)

#         update_combobox_values()

#         def update_inventory(event):
#             selected_part = spare_part_combo.get().split(' - ')[0]
#             quantity = quantity_entry.get()
#             if selected_part in spare_parts_inventory and quantity.isdigit():
#                 total_quantity_needed = sum(int(q.get()) for q in quantity_entries if q.get().isdigit() and spare_part_combos[quantity_entries.index(q)].get().split(' - ')[0] == selected_part)
#                 new_quantity = original_inventory[selected_part] - total_quantity_needed
#                 if new_quantity >= 0:
#                     spare_parts_inventory[selected_part] = new_quantity
#                     update_combobox_values()
#                     calculate_rate()
#                 else:
#                     messagebox.showerror("Error", f"Not enough {selected_part} in inventory.")
#                     spare_part_combo.set('')
#                     quantity_entry.delete(0, tk.END)

#         # Bind KeyRelease to dynamically filter options
#         spare_part_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, spare_part_combo, spare_parts))
#         service_type_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, service_type_combo, service_types))

#         # Bind combobox selection to update inventory and calculate rate
#         spare_part_combo.bind("<<ComboboxSelected>>", update_inventory)
#         service_type_combo.bind("<<ComboboxSelected>>", lambda event: calculate_rate())
#         quantity_entry.bind("<FocusOut>", update_inventory)

#     for _ in range(10):
#         add_row()

#     total_label = ttk.Label(job_card_frame, text="Total: 0")
#     total_label.pack(pady=5)

#     def generate_bill():
#         vehicle_number = vehicle_entry.get()
#         customer_name = customer_entry.get()
#         bill_text = f"Bill for {customer_name} (Vehicle No: {vehicle_number}):\n\n"
#         for row in range(len(spare_part_combos)):
#             part = spare_part_combos[row].get().split(' - ')[0]
#             service = service_type_combos[row].get()
#             quantity = quantity_entries[row].get()
#             if part and service and quantity:
#                 rate = spare_part_rates[part] * int(quantity) + service_type_rates[service]
#                 bill_text += f"{part} x{quantity} - {service}: {rate}\n"
#         bill_text += f"\nTotal: {total_label.cget('text').split(': ')[1]}"
#         bill_label.config(text=bill_text)

#     # Vehicle number and customer name input
#     input_frame = ttk.Frame(root)
#     input_frame.pack(padx=10, pady=10)

#     ttk.Label(input_frame, text="Vehicle Number:").grid(row=0, column=0, padx=5, pady=5)
#     vehicle_entry = ttk.Entry(input_frame)
#     vehicle_entry.grid(row=0, column=1, padx=5, pady=5)

#     ttk.Label(input_frame, text="Customer Name:").grid(row=1, column=0, padx=5, pady=5)
#     customer_entry = ttk.Entry(input_frame)
#     customer_entry.grid(row=1, column=1, padx=5, pady=5)

#     # Generate Bill Button
#     generate_button = ttk.Button(input_frame, text="Generate Bill", command=generate_bill)
#     generate_button.grid(row=2, columnspan=2, pady=10)

#     # Bill display label
#     bill_label = ttk.Label(root, text="", justify="left")
#     bill_label.pack(pady=10)

#     # Update the scroll region
#     def update_scroll_region(event):
#         table_canvas.configure(scrollregion=table_canvas.bbox("all"))

#     table_frame.bind("<Configure>", update_scroll_region)

#     root.mainloop()

# job_page()



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Simulated spare parts inventory
spare_parts_inventory = {
    "Spark plugs": 50,
    "Air filter": 30,
    "Oil filter": 20,
    "Brake pads": 40,
    "Chain sprockets": 10,
    "Engine oil": 100,
    "Clutch cable": 25,
    "Brake cable": 30,
    "Tyres": 15,
    "Battery": 20
}

# A copy of the original inventory to reset after each operation
original_inventory = spare_parts_inventory.copy()

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
            quantity = quantity_entries[row].get()
            service = service_type_combos[row].get()
            if part and service and quantity.isdigit():
                total += spare_part_rates.get(part.split(' - ')[0], 0) * int(quantity) + service_type_rates.get(service, 0)
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
            combo.event_generate('<Down>')  # Keep dropdown open
            
            # Keep the combobox's input focused so the user can keep typing
            combo.icursor(tk.END)
            combo.selection_clear()

        if hasattr(combo, 'after_id'):
            combo.after_cancel(combo.after_id)  # Cancel previous scheduled call if any
        combo.after_id = combo.after(300, filter_combobox)  # Schedule new filtering after 300ms

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

        # Bind KeyRelease to dynamically filter options
        spare_part_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, spare_part_combo, spare_parts))
        service_type_combo.bind('<KeyRelease>', lambda event: delayed_filter(event, service_type_combo, service_types))

        # Bind combobox selection to update inventory and calculate rate
        spare_part_combo.bind("<<ComboboxSelected>>", update_inventory)
        service_type_combo.bind("<<ComboboxSelected>>", lambda event: calculate_rate())
        quantity_entry.bind("<FocusOut>", update_inventory)

    for _ in range(10):
        add_row()

    total_label = ttk.Label(job_card_frame, text="Total: 0")
    total_label.pack(pady=5)

    def generate_bill():
        vehicle_number = vehicle_entry.get()
        customer_name = customer_entry.get()
        bill_text = f"Bill for {customer_name} (Vehicle No: {vehicle_number}):\n\n"
        for row in range(len(spare_part_combos)):
            part = spare_part_combos[row].get().split(' - ')[0]
            service = service_type_combos[row].get()
            quantity = quantity_entries[row].get()
            if part and service and quantity:
                rate = spare_part_rates[part] * int(quantity) + service_type_rates[service]
                bill_text += f"{part} x{quantity} - {service}: {rate}\n"
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

job_page()
