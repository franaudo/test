class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

# Employee is a sub-class of Person and adds the attribute staffnumber
class Employee(Person):

    def __init__(self, first, last, staffnum):
        # Person.__init__(self,first, last) # this invokes the __init__method of the Person class
        # super(Employee,self).__init__(first, last) # same
        super().__init__(self,first, last) # same but only for python 3
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber


x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())
