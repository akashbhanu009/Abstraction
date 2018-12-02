from abc import *

class DBInterface(ABC):
    
    @abstractmethod
    def connect(self,text):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
class oracle(DBInterface):
    
    def connect(self,text):
        print("ORACLE DB connected...")
        print(text)
    def disconnect(self):
        print("ORACLE DB Disconnected....")

class sybase(DBInterface):
    def connect(self,text):
        print("Sybase DB connected....")
        print(text)
    def disconnect(self):
        print("Sybase DB disconnected....")

#with open("sample.txt",'r') as f:
#    pname=f.readlines()
Dbname=input("Enter any one DB name (case-sensetive)=> oracle or sybase\t=>")
#db=Dbname.lowercase()
classname=globals()[Dbname]
c=classname()
c.connect("Hello,this is the variable text")
c.disconnect()