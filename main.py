import math
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

program_models = [
    "Path Loss UMi-LOS",
    "Path Loss UMa-LOS",
    "Path Loss UMi-NLOS"
]

root = tk.Tk()
root.title("5G NR")

tabControl = ttk.Notebook(root)

firstTab = ttk.Frame(tabControl)
secondTab = ttk.Frame(tabControl)
thirdTab = ttk.Frame(tabControl)

tabControl.add(firstTab, text=program_models[0])
tabControl.add(secondTab, text=program_models[1])
tabControl.add(thirdTab, text=program_models[2])
tabControl.pack()

# D(2D)
firstTab_d_2d_frame = Frame(firstTab)
firstTab_d_2d_label = Label(firstTab_d_2d_frame, text="d(2D)")
firstTab_d_2d_entry = Entry(firstTab_d_2d_frame, width=50)
firstTab_d_2d_entry.bind("<FocusIn>", lambda args: firstTab_d_2d_entry.delete("0", "end"))
firstTab_d_2d_entry.insert(0, "Расстояние - в метрах") # (от 10 до 5000)

firstTab_d_2d_frame.pack(fill=X, padx=5, pady=5)
firstTab_d_2d_label.pack(side=LEFT)
firstTab_d_2d_entry.pack(fill=X, side=LEFT)

# H(BS)
firstTab_h_bs_frame = Frame(firstTab)
firstTab_h_bs_label = Label(firstTab_h_bs_frame, text="h(BS)")
firstTab_h_bs_entry = Entry(firstTab_h_bs_frame, width=50)
firstTab_h_bs_entry.bind("<FocusIn>", lambda args: firstTab_h_bs_entry.delete("0", "end"))
firstTab_h_bs_entry.insert(0, "Высота антенны - в метрах") #(до 150)

firstTab_h_bs_frame.pack(fill=X, padx=5, pady=5)
firstTab_h_bs_label.pack(side=LEFT)
firstTab_h_bs_entry.pack(fill=X, side=LEFT)

# H(UT)
firstTab_h_ut_frame = Frame(firstTab)
firstTab_h_ut_label = Label(firstTab_h_ut_frame, text="h(UT)")
firstTab_h_ut_entry = Entry(firstTab_h_ut_frame, width=50)
firstTab_h_ut_entry.bind("<FocusIn>", lambda args: firstTab_h_ut_entry.delete("0", "end"))
firstTab_h_ut_entry.insert(0, "Высота приёмника - в метрах")

firstTab_h_ut_frame.pack(fill=X, padx=5, pady=5)
firstTab_h_ut_label.pack(side=LEFT)
firstTab_h_ut_entry.pack(fill=X, side=LEFT)

# f(c)
firstTab_f_c_frame = Frame(firstTab)
firstTab_f_c_label = Label(firstTab_f_c_frame, text="f(c)")
firstTab_f_c_entry = Entry(firstTab_f_c_frame, width=50)
firstTab_f_c_entry.bind("<FocusIn>", lambda args: firstTab_f_c_entry.delete("0", "end"))
firstTab_f_c_entry.insert(0, "Частота - в Ггц") #(от 3.5 до 7.0)

firstTab_f_c_frame.pack(fill=X, padx=5, pady=5)
firstTab_f_c_label.pack(side=LEFT)
firstTab_f_c_entry.pack(fill=X, side=LEFT)

# First tab calculations
firstTab_calc_frame = Frame(firstTab)
firstTab_answer = StringVar()
firstTab_answer.set("Ответ будет показан здесь")
firstTab_answer_label = Label(firstTab_calc_frame, textvariable=firstTab_answer)


def first_tab_calculations():
    c = 3 * pow(10, 8)
    d2d = float(firstTab_d_2d_entry.get())
    h_bs = float(firstTab_h_bs_entry.get())
    h_ut = float(firstTab_h_ut_entry.get())
    f_c = float(firstTab_f_c_entry.get())
    d_bp = 4 * (h_bs - 1) * h_ut * f_c / c
    d3d = math.sqrt(pow(h_bs - h_ut, 2) + pow(d2d, 2))
    answer = 0

    if d2d < 0:
        messagebox.showwarning("Warning", "d(2d) не может быть отрицательным")
    if h_bs < 0:
        messagebox.showwarning("Warning", "h_bs не может быть отрицательным")
    if h_ut < 0:
        messagebox.showwarning("Warning", "h_ut не может быть отрицательным")
    if f_c < 0:
        messagebox.showwarning("Warning", "f_c не может быть отрицательным")

    if d2d < 10 or d2d > 5000:
        answer = "Неправильный d2d"
    elif d2d < d_bp:
        answer = 32.4 + math.log10(d3d) + 20 * math.log10(f_c) - 20
    else:
        answer = 32.4 + 40 * math.log10(d3d) + 20 * math.log10(f_c) - 9.5 * math.log10(pow(d_bp, 2) + pow((h_bs - 1) - h_ut, 2)) - 20
    firstTab_answer.set(answer)


