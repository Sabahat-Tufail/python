class Complex:
    """
    A class to represent a complex number and perform operations like addition, subtraction, and multiplication.
    """

    def __init__(self):
        """
        Initializes a complex number with real and imaginary parts set to 0 by default.
        """
        self.re = 0  # Real part
        self.im = 0  # Imaginary part

    def input(self):
        """
        Takes input from the user for the real and imaginary parts of the complex number.
        """
        self.re = float(input("Enter the real part: "))  # Input for real part
        self.im = float(input("Enter the imaginary part: "))  # Input for imaginary part

    def add_com(self, c):
        """
        Adds the current complex number with another complex number c.
        Returns the result as a new complex number.
        :param c: Another complex number
        :return: Resultant complex number after addition
        """
        temp = Complex()  # Create a temporary complex number for storing the result
        temp.re = self.re + c.re  # Add real parts
        temp.im = self.im + c.im  # Add imaginary parts
        return temp

    def sub_com(self, c):
        """
        Subtracts the current complex number by another complex number c.
        Returns the result as a new complex number.
        :param c: Another complex number
        :return: Resultant complex number after subtraction
        """
        temp = Complex()  # Create a temporary complex number for storing the result
        temp.re = self.re - c.re  # Subtract real parts
        temp.im = self.im - c.im  # Subtract imaginary parts
        return temp

    def mult_com(self, c):
        """
        Multiplies the current complex number with another complex number c.
        Returns the result as a new complex number.
        :param c: Another complex number
        :return: Resultant complex number after multiplication
        """
        temp = Complex()  # Create a temporary complex number for storing the result
        temp.re = (self.re * c.re) - (self.im * c.im)  # Real part of the product
        temp.im = (self.re * c.im) + (self.im * c.re)  # Imaginary part of the product
        return temp

    def show(self):
        """
        Displays the complex number in the format "a + bi" or "a - bi".
        """
        if self.im >= 0:
            print(f"{self.re} + {self.im}i")
        else:
            print(f"{self.re} - {abs(self.im)}i")


# Main program to demonstrate complex number operations
if __name__ == "__main__":
    c1 = Complex()  # First complex number
    c2 = Complex()  # Second complex number
    result = Complex()  # Resultant complex number for operations

    print("Enter the first complex number:")
    c1.input()  # Input for first complex number

    print("Enter the second complex number:")
    c2.input()  # Input for second complex number

    # Addition
    result = c1.add_com(c2)
    print("Addition result:")
    result.show()

    # Subtraction
    result = c1.sub_com(c2)
    print("Subtraction result:")
    result.show()

    # Multiplication
    result = c1.mult_com(c2)
    print("Multiplication result:")
    result.show()
