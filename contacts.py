from tkinter import *
from new_db import Database 
from tkinter import messagebox
db= Database('F:/myfile/new_db.db')
win=Tk()
win.geometry('600x400')
win.title('Login from')
win.config(bg='#468906')
def sign_up():
    if ent_imail.get() == "" or ent_pass.get()=="":
        messagebox.showerror('Error','one of the fields is empty')
        return
    db.insert(ent_fname.get(),ent_lname.get(),ent_imail.get(),ent_pass.get())
    print('you are registered')
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_imail.delete(0,END)
    ent_pass.delete(0,END)
    crsr=ent_fname.focus_set()

def sign_in():
    if not ent_imail.get() and not ent_pass.get():
        messagebox.showerror('Error','one of the fields is empty')
        return
    serch=db.serch(ent_imail.get(),ent_pass.get())
    if serch:
        win.destroy()
        root= Tk()
        root.geometry("300x300")
        root.title("Welcome")
        root.configure(bg='#468906')
        for rec in serch:
         lbl_welcome = Label(root,text=f'Welcome {rec[1]} {rec[2]}',font='arial 15 bold',fg='white',bg='red').place(x=40,y=50)
    else:
        messagebox.showerror('Error','one or more filled in incorrectly')

#label=============
lbl_fname=Label(win,text='fname:',font='arial 13',bg='#4e0693',fg='white')
lbl_fname.place(x=25,y=25)
lbl_lname=Label(win,text='lname:',font='arial 13',bg='#4e0693',fg='white')
lbl_lname.place(x=25,y=85)
lbl_imail=Label(win,text='Email:',font='arial 13',bg='#4e0693',fg='white')
lbl_imail.place(x=25,y=145)
lbl_pass=Label(win,text='password:',font='arial 13',bg='#4e0693',fg='white')
lbl_pass.place(x=25,y=210)
lbl_setare=Label(win,text='*',font='arial 20',bg='#468906',fg='red')
lbl_setare.place(x=10,y=145)
lbl_setare1=Label(win,text='*',font='arial 20',bg='#468906',fg='red')
lbl_setare1.place(x=10,y=210)
#entry=================
ent_fname=Entry(win,font='arial 14')
ent_fname.place(x=85,y=25)
ent_lname=Entry(win,font='arial 14')
ent_lname.place(x=85,y=85)
ent_imail=Entry(win,font='arial 14')
ent_imail.place(x=82,y=145)
ent_pass=Entry(win,font='arial 14')
ent_pass.place(x=110,y=210)
#btn========================
btn_sign=Button(win,text='sign up',font='arial 13',bg='#4e0693',fg='white',command=sign_up)
btn_sign.place(x=150,y=300)
btn_sign1=Button(win,text='sign in',font='arial 13',bg='#4e0693',fg='white',command=sign_in)
btn_sign1.place(x=350,y=300)







win.mainloop()