firstTab_calc_button = Button(firstTab_calc_frame, text="Вычислить", command=first_tab_calculations)

firstTab_calc_frame.pack()
firstTab_calc_button.pack()
firstTab_answer_label.pack()

# D(2D)
secondTab_d_2d_frame = Frame(secondTab)
secondTab_d_2d_label = Label(secondTab_d_2d_frame, text="d(2D)")
secondTab_d_2d_entry = Entry(secondTab_d_2d_frame, width=50)
secondTab_d_2d_entry.bind("<FocusIn>", lambda args: secondTab_d_2d_entry.delete("0", "end"))
secondTab_d_2d_entry.insert(0, "Расстояние - в метрах (от 10 до 5000)")

secondTab_d_2d_frame.pack(fill=X, padx=5, pady=5)
secondTab_d_2d_label.pack(side=LEFT)
secondTab_d_2d_entry.pack(fill=X, side=LEFT)

# H(BS)
secondTab_h_bs_frame = Frame(secondTab)
secondTab_h_bs_label = Label(secondTab_h_bs_frame, text="h(BS)")
secondTab_h_bs_entry = Entry(secondTab_h_bs_frame, width=50)
secondTab_h_bs_entry.bind("<FocusIn>", lambda args: secondTab_h_bs_entry.delete("0", "end"))
secondTab_h_bs_entry.insert(0, "Высота антенны - в метрах") #(до 150)

secondTab_h_bs_frame.pack(fill=X, padx=5, pady=5)
secondTab_h_bs_label.pack(side=LEFT)
secondTab_h_bs_entry.pack(fill=X, side=LEFT)

# H(UT)
secondTab_h_ut_frame = Frame(secondTab)
secondTab_h_ut_label = Label(secondTab_h_ut_frame, text="h(UT)")
secondTab_h_ut_entry = Entry(secondTab_h_ut_frame, width=50)
secondTab_h_ut_entry.bind("<FocusIn>", lambda args: secondTab_h_ut_entry.delete("0", "end"))
secondTab_h_ut_entry.insert(0, "Высота приёмника - в метрах")

secondTab_h_ut_frame.pack(fill=X, padx=5, pady=5)
secondTab_h_ut_label.pack(side=LEFT)
secondTab_h_ut_entry.pack(fill=X, side=LEFT)

# f(c)
secondTab_f_c_frame = Frame(secondTab)
secondTab_f_c_label = Label(secondTab_f_c_frame, text="f(c)")
secondTab_f_c_entry = Entry(secondTab_f_c_frame, width=50)
secondTab_f_c_entry.bind("<FocusIn>", lambda args: secondTab_f_c_entry.delete("0", "end"))
secondTab_f_c_entry.insert(0, "Частота - в Ггц") # (от 3.5 до 7.0)

secondTab_f_c_frame.pack(fill=X, padx=5, pady=5)
secondTab_f_c_label.pack(side=LEFT)
secondTab_f_c_entry.pack(fill=X, side=LEFT)

# First tab calculations
secondTab_calc_frame = Frame(secondTab)
secondTab_answer = StringVar()
secondTab_answer.set("Ответ будет показан здесь")
secondTab_answer_label = Label(secondTab_calc_frame, textvariable=secondTab_answer)


def second_tab_calculations():
    c = 3 * pow(10, 8)
    d2d = float(secondTab_d_2d_entry.get())
    h_bs = float(secondTab_h_bs_entry.get())
    h_ut = float(secondTab_h_ut_entry.get())
    f_c = float(secondTab_f_c_entry.get())
    d_bp = 4 * h_bs * h_ut * f_c / c
    d3d = math.sqrt(pow(h_bs - h_ut, 2) + pow(d2d, 2))
    answer = 0

    if d2d < 0:
        messagebox.showwarning("Warning", "d(2d) не может быть отрицательным")
    if h_bs < 0:
        messagebox.showwarning("Warning", "h_bs не может быть отрицательным")
    if h_ut < 0:
        messagebox.showwarning("Warning", "h_ut не может быть отрицательным")
    if f_c < 0:
        messagebox.showwarning("Warning", "f_c не может быть отрицательным")

    if d2d < 10 or d2d > 5000:
        answer = "Неправильный d2d"
    elif d2d < d_bp:
        answer = 28.0 + 22 * math.log10(d3d) + 20 * math.log10(f_c) -25
    else:
        answer = 28.0 + 40 * math.log10(d3d) + 20 * math.log10(f_c) - 9 * math.log10(pow(d_bp, 2) + pow(h_bs - h_ut, 2)) - 25
    secondTab_answer.set(answer)


secondTab_calc_button = Button(secondTab_calc_frame, text="Вычислить", command=second_tab_calculations)

secondTab_calc_frame.pack()
secondTab_calc_button.pack()
secondTab_answer_label.pack()

