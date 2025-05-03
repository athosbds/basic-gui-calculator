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
window.geometry("235x310")
window.config(bg=colors['Preta'])

# Frames
frame_window = Frame(window, width=235, height=50, bg=colors['Azul'])
frame_window.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)

# BOTÕES - PRIMEIRA FILEIRA

button_1 = Button(frame_body, text="C", width=11, height=2, bg=colors['Cizenta'], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_1.place(x=0, y=0)
button_2 = Button(frame_body, text="%", width=5, height=2, bg=colors["Cizenta"], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_2.place(x=118, y=0)
button_3 = Button(frame_body, text="/", width=5, height=2, bg=colors['Laranja'], fg=colors['Branca'], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_3.place(x=177, y=0)

# BOTÕES - SEGUNDA FILEIRA

button_4 = Button(frame_body, text="7", width=5, height=2, bg=colors["Cizenta"], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_4.place(x=0, y=52)
button_5 = Button(frame_body, text="8", width=5, height=2, bg=colors["Cizenta"], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_5.place(x=59, y=52)
button_6 = Button(frame_body, text="9", width=5, height=2, bg=colors["Cizenta"], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_6.place(x=118, y=52)
button_7 = Button(frame_body, text="x", width=5, height=2, bg=colors['Laranja'], fg=colors['Branca'], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_7.place(x=177, y=52)

#BOTÕES - TERCEIRA FILEIRA

button_8 = Button(frame_body, text="4", width=5, height=2, bg=colors["Cizenta"], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_8.place(x=0, y=104)
button_9 = Button(frame_body, text="5", width=5, height=2, bg=colors["Cizenta"], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_9.place(x=59, y=104)
button_10 = Button(frame_body, text="6", width=5, height=2, bg=colors["Cizenta"], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_10.place(x=118, y=104)
button_11 = Button(frame_body, text="-", width=5, height=2, bg=colors['Laranja'], fg=colors['Branca'], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_11.place(x=177, y=104)

#BOTÕES - QUARTA FILEIRA

button_12 = Button(frame_body, text="1", width=5, height=2, bg=colors["Cizenta"], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_12.place(x=0, y=155)
button_13 = Button(frame_body, text="2", width=5, height=2, bg=colors["Cizenta"], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_13.place(x=59, y=155)
button_14 = Button(frame_body, text="3", width=5, height=2, bg=colors["Cizenta"], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_14.place(x=118, y=155)
button_15 = Button(frame_body, text="+", width=5, height=2, bg=colors['Laranja'], fg=colors['Branca'], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_15.place(x=177, y=155)

# BOTÕES - QUINTA FILEIRA

button_16 = Button(frame_body, text="0", width=11, height=2, bg=colors['Cizenta'], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_16.place(x=0, y=208)
button_17 = Button(frame_body, text=".", width=5, height=2, bg=colors["Cizenta"], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_17.place(x=118, y=208)
button_3 = Button(frame_body, text="/", width=5, height=2, bg=colors['Laranja'], fg=colors['Branca'], font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_3.place(x=177, y=208)





window.mainloop()

