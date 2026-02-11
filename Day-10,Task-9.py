class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Greater than comparison based on salary
    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.salary > other.salary
        return NotImplemented

    # Less than comparison based on salary
    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.salary < other.salary
        return NotImplemented


# Creating employee objects
e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

# Comparing employees
print(e1 > e2)  # False
print(e1 < e2)  # True