# D(2D)
thirdTab_d_2d_frame = Frame(thirdTab)
thirdTab_d_2d_label = Label(thirdTab_d_2d_frame, text="d(2D)")
thirdTab_d_2d_entry = Entry(thirdTab_d_2d_frame, width=50)
thirdTab_d_2d_entry.bind("<FocusIn>", lambda args: thirdTab_d_2d_entry.delete("0", "end"))
thirdTab_d_2d_entry.insert(0, "Расстояние - в метрах") #(от 10 до 5000)

thirdTab_d_2d_frame.pack(fill=X, padx=5, pady=5)
thirdTab_d_2d_label.pack(side=LEFT)
thirdTab_d_2d_entry.pack(fill=X, side=LEFT)

# H(BS)
thirdTab_h_bs_frame = Frame(thirdTab)
thirdTab_h_bs_label = Label(thirdTab_h_bs_frame, text="h(BS)")
thirdTab_h_bs_entry = Entry(thirdTab_h_bs_frame, width=50)
thirdTab_h_bs_entry.bind("<FocusIn>", lambda args: thirdTab_h_bs_entry.delete("0", "end"))
thirdTab_h_bs_entry.insert(0, "Высота антенны - в метрах") # (до 150)

thirdTab_h_bs_frame.pack(fill=X, padx=5, pady=5)
thirdTab_h_bs_label.pack(side=LEFT)
thirdTab_h_bs_entry.pack(fill=X, side=LEFT)

# H(UT)
thirdTab_h_ut_frame = Frame(thirdTab)
thirdTab_h_ut_label = Label(thirdTab_h_ut_frame, text="h(UT)")
thirdTab_h_ut_entry = Entry(thirdTab_h_ut_frame, width=50)
thirdTab_h_ut_entry.bind("<FocusIn>", lambda args: thirdTab_h_ut_entry.delete("0", "end"))
thirdTab_h_ut_entry.insert(0, "Высота приёмника - в метрах")

thirdTab_h_ut_frame.pack(fill=X, padx=5, pady=5)
thirdTab_h_ut_label.pack(side=LEFT)
thirdTab_h_ut_entry.pack(fill=X, side=LEFT)

# f(c)
thirdTab_f_c_frame = Frame(thirdTab)
thirdTab_f_c_label = Label(thirdTab_f_c_frame, text="f(c)")
thirdTab_f_c_entry = Entry(thirdTab_f_c_frame, width=50)
thirdTab_f_c_entry.bind("<FocusIn>", lambda args: thirdTab_f_c_entry.delete("0", "end"))
thirdTab_f_c_entry.insert(0, "Частота - в Ггц") #(от 3.5 до 7.0)

thirdTab_f_c_frame.pack(fill=X, padx=5, pady=5)
thirdTab_f_c_label.pack(side=LEFT)
thirdTab_f_c_entry.pack(fill=X, side=LEFT)

# First tab calculations
thirdTab_calc_frame = Frame(thirdTab)
thirdTab_answer = StringVar()
thirdTab_answer.set("Ответ будет показан здесь")
thirdTab_answer_label = Label(thirdTab_calc_frame, textvariable=thirdTab_answer)


def third_tab_calculations():
    c = 3 * pow(10, 8)
    d2d = float(thirdTab_d_2d_entry.get())
    h_bs = float(thirdTab_h_bs_entry.get())
    h_ut = float(thirdTab_h_ut_entry.get())
    f_c = float(thirdTab_f_c_entry.get())
    d_bp = 4 * h_bs * h_ut * f_c / c
    d3d = math.sqrt(pow(h_bs - h_ut, 2) + pow(d2d, 2))
    answer = 0

    los_answer = 0
    if d2d < 0:
        messagebox.showwarning("Warning", "d(2d) не может быть отрицательным")
    if h_bs < 0:
        messagebox.showwarning("Warning", "h_bs не может быть отрицательным")
    if h_ut < 0:
        messagebox.showwarning("Warning", "h_ut не может быть отрицательным")
    if f_c < 0:
        messagebox.showwarning("Warning", "f_c не может быть отрицательным")

    if d2d < 10 or d2d > 5000:
        messagebox.showwarning("Warning", "Неправильный d2d")
        answer = "Неправильный d2d"
        thirdTab_answer.set(answer)
        pass
    else:
        los_answer = 35.3 * math.log10(d3d) + 22.4 + 21.3 * math.log10(f_c) - 0.3 * math.log10(h_ut - 1.5)

    nlos_answer = 0
    if d2d < d_bp:
        nlos_answer = 28.0 + 22 * math.log10(d3d) + 20 * math.log10(f_c)
    else:
        nlos_answer = 28.0 + 40 * math.log10(d3d) + 20 * math.log10(f_c) - 9 * math.log10(pow(d_bp, 2) + pow(h_bs - h_ut, 2))

    answer = max(nlos_answer, los_answer)
    thirdTab_answer.set(str(answer))



thirdTab_calc_button = Button(thirdTab_calc_frame, text="Вычислить", command=third_tab_calculations)

thirdTab_calc_frame.pack()
thirdTab_calc_button.pack()
thirdTab_answer_label.pack()


root.mainloop()