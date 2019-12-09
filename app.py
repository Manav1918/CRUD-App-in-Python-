from tkinter import *
from crudAppMethods import crudApp
class App(crudApp):
    def __init__(self):
        super().__init__()  # calling init method of crudApp
#===========window design
        self.win = Tk()
        self.win.geometry('630x300')
        self.win.title('CRUD App Designed by: CID')
        self.win.resizable(0,0)
        try:self.win.wm_iconbitmap("icon.ico")
        except:pass

#=====================listbox to show etails
        self.labels =['StudentID','StudentName','StudentMobile','StudentEmail','StudentAddress']
        for btn in range(5):
            if btn<=2:
                lbtn = Label(text=self.labels[btn],font=('impact',10),fg='red').place(x=btn*90,y=5)
            else:
                lbtn = Label(text=self.labels[btn],font=('impact',10),fg='red').place(x=btn*105,y=5)
        self.details = Listbox(self.win,width=100,height=15,
                               selectmode=SINGLE,bg='light gray')
        
        self.details.place(x=0,y=25)
        
        self.scrollbar = Scrollbar(self.win,orient=VERTICAL)
        
        self.scrollbar.config(command=self.details.yview)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.details.config(yscrollcommand=self.scrollbar.set)
        #=======DISPLAY BUTTON
        self.displayBtn = Button(self.win,text='Display',bg='black',
                                 fg='white',width=20,command=self.showAll)
        self.displayBtn.place(x=20,y=275)
        #=======UPDATE BUTTON
        self.updateBtn = Button(self.win,text='Update',bg='black',
                                 fg='white',width=20,command=lambda:self.newWindow('u'))
        self.updateBtn.place(x=160,y=275)

        #=======DELETE BUTTON
        self.deleteBtn = Button(self.win,text='Delete',bg='black',
                                 fg='white',width=20,command=self.delete)
        self.deleteBtn.place(x=300,y=275)

        #=======INSERT BUTTON                                               #completed
        self.insertBtn = Button(self.win,text='Insert',bg='black',
                                 fg='white',width=20,command=lambda:self.newWindow('i'))
        self.insertBtn.place(x=440,y=275)

        self.win.mainloop()
#======================methods========================================
#====================== show all form database
    def showAll(self):
        a = self.displayAll()
        self.details.delete(0,END)  #firstly delete texts in listbox
        for c,o,l,u,m in a:
            
            self.details.insert(END,c+'  '*7+o+'  '*7+str(l)+'  '*7+u+'  '*7+m)
        #=================color change of all items in list
        for i in range(self.details.size()):
            if i%2!=0:
                self.details.itemconfig(i,bg='sky blue')
            else:
                self.details.itemconfig(i,bg='light green')
        
#=====================show selected items in listbox
    def selected(self):
        self.items= self.details.curselection()
        for items in self.items:
            self.data = (self.details.get(items)).split('  '*7)   # GET SELECTED LIST ITEMS
        self.data[2]= int(self.data[2])
        print('from selected: ',self.data)
        return self.data
        
#=====================Top level================================
    def newWindow(self,*args):
        self.top = Toplevel(self.win)
        self.top.geometry('630x300')
        self.top.title('Update data ')
        self.top.resizable(0,0)
        
        for i in args:
            if i=='u':
                self.forUpdate()
            elif i=='i':
                self.forInsert()

        self.top.mainloop()
    #============== gui for update function
    def forUpdate(self):
            self.e = [0,0,0,0,0,0]
            self.data = self.selected()
            self.ulabel = Label(self.top,text="UPDATE",font=('impact',20),fg='blue').pack(side=TOP,anchor=N)
            #==================== make labels for table column names
            for lbl in range(1,6):
                  lbl = Label(self.top,text=self.labels[lbl-1],font=('impact',10),fg='blue').place(x=20,y=lbl*50)
            #==================== make Entry box for table row data to change
            try:
                for lbl in range(1,6):
                    if lbl==1:
                        self.e[lbl] = Entry(self.top,font=('calibri',10),fg='red')
                        self.e[lbl].place(x=150,y=lbl*50)
                        self.e[lbl].insert(0,self.data[lbl-1])
                        self.e[lbl].config(state='readonly')
                    else:
                        self.e[lbl] = Entry(self.top,font=('calibri',10),fg='red')
                        self.e[lbl].place(x=150,y=lbl*50)
                        self.e[lbl].insert(0,self.data[lbl-1])
            except: pass
            self.submit = Button(self.top,text='Update',width=20,bg='green',fg='white',command=self.update)
            self.submit.pack(side=BOTTOM,anchor=S)
    #=============== gui for insert function
    def forInsert(self):
            self.e = [0,0,0,0,0,0]
            self.ulabel = Label(self.top,text="INSERT",font=('impact',20),fg='blue').pack(side=TOP,anchor=N)
            #==================== make labels for table column names
            for lbl in range(1,6):
                  lbl = Label(self.top,text=self.labels[lbl-1],font=('impact',10),fg='blue').place(x=20,y=lbl*50)
            #==================== make Entry box for table row data to change
            try:
                for lbl in range(1,6):
                    self.e[lbl] = Entry(self.top,font=('calibri',10),fg='red')
                    self.e[lbl].place(x=150,y=lbl*50)
            except: pass
            #==========insert button to enter data in database
            self.submit = Button(self.top,text='Insert',width=20,bg='green',fg='white',command=self.insert)
            self.submit.pack(side=BOTTOM,anchor=S)









    
if __name__== "__main__":
    
    App()
