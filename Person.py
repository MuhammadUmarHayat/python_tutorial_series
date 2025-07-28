class Person:
    #attribute intinailization
    name="" 
    age=0
    gender=""

    #assign values to the attributes

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def printPerson(self):
        print(self.name, self.age,self.gender)



class Teacher(Person):
    subject=""# initialize attribute
    def __init__(self, name, age, gender,subject):
        super().__init__(name, age, gender)
        self.subject=subject
    def printTeacher(self):
        print ("Welcome",self.name,self.age, self.gender,self.subject)


#p=Person("Umar",33,"male")
#p.printPerson()
t=Teacher("Imran",35,"Male","Machine Learning")
t.printTeacher()
