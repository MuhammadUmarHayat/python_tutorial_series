class Student:
    #attribute initialization
    id=0
    name=""
    program=""

    def __init__(self,id,name,program):
        self.id=id
        self.name=name
        self.program=program
        
    def __str__(self):
        return f"{self.id} {self.name} {self.program}"
    
s=Student(1,"Ali","BSCS")
#print(s.id)
#print(s.name)
#print(s.program)
print(s)