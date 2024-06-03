import tkinter as tk
root=tk.Tk()
root.geometry("1000x500")
root.title("Vehicle Service Centre")
options_frame=tk.Frame(root,bg="#A89DC7")

def job_page():
    job_frame=tk.Frame(main_frame)
    lb=tk.Label(job_frame,text="JOB CARD\n\n",font=("Bold",30))
    lb.pack()
    job_frame.pack(pady=20)

def cus_page():
    cus_frame=tk.Frame(main_frame)
    lb=tk.Label(cus_frame,text="CUSTOMER CARD",font=("Bole",30))
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

def hide_indicators():
    job_indicate.config(bg="#c3c3c3")
    cus_indicate.config(bg="#c3c3c3")
    assign_indicate.config(bg="#c3c3c3")
    unassigned_indicate.config(bg="#c3c3c3")
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