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

    def add_com(self, c1, c2):
        """
        Adds two complex numbers and stores the result in the current object.
        :param c1: First complex number
        :param c2: Second complex number
        """
        self.re = c1.re + c2.re  # Real part addition
        self.im = c1.im + c2.im  # Imaginary part addition

    def sub_com(self, c1, c2):
        """
        Subtracts two complex numbers and stores the result in the current object.
        :param c1: First complex number
        :param c2: Second complex number
        """
        self.re = c1.re - c2.re  # Real part subtraction
        self.im = c1.im - c2.im  # Imaginary part subtraction

    def mult_com(self, c1, c2):
        """
        Multiplies two complex numbers and stores the result in the current object.
        :param c1: First complex number
        :param c2: Second complex number
        """
        self.re = (c1.re * c2.re) - (c1.im * c2.im)  # Real part: ac - bd
        self.im = (c1.re * c2.im) + (c1.im * c2.re)  # Imaginary part: ad + bc

    def show(self):
        """
        Displays the complex number in the format "a + bi" or "a - bi".
        """
        if self.im >= 0:
            print(f"{self.re} + {self.im}i")
        else:
            print(f"{self.re} - {abs(self.im)}i")


# Main function equivalent
if __name__ == "__main__":
    c1 = Complex()  # First complex number
    c2 = Complex()  # Second complex number
    result = Complex()  # Resultant complex number for operations

    print("Enter the first complex number:")
    c1.input()  # Input for first complex number

    print("Enter the second complex number:")
    c2.input()  # Input for second complex number

    # Subtraction
    result.sub_com(c1, c2)
    print("Subtraction result:")
    result.show()

    # Addition
    result.add_com(c1, c2)
    print("Addition result:")
    result.show()

    # Multiplication
    result.mult_com(c1, c2)
    print("Multiplication result:")
    result.show()
