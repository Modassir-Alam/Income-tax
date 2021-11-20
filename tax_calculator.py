from tkinter import*
from tkinter import font
#creating tkinter window
root=Tk()
root.title("Income Tax Calculator")  #giving title 
root.geometry('600x400')
root.configure(background='cadetblue4')
root.resizable(width=False, height=False) #disabled the resizabilty option as per choice

#created heading inside windows and set their dimension and position
lbl_heading=Label(root,text='Income Tax Calculator',bg='dodgerblue', font=('Helvetica',16)).place(x=200,y=30)

#mentioned entry box name and its dimension ,font style and position
income_lbl=Label(root, text='Annual Income : ',bg='light green', font=('Times roman', 15)).place(x=40,y=100)
##
#created entry box for taking values
income_entry=Entry(root,width=30,bd=3,font=20)
income_entry.place(x=200,y=100)


#mentioned other entry box namne and its dimension,font style and position
tax_lbl=Label(root, text='Tax(%) : ',bg='light green',font=('Times roman', 15))
tax_lbl.place(x=90,y=150)
##
#created another entry box for taking values
tax_entry=Entry(root,width=30,bd=3,font=20)
tax_entry.place(x=200,y=150)

#function for calculating value
def cal():
    income_val=int(income_entry.get())
    tax_val=int(tax_entry.get())
    total=(income_val*tax_val)/100
    lbl=Label(root,text=f"Total TAX you have to pay is : {total}",font=50,bg='gold1')
    lbl.place(x=150,y=300)

########

def clearAll():
    # deleting the content from the entry box 
    income_entry.delete(0, END)
    
    tax_entry.delete(0, END)


#button for calculation
cal_btn=Button(root, text='Calulate',bg='white',bd=5,width=8, command=cal)
cal_btn.place(x=400,y=200)

# Create a Clear Button
clear = Button(root, text = "Clear", fg = "Black",bg = "light blue",bd=5,width=8,command = clearAll) 
clear.place(x=210,y=200)


# Button for closing
exit_button = Button(root, text="Exit",font='Arial 10',bg='white',
bd=5,width=8, command=root.destroy)
exit_button.place(x=120,y=200)

root.mainloop()