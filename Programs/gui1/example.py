from tkinter import *



app=Tk()
app.title("Head-Ex Deliveries")
Label(app,text="Depot").pack()
depot=Entry(app)
depot.pack()
Label(app,text="Description").pack()
description=Entry(app)
description.pack()
Label(app,text="Address").pack()
Address=Text(app)
Address.pack()

def savedetails():
	file=open("deliveries.txt","a")
	file.write("Depot:\n")
	file.write("%s\n" %depot.get())
	file.write("Description:\n")
	file.write("%s\n" %description.get())
	file.write("Address:\n")
	file.write("%s\n" %Address.get("1.0",END))
	depot.delete(0,END)
	description.delete(0,END)
	Address.delete("1.0",END)


Button(app,text="Save",command=savedetails).pack()

app.mainloop()
