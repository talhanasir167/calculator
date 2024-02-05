from tkinter import ttk, Label, Frame, StringVar
from ttkthemes import ThemedTk

# Button Press
def btn_press(num):
    global eq_text
    eq_text = eq_text + str(num)
    eq_label.set(eq_text)

# Calculate input
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

# Clear the output
def clear_func():
    global eq_text
    eq_label.set("")
    eq_text = ""

# Main Window
window = ThemedTk(theme="yaru")
window.title("Basic Calculator")
window.geometry("480x400")

eq_text = ""
eq_label = StringVar()

label = Label(window, textvariable=eq_label, font=('Times New Roman', 20),
              bg="#FFFFFF", width=20, height=1)
label.pack()

frame = Frame(window)
frame.pack(pady=8)

# Specific Style for '=' button
button_height = 24

style = ttk.Style()
style.configure("TButtonCustom.TButton", padding=[3, button_height])

# Specific Style for '0' button
button_height = 24

style = ttk.Style()
style.configure("TButtonCustom2.TButton", padding=[28, 4])


# Buttons
btn_7 = ttk.Button(frame, text=7, width=3,
                   command=lambda: btn_press(7))
btn_7.grid(padx=3, pady=4, row=0, column=0)

btn_8 = ttk.Button(frame, text=8, width=3,
                   command=lambda: btn_press(8))
btn_8.grid(padx=3, pady=4, row=0, column=1)

btn_9 = ttk.Button(frame, text=9,  width=3,
                   command=lambda: btn_press(9))
btn_9.grid(padx=3, pady=4, row=0, column=2)

btn_4 = ttk.Button(frame, text=4,  width=3,
                   command=lambda: btn_press(4))
btn_4.grid(padx=3, pady=4, row=1, column=0)

btn_5 = ttk.Button(frame, text=5,  width=3,
                   command=lambda: btn_press(5))
btn_5.grid(padx=3, pady=4, row=1, column=1)

btn_6 = ttk.Button(frame, text=6, width=3,
                   command=lambda: btn_press(6))
btn_6.grid(padx=3, pady=4, row=1, column=2)

btn_1 = ttk.Button(frame, text=1, width=3,
                   command=lambda: btn_press(1))
btn_1.grid(padx=3, pady=4, row=2, column=0)

btn_2 = ttk.Button(frame, text=2, width=3,
                   command=lambda: btn_press(2))
btn_2.grid(padx=3, pady=4, row=2, column=1)

btn_3 = ttk.Button(frame, text=3, width=3,
                   command=lambda: btn_press(3))
btn_3.grid(padx=3, pady=4, row=2, column=2)

btn_0 = ttk.Button(frame, text=0, width=3,
                   command=lambda: btn_press(0), style='TButtonCustom2.TButton')
btn_0.grid(padx=3, pady=4, row=3, column=0, columnspan=2)

btn_plus = ttk.Button(frame, text='+', width=3,
                      command=lambda: btn_press('+'))
btn_plus.grid(padx=3, pady=4, row=0, column=3)

btn_minus = ttk.Button(frame, text='-', width=3,
                       command=lambda: btn_press('-'))
btn_minus.grid(padx=3, pady=4, row=1, column=3)

btn_multiply = ttk.Button(frame, text='*', width=3,
                          command=lambda: btn_press('*'))
btn_multiply.grid(padx=3, pady=4, row=4, column=0)

btn_divide = ttk.Button(frame, text='/', width=3,
                        command=lambda: btn_press('/'))
btn_divide.grid(padx=3, pady=4, row=4, column=1)

btn_equal = ttk.Button(frame, text='=', width=3,
                       command=calculate, style='TButtonCustom.TButton')
btn_equal.grid(padx=3, pady=4, row=2, rowspan=2, column=3)

btn_decimal = ttk.Button(frame, text='.', width=3,
                         command=lambda: btn_press('.'))
btn_decimal.grid(padx=3, pady=4, row=3, column=2)

btn_clear = ttk.Button(frame, text='Clear',
                       command=clear_func)
btn_clear.grid(padx=3, pady=4, row=4, column=2, columnspan=2)

btn_quit = ttk.Button(window, text="Quit",
           command=window.destroy)
btn_quit.pack(pady=6)


# Main Loop
window.mainloop()
