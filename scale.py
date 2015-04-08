from tkinter import *
from tkinter import ttk

root = Tk()
content = ttk.Frame(root)

explanation = """This is a simulation for an Elevator.  
Please drag each slider to select the number of 
Floors in the building and the Number of 
Customers to be serviced."""
w2 = Label(root, justify=LEFT, padx = 10, text=explanation).pack(side="left")


cust=Scale(root, from_=0, to=1000, label = "# of Customers") # creates widget
cust.pack(side=RIGHT) # packs widget
floor=Scale(root, from_=0, to=1000, label = "# of Floors") # creates widget
floor.pack(side=RIGHT) # packs widget

def read_scales():
    print("The number of Customers selected is %d" %(cust.get()))
    print("The Number of floors selected is %d" %(floor.get()))

b=Button(root,text="Run Elevator",command=read_scales) # button to read values
b.pack(side="bottom")

#cust = Scale(root, from_=0, to=100, orient=VERTICAL, label = 'Number of Customers')
#cust.grid(column=0, row=1)
#print cust.get()

#fl = Scale(root, from_=0, to=200, orient=VERTICAL, label='Number of Floors')
#fl.grid(column=2, row=1)
#print (fl.get())

button = ttk.Button(text='Okay')

mainloop()