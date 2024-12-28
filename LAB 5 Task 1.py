# Base class for Employee
class Employee:
    def __init__(self, employeeID, name):
        """
        Constructor to initialize an Employee object with employee ID and name.
        :param employeeID: Unique ID for the employee
        :param name: Name of the employee
        """
        self.employeeID = employeeID  # Initialize employee ID
        self.name = name  # Initialize employee name

    def display(self):
        """
        Method to display employee information: ID and name.
        """
        print(f"Employee ID: {self.employeeID}")
        print(f"Employee name: {self.name}")


# Derived class for Manager, inherits from Employee
class Manager(Employee):
    def __init__(self, employeeID, name, department):
        """
        Constructor to initialize a Manager object with employee details and department.
        :param employeeID: Unique ID for the manager
        :param name: Name of the manager
        :param department: Department where the manager works
        """
        super().__init__(employeeID, name)  # Call the parent constructor to initialize employee details
        self.department = department  # Initialize department

    def get_department(self):
        """
        Method to get the manager's department.
        """
        print(f"Manager's department: {self.department}")

    def set_department(self, dep):
        """
        Method to set the manager's department.
        :param dep: Department name to set
        """
        self.department = dep

    def manage_team(self):
        """
        Method to simulate managing the team in the manager's department.
        """
        print(f"Managing the team in {self.department} department.")

    def assign_tasks(self):
        """
        Method to simulate assigning tasks in the manager's department.
        """
        print(f"Assigning the tasks in the {self.department} department.")


# Derived class for Intern, inherits from Employee
class Intern(Employee):
    def __init__(self, employeeID, name, supervisor, duration):
        """
        Constructor to initialize an Intern object with employee details, supervisor and duration.
        :param employeeID: Unique ID for the intern
        :param name: Name of the intern
        :param supervisor: Supervisor's name
        :param duration: Duration of the internship in months
        """
        super().__init__(employeeID, name)  # Call the parent constructor to initialize employee details
        self.supervisor = supervisor  # Initialize supervisor name
        self.duration = duration  # Initialize internship duration

    def track_progress(self):
        """
        Method to track the progress of the intern under the supervisor.
        """
        print(f"Tracking progress of intern under {self.supervisor} for {self.duration} months.")

    def report_activities(self):
        """
        Method to simulate the intern reporting activities to their supervisor.
        """
        print(f"Reporting activities to {self.supervisor} regularly.")


# Main execution begins here
if __name__ == "__main__":
    # Creating an instance of Manager with specific employee ID, name, and department
    m1 = Manager(12115, "Khalil", "Marketing")
    m1.display()  # Display manager details
    m1.manage_team()  # Manager manages the team
    m1.assign_tasks()  # Manager assigns tasks
    m1.get_department()  # Display manager's department

    print()  # Print a blank line for separation

    # Creating an instance of Intern with specific employee ID, name, supervisor, and internship duration
    i1 = Intern(15123, "Jamila Shoaib", "Daud Khan", 6)
    i1.display()  # Display intern details
    i1.track_progress()  # Track progress of the intern
    i1.report_activities()  # Report activities of the intern
