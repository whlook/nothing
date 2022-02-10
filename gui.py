import tkinter as tk
import tkinter.filedialog as fd
import paiban

filename=""
def btn1_func():
    global filename
    filename=fd.askopenfilename()
    if filename != "":
            print(filename)
            label2.config(text=filename)
    else:
            print("no file choosen")

def btn2_func():
    exl=paiban.read_excel(filename,7)
    print(exl)
    paiban.online_operate(staffs=exl)

win=tk.Tk()
win.title(u"排班")
win.geometry("300x300+500+500")
label0=tk.Label(win,text="",fg="black",width=10,height=2)
label0.pack()
btn1=tk.Button(win,text="choose excel",command=btn1_func,width=10,height=5)
btn1.pack()
label2=tk.Label(win,text=filename,fg="black",wraplength=200,width=40,height=5)
label2.pack()
btn2=tk.Button(win,text="start",command=btn2_func,width=10,height=5)
btn2.pack()
label1=tk.Label(win,text="processing:",fg="black",width=20,height=5)
label1.pack()
win.mainloop()
