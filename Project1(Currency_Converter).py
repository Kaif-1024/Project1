import tkinter as tk 
from tkinter import *
import tkinter.messagebox

root = tk.Tk()
 
root.title("Currency Converter")

Tops = Frame(root, bg = 'black', pady=2, width=2000, height=100, relief='ridge', bd=10, cursor='dot')

Tops.grid(row=0, column=0)
 

 
headlabel = tk.Label(Tops, font=('lato black', 25, 'bold'), text='Currency Converter ',
                    bg='cyan', fg='black', anchor=N )
headlabel.grid(row=1, column=0)


variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
 
variable1.set("currency")
variable2.set("currency")

 
def CurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()
 
    from_currency = variable1.get()
    to_currency = variable2.get()
 
    if (Amount1_field.get().isalpha() or Amount1_field.get() == "" ):
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")
 
    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency form menu.")
 
    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))
 

def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)
 
 
CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "JPY", "ZAR", "SAR"]
 
root.configure(background='blue')
root.geometry("800x400")


Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2)
Label_1.grid(row=1, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="        Amount  :  ", bg="violet", fg="black")
label1.grid(row=2, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="    From Currency  :   \t\t\t", bg="red", fg="black")
label1.grid(row=3, sticky=SW)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="    To Currency  :  \t\t\t", bg="orange", fg="black")
label1.grid(row=4, column=0, sticky=SW)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="   Converted Amount  :  ", bg="YELLOW", fg="black")
label1.grid(row=8, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2)
Label_1.grid(row=5, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2)
Label_1.grid(row=7, column=0, sticky=W)
 
FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)
 
FromCurrency_option.grid(row=3, column=0, ipadx=60, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=60, sticky=E)
 
Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=45, ipady=5, sticky=E)
 
Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=40, sticky=E)
 
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="MEDIUMSEAGREEN", fg="white",
                 command=CurrencyConversion)
Label_9.grid(row=6, column=0)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2)
Label_1.grid(row=9, column=0, sticky=W)
 
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="black", fg="white",
                 command=clear_all)
Label_9.grid(row=10, column=0)
 
 
root.mainloop()

