from tkinter import *

root = Tk()
root.title("Calculadora simples")

def btn_add():
    global stack_val, last_btn
    stack_val += int(txtbox.get())
    txtbox.delete(0, END)
    last_btn = "+"

def btn_sub():
    global stack_val, last_btn
    stack_val -= int(txtbox.get())
    txtbox.delete(0, END)
    last_btn = "-"

def btn_calc(symbol):
    global stack_val, last_btn
    if (last_btn == "+" or last_btn == " ") and symbol == "+":
        stack_val += int(txtbox.get())
        txtbox.delete(0, END)
        last_btn = "+"
    elif (last_btn == "+" or last_btn == " ") and symbol == "-":
        stack_val += int(txtbox.get())
        txtbox.delete(0, END)
        last_btn = "-"
    elif last_btn == "-" and symbol == "-":
        stack_val -= int(txtbox.get())
        txtbox.delete(0, END)
        last_btn = "-"
    elif last_btn == "-" and symbol == "+":
        stack_val -= int(txtbox.get())
        txtbox.delete(0, END)
        last_btn = "+"

def btn_click(num):
    atual = txtbox.get()
    txtbox.delete(0, END) # pra n repetir as substrings
    txtbox.insert(0, str(atual) + str(num))

def btn_clear():
    global stack_val, last_btn
    txtbox.delete(0, END)
    stack_val = 0 
    last_btn = " "

def btn_eq():
    global stack_val, last_btn
    if last_btn != " ":
        if last_btn == "+":
            stack_val += int(txtbox.get())
        elif last_btn == "-":
            stack_val -= int(txtbox.get())
        txtbox.delete(0, END)
        txtbox.insert(0, str(stack_val))
        stack_val = 0
        last_btn = " "
    else:
        pass

stack_val = 0
last_btn  = " "

txtbox = Entry(root, width=35, borderwidth=5)
txtbox.grid(row=0,column=0, columnspan=3)

btn1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_click(1))
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_click(2))
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_click(3))
btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_click(4))
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_click(5))
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_click(6))
btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_click(7))
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_click(8))
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_click(9))
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_click(0))
btnadd = Button(root, text="+",     padx=40, pady=20, command=lambda: btn_calc("+"))
btnsub = Button(root, text="-",     padx=40, pady=20, command=lambda: btn_calc("-"))
btneq  = Button(root, text="=",     padx=40, pady=20, command=lambda: btn_eq() )
btncls = Button(root, text="limpar",padx=75, pady=20, command=lambda: btn_clear())

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)
btn0.grid(row=4, column=1)
btnadd.grid(row=4, column=0)
btnsub.grid(row=4, column=2)
btneq.grid( row=5, column=2)
btncls.grid(row=5, column=0, columnspan=2)

root.mainloop()