
#                                 PROJECT 2  CALCULATOR
from tkinter import *
from tkinter import ttk, Entry, StringVar, DoubleVar
from tkinter.messagebox import showinfo,showerror,showwarning,askokcancel
from tkinter.scrolledtext import ScrolledText
from tkinter.colorchooser import askcolor
root=Tk()
root.title("CALCULATOR")
root.config(bg="black")
root.geometry("460x685")
root.resizable(False,False)
root.attributes('-alpha',1)

data=''
def get_data_from_number(value):
    global data
    data=data+str(value)
    var.set(data)
def clear():
    global data
    data=''
    var.set(data)
def equal_data():
    global data
    try:
        total=str(eval(data))
        var.set(total)
        data = ''
    except:
        var.set("ERROR")



var=StringVar()
label1=Label(root,text="Calculator",relief=SUNKEN,font=("Arial",45,"bold"),bg="green")
label1.place(x=50,y=20,height=85,width=350)

entry1=Entry(root,font=("Arial",20,"bold"),relief=SUNKEN,bg="green",bd=8,textvariable=var)
entry1.place(x=20,y=130,height=85,width=420)

#=======================================================================================================================================================
# button 1
button_1=Button(root,text="1",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number(1))
button_1.place(x=20,y=220,height=85,width=105)
#=======================================================================================================================================================
# button 2
button_2=Button(root,text="2",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number(2))
button_2.place(x=125,y=220,height=85,width=105)
#=======================================================================================================================================================
# button 3
button_3=Button(root,text="3",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number(3))
button_3.place(x=230,y=220,height=85,width=105)
#=======================================================================================================================================================
# button4
button_plus=Button(root,text="+",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number("+"))
button_plus.place(x=335,y=220,height=85,width=105)
#=======================================================================================================================================================
# button 5
button_4=Button(root,text="4",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number(4))
button_4.place(x=20,y=305,height=85,width=105)
#=======================================================================================================================================================
# button 6
button_5=Button(root,text="5",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number(5))
button_5.place(x=125,y=305,height=85,width=105)
#=======================================================================================================================================================
# button 7
button_6=Button(root,text="6",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number(6))
button_6.place(x=230,y=305,height=85,width=105)
#=======================================================================================================================================================
# button 8
button_minus=Button(root,text="-",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number("-"))
button_minus.place(x=335,y=305,height=85,width=105)
#=======================================================================================================================================================
# button 9
button_7=Button(root,text="7",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number(7))
button_7.place(x=20,y=390,height=85,width=105)
#=======================================================================================================================================================
# button 10
button_8=Button(root,text="8",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number(8))
button_8.place(x=125,y=390,height=85,width=105)

#=======================================================================================================================================================
# button 11
button_9=Button(root,text="9",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number(9))
button_9.place(x=230,y=390,height=85,width=105)
#=======================================================================================================================================================
# button 12
button_multiple=Button(root,text="*",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number("*"))
button_multiple.place(x=335,y=390,height=85,width=105)
#=======================================================================================================================================================
# button 13
button_dot=Button(root,text=".",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number("."))
button_dot.place(x=20,y=475,height=85,width=105)
#=======================================================================================================================================================
# button 14
button_0=Button(root,text="0",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number(0))
button_0.place(x=125,y=475,height=85,width=105)

#=======================================================================================================================================================
# button 15
button_clear=Button(root,text="clear",relief=SUNKEN,font=("Arial",30,"bold"),command=clear)
button_clear.place(x=230,y=475,height=85,width=105)
#=======================================================================================================================================================
# button 16
button_div=Button(root,text="/",relief=SUNKEN,font=("Arial",45,"bold"),command=lambda : get_data_from_number("/"))
button_div.place(x=335,y=475,height=85,width=105)

button_equal=Button(root,text="=",relief=SUNKEN,font=("Arial",45,"bold"),command=equal_data)
button_equal.place(x=20,y=560,height=85,width=420)

root.mainloop()
