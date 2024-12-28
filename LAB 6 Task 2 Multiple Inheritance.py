# Base class for inputting and displaying the base value
class Base:
    def __init__(self):
        self.ba = 0  # Initialize base to 0
    
    def input_base(self):
        """Method to input base value."""
        self.ba = int(input("Enter base: "))  # Input base value
    
    def show_base(self):
        """Method to display base value."""
        print(f"Base: {self.ba}")

# Exponent class for inputting and displaying the exponent value
class Exponent:
    def __init__(self):
        self.exp = 0  # Initialize exponent to 0
    
    def input_exp(self):
        """Method to input exponent value."""
        self.exp = int(input("Enter exponent: "))  # Input exponent value
    
    def show_exp(self):
        """Method to display exponent value."""
        print(f"Exponent: {self.exp}")

# Derived class Power, inherits from both Base and Exponent
class Power(Base, Exponent):
    def __init__(self):
        super().__init__()  # Call constructor of Base
        Exponent.__init__(self)  # Call constructor of Exponent
        self.po = 1  # Initialize power to 1
    
    def in1(self):
        """Method to input both base and exponent."""
        self.input_base()  # Input base value
        self.input_exp()   # Input exponent value
    
    def show1(self):
        """Method to display base, exponent, and the calculated power."""
        self.show_base()  # Show base value
        self.show_exp()   # Show exponent value
        
        # Calculate the power (base raised to the exponent)
        for i in range(self.exp):
            self.po *= self.ba
        print(f"Power: {self.po}")  # Display the calculated power

# Main function to execute the program
if __name__ == "__main__":
    p1 = Power()  # Create an instance of the Power class
    p1.in1()      # Input base and exponent values
    p1.show1()    # Display base, exponent, and calculated power
