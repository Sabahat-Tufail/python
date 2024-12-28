# Base class First
class First:
    def __init__(self):
        """
        Constructor for the First class.
        """
        self.f = 0  # Initialize the first number

    def f_input(self):
        """
        Method to input the first number.
        """
        self.f = int(input("Enter number 1: "))  # Input first number


# Derived class Second, inherits from First
class Second(First):
    def __init__(self):
        """
        Constructor for the Second class, which inherits from First.
        """
        super().__init__()  # Call the parent constructor to initialize 'f'
        self.s = 0  # Initialize the second number

    def s_input(self):
        """
        Method to input the second number.
        """
        self.f_input()  # Call the f_input() method from the parent class
        self.s = int(input("Enter number 2: "))  # Input second number


# Derived class Third, inherits from Second
class Third(Second):
    def __init__(self):
        """
        Constructor for the Third class, which inherits from Second.
        """
        super().__init__()  # Call the parent constructor to initialize 'f' and 's'
        self.t = 0  # Initialize the third number

    def t_input(self):
        """
        Method to input the third number.
        """
        self.s_input()  # Call the s_input() method from the parent class
        self.t = int(input("Enter number 3: "))  # Input third number

    def max(self):
        """
        Method to find and print the maximum of the three numbers.
        """
        if self.s >= self.f and self.s >= self.t:
            print("Maximum:", self.s)  # If 's' is the largest
        elif self.t >= self.f and self.t >= self.s:
            print("Maximum:", self.t)  # If 't' is the largest
        else:
            print("Maximum:", self.f)  # If 'f' is the largest

    def show(self):
        """
        Method to display the three numbers.
        """
        print(f"First number: {self.f}")
        print(f"Second number: {self.s}")
        print(f"Third number: {self.t}")


# Main execution
if __name__ == "__main__":
    t1 = Third()  # Create an instance of Third
    t1.t_input()  # Input the three numbers
    t1.show()  # Show the numbers
    t1.max()  # Show the maximum value
