class Student:
    # Class variable
    school_name = "Green Valley High School"

    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"School Name: {Student.school_name}")


# Creating student objects
student1 = Student("ABC", 101)
student2 = Student("PQR", 102)

# Display details
print("Before changing school name:")
student1.display_details()
student2.display_details()

# Change school name using class name
Student.school_name = "Riverdale Public School"

# Display details again to show updated school name
print("\nAfter changing school name:")
student1.display_details()
student2.display_details()
