class Person:

    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)

    def doubleage(self):
        return self.doubletheage(self.age)
    
    # check better the difference among class, instnce and static methods
    # check decorators
    @staticmethod
    def doubletheage(age):
        return age * 2


class Employee(Person):

    def __init__(self, first, last, age, staffnumber):
        super().__init__(first, last, age)
        self.staffnumber = staffnumber

    def __str__(self):
        return super().__str__() + ", " + str(self.staffnumber)

    # Example of a method that changes an attribute of the class Employee
    def fired(self):
        self.staffnumber = self.staffnumber - 1 


x = Person("Marge", "Simpson", 52)
y = Employee("Homer", "Simpson", 28, 1000)
z = Employee("Bart", "Simpson", 10, 1001)

people = [x,y,z]
employees = [y,z]

print(x.doubletheage(x.age))
print(x.doubleage())
print(y.doubleage())

# check the employee number
for e in employees:
    print(e)

# A person gets hired
for e in employees:
    e.fired()

# check the employee number again
for e in employees:
    print(e)
