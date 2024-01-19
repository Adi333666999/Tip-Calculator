from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Tip Calculator by Aditya Patil")
root.geometry("830x700+50+2")
f = ("Century", 30)
fo = ("Century", 30, "bold")

titleLabel = Label(root, text = "TIP CALCULATOR", font = fo)
titleLabel.place(x = 240, y = 1)

billLabel = Label(root, text = "Bill Amount: ", font = f)
billLabel.place(x = 10, y = 65)
billEntry = Entry(root, font = f)
billEntry.place(x = 300, y = 65)

tipLabel = Label(root, text = "Tip(%): ", font = f)
tipLabel.place(x = 10, y = 155)
tipEntry = Entry(root, font = f)
tipEntry.place(x = 300, y = 155)

noLabel = Label(root, text = "No of People: ", font = f)
noLabel.place(x = 10, y = 250)
noEntry = Entry(root, font = f)
noEntry.place(x = 300, y = 250)

def compute():
	bill = billEntry.get()
	tip = tipEntry.get()
	no = noEntry.get()

	if not bill:
		showerror("CAUTION", "Enter Amount!!!")
	elif not all(char.isdigit() or char == "." for char in bill):
        	showerror("CAUTION", "Enter Amount!!!")
	elif int(bill) < 0:
        	showerror("CAUTION", "Amount cannot be negative!!!")
	elif not bill.isdigit():
        	showerror("CAUTION", "Enter only Amount!!!")	
	elif not tip:
		showerror("CAUTION", "Enter Tip Amount!!!")
	elif not all(char.isdigit() or char == "." for char in tip):
        	showerror("CAUTION", "Enter Tip Amount!!!")
	elif int(tip) < 0:
        	showerror("CAUTION", " Tip Amount cannot be negative!!!")
	elif not tip.isdigit():
        	showerror("CAUTION", "Enter only Tip Amount!!!")
	if not no:
		showerror("CAUTION", "Enter No of People!!!")
	elif not all(char.isdigit() or char == "." for char in no):
        	showerror("CAUTION", "Enter No of People!!!")
	elif int(no) < 0:
        	showerror("CAUTION", "No of People cannot be negative!!!")
	elif not no.isdigit():
        	showerror("CAUTION", "Enter only No of People!!!")	
	else:
		try:
			BillEntry = float(bill)
			TipEntry = float(tip)
			NoEntry = float(no)
			tip_amount = "\u20B9" + str((((BillEntry * TipEntry) / 100) * NoEntry) / NoEntry)
			total_amount = "\u20B9" + str(((BillEntry * TipEntry) / 100) + BillEntry)
			tipLabel.configure(text = tip_amount)
			tatLabel.configure(text = total_amount)
		except ValueError:
			showerror("ERROR", "Invalid input")

tpLabel = Label(root, text= "Tip amount: ", font = f)
tpLabel.place(x = 10, y = 450)
tipLabel = Label(root, text = " ", font = f)
tipLabel.place(x = 400, y = 450)

ttLabel = Label(root, text = "Total Amount: ", font = f)
ttLabel.place(x = 10, y = 550)
tatLabel = Label(root, text = " ", font = f)
tatLabel.place(x = 400, y = 550)

b = Button(root, text = "Submit", font = f, command = compute)
b.place(x = 320, y = 350)


root.mainloop()