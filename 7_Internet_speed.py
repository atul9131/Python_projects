from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + " Mbps"
    up = str(round(sp.upload()/(10**6),3)) + " Mbps"
    lab_down.config(text = down)
    lab_up.config(text = up)

sp = Tk()
sp.title(' Internet Speed Meter ')
sp.geometry('500x650')
sp.config(bg = 'aqua')

lab = Label(sp, text='Internet Speed Test', font = ('time new roman', 30, 'bold'),bg='aqua')
lab.place(x=60,y=40,height=50,width=380)

lab = Label(sp, text='Download Speed', font = ('time new roman', 30, 'bold'))
lab.place(x=60,y=150,height=50,width=380)

lab_down = Label(sp, text='00', font = ('time new roman', 30, 'bold'))
lab_down.place(x=60,y=210,height=50,width=380)

lab = Label(sp, text='Upload Speed', font = ('time new roman', 30, 'bold'))
lab.place(x=60,y=350,height=50,width=380)

lab_up = Label(sp, text='00', font = ('time new roman', 30, 'bold'))
lab_up.place(x=60,y=410,height=50,width=380)

button = Button(sp, text='Check Speed', font = ('time new roman', 30, 'bold'),bg='gold', relief=RAISED , command=speedcheck)
button.place(x=60,y=550,height=50,width=380)

sp.mainloop()