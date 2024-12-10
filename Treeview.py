from tkinter import*
from tkinter.ttk import*

root=Tk()
root.title('Treeview')

contacts_treeview=Treeview(root,columns=('name','phone_no','email_id','city'),show='headings')

contacts_treeview.heading('name',text="Name",anchor=W)
contacts_treeview.heading('phone_no',text="Phone No",anchor=W)
contacts_treeview.heading('email_id',text="Email Id",anchor=W)
contacts_treeview.heading('city',text="City",anchor=W)
contacts_treeview.column('name',width=250)
contacts_treeview.column('phone_no',width=200)
contacts_treeview.column('name',width=250)
contacts_treeview.column('email_id',width=250)
contacts_treeview.column('city',width=100)
contacts_treeview.insert("",0,values=('Rahul Mehra','+91-960436551','fusgdf@gmail.com','hyd'))
contacts_treeview.insert("",1,values=('ygnsmj','+91-96043663','rghcsdu@gmail.com','chennai'))
contacts_treeview.insert("",2,values=('srjhghf','+91-840836551','rgthjk@gmail.com','mumbai'))
contacts_treeview.pack()

root.mainloop()
