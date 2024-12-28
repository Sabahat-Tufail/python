# Class definition for GPSCoordinates
class GPSCoordinates:
    """
    Represents a geographical coordinate with latitude and longitude.
    Provides methods to get and set these coordinates and display them.
    """

    def __init__(self, latitude=0, longitude=0):
        """
        Constructor to initialize the GPS coordinates.
        - If no arguments are passed, both latitude and longitude default to 0.
        :param latitude: The latitude of the location (default is 0)
        :param longitude: The longitude of the location (default is 0)
        """
        self.latitude = latitude  # Instance variable for latitude
        self.longitude = longitude  # Instance variable for longitude

    def get_latitude(self):
        """
        Getter method for the latitude coordinate.
        :return: The current value of latitude.
        """
        return self.latitude

    def set_latitude(self, latitude):
        """
        Setter method for the latitude coordinate.
        Updates the latitude to the given value.
        :param latitude: The new value for latitude.
        """
        self.latitude = latitude

    def get_longitude(self):
        """
        Getter method for the longitude coordinate.
        :return: The current value of longitude.
        """
        return self.longitude

    def set_longitude(self, longitude):
        """
        Setter method for the longitude coordinate.
        Updates the longitude to the given value.
        :param longitude: The new value for longitude.
        """
        self.longitude = longitude

    def display(self):
        """
        Prints the current latitude and longitude as a tuple.
        Example output: (33.6844, 71.0975)
        """
        print(f"({self.latitude}, {self.longitude})")


# Main function equivalent in Python
if __name__ == "__main__":
    # Step 1: Create location1 with default coordinates (0, 0)
    location1 = GPSCoordinates()  # No arguments passed; default values are used
    print("Location 1: ", end="")  # Print label for the output
    location1.display()  # Display the default values of location1 (0, 0)

    # Step 2: Update the coordinates of location1
    location1.set_latitude(33.6844)  # Set latitude to 33.6844
    location1.set_longitude(71.0975)  # Set longitude to 71.0975
    print("Updated Location 1: ", end="")  # Print label for the updated values
    location1.display()  # Display the updated values of location1 (33.6844, 71.0975)

    # Step 3: Create location2 with specific coordinates (33.6844, 73.0479)
    location2 = GPSCoordinates(33.6844, 73.0479)  # Pass latitude and longitude as arguments
    print("Location 2: ", end="")  # Print label for location2
    location2.display()  # Display the coordinates of location2 (33.6844, 73.0479)
