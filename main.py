from tkinter import *
from tkinter import ttk

colors = {
    'Preta': "#3b3b3b",
    'Branca': "#FFFFFF",
    'Azul': "#1E90FF",
    'Cizenta': "#D3D3D3",
    'Laranja': "#FFA500"
    }

window = Tk()
window.title("Calculadora")
window.geometry("235x318")
window.config(bg=colors['Preta'])

# Frames
frame_window = Frame(window, width=235, height=50, bg=colors['Azul'])
frame_window.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)

# Botões 

button_1 = Button(frame_body, text="C", width=11, height=2, bg=colors['Cizenta'], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_1.place(x=0, y=0)
button_2 = Button(frame_body, text="%", width=5, height=2, bg=colors["Cizenta"], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_2.place(x=118, y=0)
button_3 = Button(frame_body, text="/", width=5, height=2, bg=colors['Laranja'], fg=colors['Branca'], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_3.place(x=177, y=0)

window.mainloop()

