from tkinter import *
from tkinter.ttk import *
import sqlite3
from tkinter import messagebox

class ChangePasswordFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        s = Style()
        s.configure('TFrame', background='white')
        s.configure('TLabel', background='white', font=('Arial', 15))
        s.configure('TButton', width=15, font=('Arial', 15))
        s.configure('Content.TFrame', background='white')
        
        self.place(relx=.5, rely=.5, anchor=CENTER)

        old_psw_label = Label(self, text="Old Password:", style='TLabel')
        old_psw_label.grid(row=0, column=0)

        self.old_psw_entry = Entry(self, font=('Arial', 15))  
        self.old_psw_entry.grid(row=0, column=1)

        new_psw_label = Label(self, text="New Password:", style='TLabel')
        new_psw_label.grid(row=1, column=0)

        self.new_psw_entry = Entry(self, font=('Arial', 15))  
        self.new_psw_entry.grid(row=1, column=1)

        confirm_psw_label = Label(self, text="Confirm Password:", style='TLabel')
        confirm_psw_label.grid(row=2, column=0)

        self.confirm_psw_entry = Entry(self, font=('Arial', 15))  
        self.confirm_psw_entry.grid(row=2, column=1)

        change_psw_button = Button(self, text='Change Password', command=self.change_password)
        change_psw_button.grid(row=3, column=1)

    def change_password(self):
        con = sqlite3.connect('contacts.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM Login WHERE password = ?", (self.old_psw_entry.get(),))  
        user = cur.fetchone()
        if user:
            if self.new_psw_entry.get() == self.confirm_psw_entry.get():
                cur.execute("UPDATE Login SET password = ? WHERE password = ?", (self.new_psw_entry.get(), self.old_psw_entry.get()))
                con.commit()
                messagebox.showinfo("Success", "Password changed successfully.")
            else:
                messagebox.showerror("Error", "New passwords do not match.")
        else:
            messagebox.showerror("Error", "Old password is incorrect.")
        con.close()

if __name__ == '__main__':
    root = Tk()
    frame = ChangePasswordFrame(root)
    root.mainloop()
