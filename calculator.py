from tkinter import *

def btn_press(num):
    global eq_text
    eq_text = eq_text + str(num)
    eq_label.set(eq_text)

def calculate():
    global eq_text
    try:
        result = str(eval(eq_text))
        eq_label.set(result)
        eq_text = result
    except SyntaxError:
        eq_label.set("Syntax Error")
        eq_text = ""
    except ZeroDivisionError:
        eq_label.set("Arithmetic Error")
        eq_text = ""

def clear_func():
    global eq_text
    eq_label.set("")
    eq_text = ""


window = Tk()
window.title("Custom Calculator")
window.geometry("500x500")

eq_text = ""
eq_label = StringVar()

label = Label(window, textvariable=eq_label, font=('consolas', 20), bg="#FFFFFF", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

btn_7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: btn_press(7))
btn_7.grid(row=0, column=0)

btn_8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: btn_press(8))
btn_8.grid(row=0, column=1)

btn_9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: btn_press(9))
btn_9.grid(row=0, column=2)

btn_4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: btn_press(4))
btn_4.grid(row=1, column=0)

btn_5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: btn_press(5))
btn_5.grid(row=1, column=1)

btn_6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: btn_press(6))
btn_6.grid(row=1, column=2)

btn_1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: btn_press(1))
btn_1.grid(row=2, column=0)

btn_2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: btn_press(2))
btn_2.grid(row=2, column=1)

btn_3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: btn_press(3))
btn_3.grid(row=2, column=2)

btn_0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: btn_press(0))
btn_0.grid(row=3, column=0)

btn_plus = Button(frame, text='+', height=4, width=9, font=35, command=lambda: btn_press('+'))
btn_plus.grid(row=0, column=3)

btn_minus = Button(frame, text='-', height=4, width=9, font=35, command=lambda: btn_press('-'))
btn_minus.grid(row=1, column=3)

btn_multiply = Button(frame, text='*', height=4, width=9, font=35, command=lambda: btn_press('*'))
btn_multiply.grid(row=2, column=3)

btn_divide = Button(frame, text='/', height=4, width=9, font=35, command=lambda: btn_press('/'))
btn_divide.grid(row=3, column=3)

btn_equal = Button(frame, text='=', height=4, width=9, font=35, command=calculate)
btn_equal.grid(row=3, column=2)

btn_decimal = Button(frame, text='.', height=4, width=9, font=35, command=lambda: btn_press('.'))
btn_decimal.grid(row=3, column=1)

btn_clear = Button(window, text='Clear', height=4, width=12, font=35, command=clear_func)
btn_clear.pack()

window.mainloop()
