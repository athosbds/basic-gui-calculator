from tkinter import *
from calc_logic import insert_value, calculate, clear
colors = {
    'Preta': "#3b3b3b",
    'Branca': "#FFFFFF",
    'Azul': "#1E90FF",
    'Cizenta': "#D3D3D3",
    'Laranja': "#FFA500"
    }

window = Tk()
window.title("Calculadora")
window.geometry("235x310")
window.config(bg=colors['Preta'])

text_var = StringVar()

# Frames
frame_window = Frame(window, width=235, height=50, bg=colors['Preta'])
frame_window.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)


# LABEL

layout_label = Label(frame_window, textvariable=text_var, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '), bg=colors['Preta'], fg=colors['Branca'])
layout_label.place(x=0, y=0)

def button(first_text, x, y, comando=None, largura=5):
    return Button(frame_body, text=first_text, width=largura, height=2, command=comando, bg=colors['Cizenta'] if first_text not in ['=', '+', 'x', '-', '÷'] else colors['Laranja'], fg=colors['Branca'] if first_text in ["=", "+", "-", "x", "÷"] else "black", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=x, y=y)


# BOTÕES - PRIMEIRA FILEIRA

button("C", 0, 0, comando=lambda: clear(text_var), largura=11)
button("%", 118, 0, comando=lambda: insert_value("%", text_var))
button("÷", 177, 0, comando=lambda: insert_value("÷", text_var))

# BOTÕES - SEGUNDA FILEIRA

button("7", 0, 52, comando=lambda: insert_value("7", text_var))
button("8", 59, 52, comando=lambda: insert_value("8", text_var))
button("9", 118, 52, comando=lambda: insert_value("9", text_var))
button("x", 177, 52, comando=lambda: insert_value("x", text_var))

#BOTÕES - TERCEIRA FILEIRA

button("4", 0, 104, comando=lambda: insert_value("4", text_var))
button("5", 59, 104, comando=lambda: insert_value("5", text_var))
button("6", 118, 104, comando=lambda: insert_value("6", text_var))
button("-", 177, 104, comando=lambda: insert_value("-", text_var))

#BOTÕES - QUARTA FILEIRA

button("1", 0, 155, comando=lambda: insert_value("1", text_var))
button("2", 59, 155, comando=lambda: insert_value("2", text_var))
button("3", 118, 155, comando=lambda: insert_value("3", text_var))
button("+", 177, 155, comando=lambda: insert_value("+", text_var))

# BOTÕES - QUINTA FILEIRA

button("0", 0, 208, comando=lambda: insert_value("0", text_var), largura=11)
button(".", 118, 208, comando=lambda: insert_value(".", text_var))
button("=", 177, 208, comando=lambda: calculate(text_var))


window.mainloop()

