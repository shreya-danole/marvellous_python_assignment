# access specifier

class Employee:
    def __init__(self,A,B,C):
        self.Name = A       #public
        self._department = B     #protected
        self.__Salary = C   #private

    def display(self):
        print(self.Name)
        print(self._department)
        print(self.__Salary)
        
obj = Employee('Rahul',24,89)
obj.display()

print(obj.Name)
print(obj._department)
# print(obj.__Salary)    # private are not accessable outside
