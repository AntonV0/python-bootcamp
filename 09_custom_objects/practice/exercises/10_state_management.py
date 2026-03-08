"""Exercise 10: State Management"""


class TrafficLight:
    """TrafficLight class to manage the state of a traffic light."""
    total_light_changes = 0  # Class variable to track total light changes across all instances

    # List of traffic light colors in the order they change
    COLOURS = ["Red", "Green", "Yellow"]

    DURATIONS = {
        "Red": 50,
        "Green": 60,
        "Yellow": 5
    }

    def __init__(self, colour):
        self.colour = colour
        # Set the initial duration based on the color
        self.duration = TrafficLight.DURATIONS[colour]

    def change_colour(self):
        """Change the traffic light to the next colour in the sequence."""
        # Find the index of the current colour
        current_index = TrafficLight.COLOURS.index(self.colour)
        # Calculate the index of the next colour using modulo to wrap around the list
        # Modulo operator (%) ensures list wraps back to the beginning
        next_index = (current_index + 1) % len(TrafficLight.COLOURS)

        # Update the colour to the next one in the sequence
        self.colour = TrafficLight.COLOURS[next_index]
        # Update the duration based on the new colour
        self.duration = TrafficLight.DURATIONS[self.colour]

        TrafficLight.total_light_changes += 1  # Increment total light changes

        print(
            f"Traffic light changed to {self.colour} for {self.duration} seconds.")
        print(f"Total light changes: {TrafficLight.total_light_changes}")


if __name__ == "__main__":
    # Create a TrafficLight object with the initial colour "Red"
    traffic_light = TrafficLight("Red")

    for _ in range(6):  # Change the traffic light 6 times
        traffic_light.change_colour()

# ? Output:
# Traffic light changed to Green for 60 seconds.
# Total light changes: 1
# Traffic light changed to Yellow for 5 seconds.
# Total light changes: 2
# Traffic light changed to Red for 50 seconds.
# Total light changes: 3
# Traffic light changed to Green for 60 seconds.
# Total light changes: 4
# Traffic light changed to Yellow for 5 seconds.
# Total light changes: 5
# Traffic light changed to Red for 50 seconds.
# Total light changes: 6
