from tkinter import *
from back import data
import os
datas=data()
def view_val():
    list1.delete(0,END)
    for i in datas.view():
        list1.insert(END,i)
def insert_val():
    datas.insert(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get())
    list1.delete(0,END)
    list1.insert(END,e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get())
def update_val():
    datas.update(ins[0],e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get())
    list1.delete(0,END)
    list1.insert(END,e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get())
def search_val():
    list1.delete(0,END)
    for i in datas.search(location=e1_val.get(),weather=e2_val.get(),time=e3_val.get()):
        list1.insert(END,i)
def store():
    if os.path.exists("..\da.txt"):
        os.remove("..\da.txt")
    liss=['id','place','weather','time','status']
    with open("..\da.txt","a+") as dt:
        for i in liss:
            dt.write(str(i))
            if not i=='status':
                dt.write(",")
        dt.write("\n")
    for i in datas.view():
        lis=[]
        for j in i:
            lis.append(j)
        with open("..\da.txt","a+") as dt:
            for k in range(len(lis)):
                if not k==0:
                    dt.write('"')
                dt.write(str(lis[k]))
                if not k==0:
                    dt.write('"')
                if not 4==k:
                    dt.write(",")
            dt.write("\n")
            lis=[]
            

def get_selected(event):
    try:
        global ins
        index=list1.curselection()[0]
        ins=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,ins[1])
        e2.delete(0,END)
        e2.insert(END,ins[2])
        e3.delete(0,END)
        e3.insert(END,ins[3])
        e4.delete(0,END)
        e4.insert(END,ins[4])
    except IndexError:
        pass
    
def delete_val():
    datas.delete(ins[0])

window=Tk()
window.title("VTG")
l1=Label(window,text="Location")
l1.grid(row=0,column=0)
l2=Label(window,text="Weather")
l2.grid(row=0,column=2)
l3=Label(window,text="Time")
l3.grid(row=1,column=0)
l4=Label(window,text="Status")
l4.grid(row=1,column=2)
e1_val=StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)
e2_val=StringVar()
e2=Entry(window,textvariable=e2_val)
e2.grid(row=0,column=3)
e3_val=StringVar()
e3=Entry(window,textvariable=e3_val)
e3.grid(row=1,column=1)
e4_val=StringVar()
e4=Entry(window,textvariable=e4_val)
e4.grid(row=1,column=3)
list1=Listbox(window,height=7,width=35)
list1.grid(row=2,column=0,rowspan=8,columnspan=2)
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb1.get())
sb1.configure(command=list1.yview)
b1=Button(window,text="INSERT",width=10,command=insert_val)
b1.grid(row=2,column=3)
b2=Button(window,text="UPDATE",width=10,command=update_val)
b2.grid(row=3,column=3)
b3=Button(window,text="DELETE",width=10,command=delete_val)
b3.grid(row=4,column=3)
b4=Button(window,text="VIEWALL",width=10,command=view_val)
b4.grid(row=5,column=3)
b5=Button(window,text="SEARCH",width=10,command=search_val)
b5.grid(row=6,column=3)
b6=Button(window,text="CANCEL",width=10,command=exit)
b6.grid(row=7,column=3)
b7=Button(window,text="STORE",width=10,command=store)
b7.grid(row=8,column=3)
list1.bind('<<ListboxSelect>>',get_selected)
window.mainloop()
