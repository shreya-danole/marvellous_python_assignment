class Person:
    def __init__(self, A, B):
        print("Inside Person constructor")
        self.Name = A
        self.Age = B

class Teacher(Person):  # Teacher inherits from Person
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)  # Call base class constructor
        self.subject = subject
        self.salary = salary

    def display(self):
        print(f"Name: {self.Name}, Age: {self.Age}")
        print(f"Subject: {self.subject}, Salary: {self.salary}")

def main():
    obj = Teacher("Alice", 35, "Mathematics", 50000)
    obj.display()

if __name__ == "__main__":
    main()
