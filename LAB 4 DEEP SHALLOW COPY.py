class Employee:
    def __init__(self, name=None, dept=None, salary=0, service_years=0):
        # Parameterless constructor
        if name is None:
            self.name = ""
            self.dept = ""
            self.salary = 0
            self.service_years = 0
        else:
            # Parameterized constructor
            self.name = name
            self.dept = dept
            self.salary = salary
            self.service_years = service_years

    def input(self):
        # Input method to take user input for employee details
        self.name = input("Enter name: ")
        self.dept = input("Enter department: ")
        self.salary = float(input("Enter salary: "))
        self.service_years = float(input("Enter period of service in years: "))

    def show(self):
        # Show method to display employee details
        print(f"Name: {self.name}")
        print(f"Department: {self.dept}")
        print(f"Salary: {self.salary}")
        print(f"Period of service: {self.service_years} years")

    def copy(self):
        # Deep copy method to create a copy of an employee object
        return Employee(self.name, self.dept, self.salary, self.service_years)


# Main execution
emp1 = Employee()
emp1.show()  # Show default values (empty)

emp2 = Employee()
emp2.input()  # Input details for emp2
emp2.show()  # Show details of emp2

emp3 = emp2.copy()  # Create a copy of emp2
emp3.show()  # Show details of the copied employee

emp4 = Employee()
emp4.input()  # Input details for emp4
emp4.show()  # Show details of emp4
