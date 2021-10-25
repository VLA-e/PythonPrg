from tkinter import *
class But:
    def __init__(self,master,oper):
        self.oper=oper
        self.b=Button(text=self.oper)
        self.b.pack()
        self.b['command']=self.action
    def action(self):
        try:
            l['text']=eval(e1.get()+self.oper+e2.get())
        except:
            l['text']='ошибка ввода'
root=Tk()
e1=Entry(width=20); e1.pack()
e2=Entry(width=20); e2.pack()
l=Label(width=20);l.pack()
S=['+','-','*','/']
for i in S:
    But(root,i)
 
root.mainloop()
