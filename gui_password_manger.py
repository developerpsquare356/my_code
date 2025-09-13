

===   Firstly create a user.json file which stores all the data of password and email  


################################        PASSWORD MANAGER GUI APP

from tkinter import *
from tkinter import ttk, Entry, StringVar, DoubleVar
from tkinter.messagebox import showinfo,showerror,showwarning,askokcancel
# from tkinter.scrolledtext import ScrolledText
# from tkinter.colorchooser import askcolor
import json

yellow="#f7f5dd"
# main window
root=Tk()
root.title("Prantik")
root.geometry('900x460')
root.config(bg=yellow)
root.resizable(width=False,height=False)
root.attributes('-alpha',1)
password_checker=True



def refresh():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

####   Function
def top():
    user=var1.get()
    email1=var2.get()
    password1=var3.get()
    new_data={user:{"Email":email1,"Password":password1}}

    if len(user)==0 or len(email1)==0 or len(password1)==0:
        showinfo(title="Prantik",message= "Sorry You Have Missed One Entry Box Please Fill it")
    else:
        try:
            with open("User_data.json", "r") as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open("User_data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("User_data.json", "w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:

            refresh()

    # label_success.config(text="You Have Successfully Registered ")

def search_data():
    user_name=var1.get()
    with open("User_data.json") as data_file:
        data = json.load(data_file)
        if user_name in data:
            user_email = data[user_name]["Email"]
            user_password = data[user_name]["Password"]
            showinfo(title="Wscube Tech",message=f'Email : {user_email} \n Password : {user_password}')





## background Image
canvas=Canvas(root,height=900,width=900,highlightthickness=0,bg=yellow)
photo=PhotoImage(file="Password-Manager.png") # take a photo for background
canvas.create_image( 0,0,image=photo,anchor=NW)
canvas.pack(fill="both",expand=True)

##   content like  user_name , email_address , password , sign_up , generate_password

user_name=Label(root,text="User Name :",font=("Arial",20,"bold","italic"))
user_name.place(x=50,y=150)


email_address=Label(root,text="Email Address :",font=("Arial",20,"bold","italic"))
email_address.place(x=50,y=200)

password=Label(root,text="Password :",font=("Arial",20,"bold","italic"))
password.place(x=50,y=250)

##   input field like  user_name , email_address , password , sign_up , generate_password

var1=StringVar()
var2=StringVar()
var3=StringVar()

entry1=Entry(root,font=("Arial",15,"bold","italic"),textvariable=var1)
entry1.place(x=300,y=150,height=35,width=400)
entry1.focus()


entry2=Entry(root,font=("Arial",15,"bold","italic"),textvariable=var2)
entry2.place(x=300,y=200,height=35,width=400)

entry3=Entry(root,font=("Arial",15,"bold","italic"),textvariable=var3,show="*")
entry3.place(x=300,y=250,height=35,width=400)

#  sign up button   and    create password option
sign_in_button=Button(root,text="Sign in",font=("Arial",15,"bold","italic"),command=top)
sign_in_button.place(x=350,y=300)

refresh_in_button=Button(root,text="search",font=("Arial",15,"bold","italic"),command=search_data)
refresh_in_button.place(x=50,y=300)

# label_success=Label(root,text="",font=("Arial",15,"bold","italic"),fg="blue")
# label_success.place(x=50,y=400)
root.mainloop()
