class Employee:
    # Static variable to track total number of employees
    total_employees = 0

    def __init__(self, emp_id, emp_name, emp_designation):
        """
        Constructor to initialize employee details and increment the total employee count.
        """
        self.employee_id = emp_id
        self.name = emp_name
        self.designation = emp_designation
        Employee.total_employees += 1  # Increment total employees

    def display_employee_info(self):
        """
        Displays employee information.
        """
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")

    @staticmethod
    def display_total_employees():
        """
        Displays the total number of employees.
        """
        print(f"Total Employees: {Employee.total_employees}")

    def update_employee_info(self, emp_name, emp_designation):
        """
        Updates employee information.
        """
        self.name = emp_name
        self.designation = emp_designation


# Main program
if __name__ == "__main__":
    # Adding employees
    emp1 = Employee(1, "Sabahat", "Manager")
    emp2 = Employee(2, "Ahlam", "Developer")

    # Displaying employee information
    print("Employee 1 Info:")
    emp1.display_employee_info()
    print()

    print("Employee 2 Info:")
    emp2.display_employee_info()
    print()

    # Displaying total employees
    Employee.display_total_employees()
    print()

    # Updating Employee 1's info
    print("Updating Employee 1's info...")
    emp1.update_employee_info("Sabahat", "Senior Manager")
    emp1.display_employee_info()
    print()

    # Displaying total employees after update
    Employee.display_total_employees()
