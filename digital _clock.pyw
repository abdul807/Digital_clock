from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

def quit():
    window.destroy()


def clock_time():
    time=datetime.datetime.now()
    #time=(time.strftime('%H:%M:%S'))
    time=(time.strftime('%Y %m %d \n %H:%M:%S \n %A'))
    txt.set(time)
    window.after(1000,clock_time)

    

window=Tk()
window.title('Digital Clock')
window.attributes('-fullscreen',True)
window.configure(background='black')
window.after(1000,clock_time)



lbl=ttk.Label(window,text='created by Alabama',font=('arial',10,'bold'))
lbl.grid(row=0,column=0)

txt=StringVar()
fnt=font.Font(family='Helvetica', size=100,weight='bold',)
lbl=ttk.Label(window,textvariable=txt,font=fnt,background='black',foreground='white')
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)


#Label(window,text='\ntime clock :',bg='black',fg='white', font='none 25' ).grid(row=1,column=0,sticky=W)



window.mainloop()


