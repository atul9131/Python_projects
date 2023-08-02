# Shutdown App using Python with GUI

from tkinter import *
import os

def restart():
    os.system('shutdown /r /t 1')
def restart_time():
    os.system('shutdown /r /t 1')
def logout():
    os.system('shutdown -1')
def shutdown():
    os.system('shutdown /s /t 1')



st = Tk()
st.title("Atul's Shutdown App")
st.geometry('500x500')
st.config(bg='turquoise')

r_button = Button(st, text='Restart',bg='black', foreground='turquoise', font=('Time New Roman', 20, 'bold',), relief=RAISED , cursor='plus', command=restart)
r_button.place(x=150 , y=60 , height=50, width=200)

rt_button = Button(st, text='Restart Time',bg='black', foreground='turquoise', font=('Time New Roman', 20, 'bold'), relief=RAISED , cursor='plus', command=restart_time)
rt_button.place(x=150 , y=160 , height=50, width=200)

lg_button = Button(st, text='Log-Out', bg='black', foreground='turquoise',font=('Time New Roman', 20, 'bold'), relief=RAISED , cursor='plus',command=logout)
lg_button.place(x=150 , y=260 , height=50, width=200)

st_button = Button(st, text='Shut Down',bg='black', foreground='turquoise', font=('Time New Roman', 20, 'bold'), relief=RAISED , cursor='plus' , command=shutdown)
st_button.place(x=150 , y=360 , height=50, width=200)


st.mainloop()
