class Student:

    # Class Variable (common for all students)
    college_name = "ABC College"

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Classmethod – change college name for all students
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    # Staticmethod – check pass or fail
    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"

    # Instance Method – display details
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print("--------------------")


# Create 2 students
s1 = Student("Aishwarya", 101)
s2 = Student("Rahul", 102)

# Print details
s1.display()
s2.display()

# Change college using classmethod
Student.change_college("XYZ College")

print("After Changing College Name\n")

# Print again (both show new college)
s1.display()
s2.display()

# Static method usage
result1 = Student.is_pass(80)
result2 = Student.is_pass(30)

print("Marks 80:", result1)
print("Marks 30:", result2)