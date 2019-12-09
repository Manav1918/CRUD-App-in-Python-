from tkinter import *
import pymysql

class crudApp():
    
    def __init__(self):
#========== Now try to connect to database
        try:
                self.connection = pymysql.connect(host='localhost',user='root',db='crud_db')
        except:
                print("You are not connected to server(localhost)")
        else:
                print('Connected Successfully')
                self.cur = self.connection.cursor()              
                
#==========================insert into                          #completed             
    def insert(self):
        
        
        try:
            #get all values from entry boxes of update window
            self.val = []
            for i in range(1,6):
                self.val.append(self.e[i].get())
            self.val[0],self.val[2]= self.val[0].upper(),int(self.val[2])
            print('data inserted : ',self.val)
            #query=======================================
            self.query="""INSERT INTO student (sid,sname, smobile, semail, saddress)
                            VALUES (%s,%s,%s,%s,%s)"""
            self.cur.execute(self.query,self.val)
            self.connection.commit()
            self.showAll()
            # destroy insert window===================
            self.top.destroy()
        except Exception as ex:
            print(ex,'\n error in inserting values')
#=========================== Update to                             # completed
    def update(self):
        #get all values from entry boxes of update window
        self.val = []
        for i in range(2,6):
            self.val.append(self.e[i].get())
        
        #print('calling from update: ',self.data[0])
        self.val.append(self.data[0])
        self.val[1]= int(self.val[1])
        print('updated values: ',self.val)
        self.query="""UPDATE student SET sname=%s,
                        smobile=%s,semail=%s,saddress=%s WHERE sid=%s """
        self.cur.execute(self.query,self.val)
        self.connection.commit()
        self.showAll()
        # destroy update window===================
        self.top.destroy()
        
        
#========================== delete from                         # completed
    def delete(self):
        self.value = self.selected()
        
        self.query="DELETE FROM student WHERE sid = %s"
        self.val = self.value[0]#'%123%'
        print('deleted row with sid: ',self.val)
        self.cur.execute(self.query,self.val)
        self.connection.commit()
        self.showAll()
#==========================display all students details        
    def displayAll(self):
        self.data =[]
        self.query= "SELECT * FROM student "
        self.cur.execute(self.query)
        for data in self.cur:
                print(data)
                self.data.append(data)
        return self.data
                
        self.connection.commit()
        
    def closeDB(self):
        self.cur.close()
        self.connection.close()

if __name__=="__main__":
    app = crudApp()
    #a=app.displayAll()
    #print(a)

    app.closeDB()
