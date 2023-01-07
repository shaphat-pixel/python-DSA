#class
#a class contains the blue prints or the prototype from which the objects are bwign created.
#attributes are vraiables that belong to a class.
#Object is an entity that has a state and behaviour associated with it.
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

#print(Dog("Ama").speak())

class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My name is {}".format(self.idnumber))

#print(Person("Khal", "1231414").display())
#print(Person("khal", "17382713").details())

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        #invoking the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("my salary is {}".format(self.salary))
    
print(Employee("Hey", 134143, 3463, 'intern').details())





