# Import model
import os
import time
from tkinter import *
import datetime
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt
from tkinter import scrolledtext
import tkinter as tk

# Make log file
if not os.path.exists("log.rubik") :
    with open("log.rubik","w") as F:
        F.write("")


#Var
start = 0
stop = 0
_strat_or_stop = 'start'
_date = None
_started_first = False
_time = None


# Function
def date():
    y,m,d = datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day
    return f"{m}/{d}/{y}"


def _strat_btn():
    global _strat_or_stop,start,stop,_time,_started_first

    if _strat_or_stop == "start":
        _strat_or_stop = "stop"
        strat_btn.config(text="Stop")
        start = time.time()
        _started_first = True

    else:
        stop = time.time()
        _time = stop - start
        strat_btn.config(text="Start")
        _strat_or_stop="start"

        time_label.config(text=f"End : {_time:.3f}",height=3,width=23,font=("calibri 18 bold"))

def __strat_btn(event):
    global _strat_or_stop,start,stop,_time,_started_first

    if _strat_or_stop == "start":
        _strat_or_stop = "stop"
        strat_btn.config(text="Stop")
        start = time.time()
        _started_first = True

    else:
        stop = time.time()
        _time = stop - start
        strat_btn.config(text="Start")
        _strat_or_stop="start"

        time_label.config(text=f"End : {_time:.3f}",height=3,width=23,font=("calibri 18 bold"))


def _svae_btn():
    global _time,_started_first 
    if _started_first:
        y,m,d = datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day
        _date = f"{m}/{d}/{y}"
        with open("log.rubik","a") as F:
            F.write(f"{_date},{_time}\n")
        showinfo("Save !","It was saved correctly !")



def _log_btn():
    log = Tk()
    log.geometry("600x450")
    log.resizable(0,0)

    s = scrolledtext.ScrolledText(log,font=("calibri 18 bold"))
    s.pack(fill=BOTH,expand=1)

    with open("log.rubik") as F:
        read = F.read()
    read = read.strip()
    s.insert(1.0,read)
    log.mainloop()





# GUI
window = Tk()
window.geometry("400x700")
window.title("Rubik")
window.resizable(0,0)
window.config(bg='gray')

Label(window,text="Rubik",bg='gray',fg='white',font=("calibri 60 bold")).pack()


time_label = Label(window,text='welcome',height=3,width=23,fg="gray",font=("calibri 20 bold"))
time_label.pack(pady=50)


strat_btn = Button(window,
    width=15,
    text="Start",
    relief='flat',
    fg="gray",
    font=("calibri 30 bold"),
    activebackground="black",
    activeforeground="white",
    command=_strat_btn
    )
strat_btn.pack()


save_btn = Button(window,
    width=15,
    text="Save",
    relief='flat',
    fg="gray",
    font=("calibri 30 bold"),
    activebackground="black",
    activeforeground="white",
    command=_svae_btn
    )
save_btn.pack(pady=50)


log_btn = Button(window,
    width=15,
    text="Log",
    relief='flat',
    fg="gray",
    font=("calibri 30 bold"),
    activebackground="black",
    activeforeground="white",
    command=_log_btn
    )
log_btn.pack()

window.bind("<Key>",__strat_btn)

window.mainloop()
