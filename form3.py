from tkinter import*
from tkinter import messagebox

def add():
        #print("hello")
        #messagebox.showinfo("message","hello")
        a=int(num1.get())
        b=int(num2.get())
        c=int(num3.get())
        #print(a,b,c)
        s=a+b+c
        #print("sum is equal to:",s)
        messagebox.showinfo("sum",s)
        res.set(s)
    
win=Tk()
win.title("window apps")
win.geometry("400x400")
win.config(bg="cyan")
win.resizable(False,False)
    
lb1=Label(win,text="NUMBER1")
lb1.grid(row=0,column=0)
num1=StringVar()
tb1=Entry(win,textvariable=num1)
tb1.grid(row=0,column=1)
    
lb2=Label(win,text="NUMBER2")
lb2.grid(row=1,column=0)
num2=StringVar()
tb2=Entry(win,textvariable=num2)
tb2.grid(row=1,column=1)
    
lb3=Label(win,text="NUMBER3")
lb3.grid(row=2,column=0)
num3=StringVar()
tb3=Entry(win,textvariable=num3)
tb3.grid(row=2,column=1)
    
lb4=Label(win,text="Result")
lb4.grid(row=3,column=0)
res=StringVar()
tb4=Entry(win,textvariable=res)
tb4.grid(row=3,column=1)
    
btn=Button(win,text="Addition",command=add)
btn.grid(row=4,column=1)
    
