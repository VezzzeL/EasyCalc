from math import sqrt, pow
import tkinter as tk


def add_num(num):
    value = res.get()
    if value == "0":
        value = value[1:]
    res.delete(0, tk.END)
    res.insert(0, value+num)


def add_opr(opr):
    value = res.get()
    if value[-1] in "+-*/":
        value = value[:-1]
    elif "+" in value or "-" in value or "*" in value or "/" in value:
        calculate()
        value = res.get()
    res.delete(0, tk.END)
    res.insert(0, value+opr)


def calculate():
    value = res.get()
    res.delete(0, tk.END)
    res.insert(0, eval(value))


def clear():
    res.delete(0, tk.END)
    res.insert(0, "0")


def make_operation_button(opr):
    return tk.Button(text=opr, bd=1, font=("Arial", 10), background="#D4E6F1", command=lambda: add_opr(opr))


def make_num_button(num):
    return tk.Button(text=num, bd=1, font=("Arial", 10), background="#D4E6F1", command=lambda: add_num(num))


def make_cal_button(opr):
    return tk.Button(text=opr, bd=1, font=("Arial", 10), background="#D4E6F1", command=calculate)


def make_clear_button(opr):
    return tk.Button(text=opr, bd=1, font=("Arial", 10), background="#D4E6F1", command=clear)


def clear_last_button():
    value = res.get()
    value = value[:-1]
    res.delete(0, tk.END)
    res.insert(0, value)


def take_root():
    value = res.get()
    value = sqrt(float(value))
    res.delete(0, tk.END)
    res.insert(0, value)


def take_pow2():
    value = res.get()
    value = pow(float(value), 2)
    res.delete(0, tk.END)
    res.insert(0, value)


calc = tk.Tk()

calc.title("Easy calc")
calc.geometry("203x303")
calc.resizable(False, False)
calc.iconphoto(False, tk.PhotoImage(file='IconMain.png'))
calc.config(bg="#ECF9FF")

res = tk.Entry(calc, justify=tk.RIGHT, font=("Arial", 12), width=12)
res.insert(0, "0")
res.grid(row=0, column=0, columnspan=4, stick="we", padx=10)


make_num_button("1").grid(row=1, column=0, stick="wens", padx=3, pady=3)
make_num_button("2").grid(row=1, column=1, stick="wens", padx=3, pady=3)
make_num_button("3").grid(row=1, column=2, stick="wens", padx=3, pady=3)
make_num_button("4").grid(row=2, column=0, stick="wens", padx=3, pady=3)
make_num_button("5").grid(row=2, column=1, stick="wens", padx=3, pady=3)
make_num_button("6").grid(row=2, column=2, stick="wens", padx=3, pady=3)
make_num_button("7").grid(row=3, column=0, stick="wens", padx=3, pady=3)
make_num_button("8").grid(row=3, column=1, stick="wens", padx=3, pady=3)
make_num_button("9").grid(row=3, column=2, stick="wens", padx=3, pady=3)
make_num_button("0").grid(row=4, column=0, stick="wens", padx=3, pady=3)
make_num_button(".").grid(row=4, column=1, stick="wens", padx=3, pady=3)

make_operation_button("+").grid(row=1, column=3, stick="wens", padx=3, pady=3)
make_operation_button("-").grid(row=2, column=3, stick="wens", padx=3, pady=3)
make_operation_button("*").grid(row=3, column=3, stick="wens", padx=3, pady=3)
make_operation_button("/").grid(row=4, column=2, stick="wens", padx=3, pady=3)

make_cal_button("=").grid(row=5, column=3, stick="wens", padx=3, pady=3)
make_clear_button("CE").grid(row=5, column=2, stick="wens", padx=3, pady=3)

clear_but = tk.Button(text="C", bd=1, font=("Arial", 10), background="#D4E6F1", command=lambda: clear_last_button())
clear_but.grid(row=5, column=1, stick="wens", padx=3, pady=3)

root_numb = tk.Button(text="sqrt", bd=1, font=("Arial", 10), background="#D4E6F1", command=lambda: take_root())
root_numb.grid(row=5, column=0, stick="wens", padx=3, pady=3)

product = tk.Button(text="x^2", bd=1, font=("Arial", 10), background="#D4E6F1", command=lambda: take_pow2())
product.grid(row=4, column=3, stick="wens", padx=3, pady=3)

calc.grid_columnconfigure(0, minsize=50)
calc.grid_columnconfigure(1, minsize=50)
calc.grid_columnconfigure(2, minsize=50)
calc.grid_columnconfigure(3, minsize=50)

calc.grid_rowconfigure(0, minsize=50)
calc.grid_rowconfigure(1, minsize=50)
calc.grid_rowconfigure(2, minsize=50)
calc.grid_rowconfigure(3, minsize=50)
calc.grid_rowconfigure(4, minsize=50)
calc.grid_rowconfigure(5, minsize=50)

calc.mainloop()
