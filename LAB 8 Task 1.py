import math  # Import the math module to use mathematical constants like pi

# Abstract base class Shape
class Shape:
    def __init__(self):
        self.area = 0  # Initialize area as 0
        self.volume = 0  # Initialize volume as 0

    def compute_area(self):
        pass  # Method to compute the area, to be implemented by subclasses

    def compute_volume(self):
        pass  # Method to compute the volume, to be implemented by subclasses

    def display(self):
        pass  # Method to display the shape information, to be implemented by subclasses

    def get_area(self):
        return self.area  # Return the computed area

    def get_volume(self):
        return self.volume  # Return the computed volume

# Derived class Point (inherits from Shape)
class Point(Shape):
    def __init__(self, x=0, y=0):
        super().__init__()  # Call the constructor of the parent class (Shape)
        self.x = x  # Initialize the x-coordinate
        self.y = y  # Initialize the y-coordinate

    def compute_area(self):
        self.area = 0  # A point has no area

    def compute_volume(self):
        self.volume = 0  # A point has no volume

    def display(self):
        print(f"Point Position: ({self.x}, {self.y})")  # Display the point's position

# Derived class Circle (inherits from Point)
class Circle(Point):
    def __init__(self, x=0, y=0, radius=5):
        super().__init__(x, y)  # Call the constructor of the parent class (Point)
        self.radius = radius  # Initialize the radius of the circle

    def compute_area(self):
        # Compute the area of the circle using the formula: π * radius^2
        self.area = math.pi * self.radius * self.radius

    def compute_volume(self):
        self.volume = 0  # A circle has no volume

    def display(self):
        # Display the circle's position and radius
        print(f"Circle Position: ({self.x}, {self.y}), Radius: {self.radius}")

# Derived class Cylinder (inherits from Circle)
class Cylinder(Circle):
    def __init__(self, x=0, y=0, radius=5, height=10):
        super().__init__(x, y, radius)  # Call the constructor of the parent class (Circle)
        self.height = height  # Initialize the height of the cylinder

    def compute_area(self):
        # Compute the surface area of the cylinder: 2πr(r + h)
        self.area = 2 * math.pi * self.radius * (self.radius + self.height)

    def compute_volume(self):
        # Compute the volume of the cylinder: πr^2h
        self.volume = math.pi * self.radius * self.radius * self.height

    def display(self):
        # Display the cylinder's position, radius, and height
        print(f"Cylinder Position: ({self.x}, {self.y}), Radius: {self.radius}, Height: {self.height}")

# Main code to test the classes
if __name__ == "__main__":
    # Create objects of derived classes
    shape1 = Point(2, 3)  # Create a Point object at position (2, 3)
    shape2 = Circle(1, 1, 7)  # Create a Circle object at position (1, 1) with radius 7
    shape3 = Cylinder(0, 0, 5, 10)  # Create a Cylinder object at position (0, 0), radius 5, and height 10

    # Display details and compute area and volume for each shape
    shape1.display()  # Display the Point object
    shape1.compute_area()  # Compute its area (should be 0)
    shape1.compute_volume()  # Compute its volume (should be 0)
    print(f"Area: {shape1.get_area()}, Volume: {shape1.get_volume()}\n")  # Display area and volume

    shape2.display()  # Display the Circle object
    shape2.compute_area()  # Compute its area
    shape2.compute_volume()  # Compute its volume (should be 0)
    print(f"Area: {shape2.get_area()}, Volume: {shape2.get_volume()}\n")  # Display area and volume

    shape3.display()  # Display the Cylinder object
    shape3.compute_area()  # Compute its area
    shape3.compute_volume()  # Compute its volume
    print(f"Area: {shape3.get_area()}, Volume: {shape3.get_volume()}\n")  # Display area and volume
