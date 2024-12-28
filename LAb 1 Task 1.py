class LightBulb:  # Create class
    def __init__(self):  # Constructor (equivalent to lightbulb() in C++)
        self.is_on = False  # Initialize isOn to False

    def turn_on(self):  # Method to turn the bulb ON
        self.is_on = True

    def turn_off(self):  # Method to turn the bulb OFF
        self.is_on = False

    def get_state(self):  # Method to get the current state of the bulb
        return self.is_on

    def show(self):  # Method to display the current state
        if self.get_state():
            print("The light bulb is now ON")
        else:
            print("The light bulb is now OFF")


# Main function equivalent
if __name__ == "__main__":
    bulb = LightBulb()  # Create an object of LightBulb
    bulb.show()         # Show initial state
    bulb.turn_on()      # Turn the bulb ON
    bulb.show()         # Show current state
    bulb.turn_off()     # Turn the bulb OFF
    bulb.show()         # Show current state
