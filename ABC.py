from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = Tk()
root.title("Management")
root.iconphoto(True,tk.PhotoImage(file="icon.png"))
root.config(bg="#ffd85c")

appLabel = Label(root, text="Student Management System",bg="#ffd85c", fg="#06a099", width=35,font=("AR JULIAN", 30,"bold italic"))
#appLabel.config(font=("AR JULIAN", 30))
appLabel.grid(row=0, column = 0, columnspan=2, padx=(10,10), pady=(30, 0))

TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

def enter():
    connection = sqlite3.connect('management.db')
    
    global TABLE_NAME,STUDENT_ADDRESS,STUDENT_COLLEGE,STUDENT_NAME,STUDENT_PHONE
    TABLE_NAME = "management_table"
    STUDENT_ID = "student_id"
    STUDENT_NAME = "student_name"
    STUDENT_COLLEGE = "student_college"
    STUDENT_ADDRESS = "student_address"
    STUDENT_PHONE = "student_phone"
    
    connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                       " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                       STUDENT_NAME + " TEXT , " + STUDENT_COLLEGE + " TEXT, " +
                       STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")
    
    class Student:
        studentName = ""
        collegeName = ""
        phoneNumber = 0
        address = ""
    
        def __init__(self, studentName, collegeName, phoneNumber, address):
            self.studentName = studentName
            self.collegeName = collegeName
            self.phoneNumber = phoneNumber
            self.address = address
    
    global nameEntry,collegeEntry,phoneEntry,addressEntry

    nameLabel = tk.Label(root, text="Enter your name", bg="#ffd85c", width=40, anchor='w',
                         font=("Comic Sans MS", 12)).grid(row=2, column=0, padx=(10,0), pady=(15, 0))
    collegeLabel = tk.Label(root, text="Enter your school name",bg="#ffd85c",  width=40, anchor='w',
                            font=("Comic Sans MS", 12)).grid(row=3, column=0, padx=(10,0))
    phoneLabel = tk.Label(root, text="Enter your phone number", bg="#ffd85c", width=40, anchor='w',
                          font=("Comic Sans MS", 12)).grid(row=4, column=0, padx=(10,0))
    addressLabel = tk.Label(root, text="Enter your address", bg="#ffd85c", width=40, anchor='w',
                            font=("Comic Sans MS", 12)).grid(row=5, column=0, padx=(10,0))
    
    nameEntry = tk.Entry(root, width = 30,borderwidth=5)
    collegeEntry = tk.Entry(root, width = 30,borderwidth=5)
    phoneEntry = tk.Entry(root, width = 30,borderwidth=5)
    addressEntry = tk.Entry(root, width = 30,borderwidth=5)
    
    nameEntry.grid(row=2, column=1, padx=(0,10), pady=(15, 10))
    collegeEntry.grid(row=3, column=1, padx=(0,10), pady = 10)
    phoneEntry.grid(row=4, column=1, padx=(0,10), pady = 10)
    addressEntry.grid(row=5, column=1, padx=(0,10), pady = 10)
    
    button = tk.Button(root, text="Take input", bg="white",borderwidth=6,activebackground="sky blue",command=lambda:takeNameInput())
    button.grid(row=6, column=0, columnspan=2, pady=30)

    def takeNameInput():
        global nameEntry, collegeEntry, phoneEntry, addressEntry
        # global username, collegeName, phone, address
        global list
        global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE
        username = nameEntry.get()
        nameEntry.delete(0, tk.END)
        collegeName = collegeEntry.get()
        collegeEntry.delete(0, tk.END)
        phone = int(phoneEntry.get())
        phoneEntry.delete(0, tk.END)
        address = addressEntry.get()
        addressEntry.delete(0, tk.END)
    
        connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                           STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                           STUDENT_PHONE + " ) VALUES ( '"
                           + username + "', '" + collegeName + "', '" +
                           address + "', " + str(phone) + " ); ")
        connection.commit()
        messagebox.showinfo("Success", "Data Saved Successfully.")



def show():
    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Student Management System",bg="#ffd85c", 
                        fg="#06a099", width=40)
    appLabel.config(font=("AR JULIAN", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="College Name")
    tree.heading("three", text="Address")
    tree.heading("four", text="Phone Number")

    connection = sqlite3.connect('management.db')
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()


def delete_record():
    def delete():
        conn = sqlite3.connect('management.db')
        c = conn.cursor()
        c.execute("DELETE from management_table WHERE student_name = '"+ delete_entry.get() +"'")
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Record Deleted Successfully.")
        delete_entry.delete(0, END)
    delete_entry = tk.Entry(root, width=30,borderwidth=5)
    delete_entry.grid(row = 9, column = 1, padx=20, pady=10)
    
    delete_label = tk.Label(root, text = "Enter Student Name", width=30, bg="#ffd85c" ,font=("Comic Sans MS", 12))
    delete_label.grid(row = 9, column = 0, padx=20, pady=10)
    
    delete_btn = tk.Button(root, text="Delete Record",bg="white",borderwidth=6, activebackground="sky blue",command=delete)
    delete_btn.grid(row = 10, columnspan = 2, padx=20, pady=10)

Enter = Button(root, text="Create Student Record", bg="white",activebackground="sky blue",width=40,borderwidth=6,command=enter, font=("Comic Sans MS", 12))
Enter.grid(row=1, column=0, columnspan=2, padx=(10,0),pady=(15, 0))

Show = Button(root, text="Show Student Records", bg="white",activebackground="sky blue",width=40, borderwidth=6,command=show, font=("Comic Sans MS", 12))
Show.grid(row=7, column=0, columnspan=2, padx=(10,0),pady=(15, 0))

Delete = Button(root, text="Delete Student Record", bg="white",activebackground="sky blue",width=40, borderwidth=6,command=delete_record, font=("Comic Sans MS", 12))
Delete.grid(row=8, column=0, columnspan=2, padx=(10,0),pady=(15,10))



def update_record():
    def update():
        conn = sqlite3.connect('management.db')
        c = conn.cursor()
        c.execute("UPDATE management_table SET student_college = 'cool' WHERE student_name = '"+ update_entry.get() +"'")
        #UPDATE from management_table set student_college = msoffice WHERE student_name = '"+ update_entry.get() +"'"
        conn.commit()       
        conn.close()
        
        messagebox.showinfo("Success", "Record UPDATED Successfully.")
        #update_entry.update(0, END)
    update_entry = tk.Entry(root, width=30,borderwidth=5)
    update_entry.grid(row = 9, column = 1, padx=20, pady=10)
    
    update_label = tk.Label(root, text = "Enter Student Name", width=30,bg="#ffd85c",  font=("Comic Sans MS", 12))
    update_label.grid(row = 9, column = 0, padx=20, pady=10)
    
    update_btn = tk.Button(root, text="Update Record",bg="white", activebackground="sky blue",command=update, borderwidth=6)
    update_btn.grid(row = 10, columnspan = 2, padx=20, pady=10)

Update = Button(root, text="Update Student Record", bg="white",activebackground="sky blue",borderwidth=6,width=40, command=update_record, font=("Comic Sans MS", 12))
Update.grid(row=11, column=0, columnspan=2, padx=(10,0),pady=(15,10))

root.mainloop()
