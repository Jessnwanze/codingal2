# Base class for Robot
class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        print(f"Hello, I am {self.name}, a {self.model} model robot.")

    def perform_task(self, task):
        print(f"{self.name} is performing task: {task}")

# Subclass for a specific type of robot
class CleaningRobot(Robot):
    def __init__(self, name, model, battery_level):
        super().__init__(name, model)
        self.battery_level = battery_level

    def check_battery(self):
        print(f"{self.name}'s battery level is at {self.battery_level}%.")

    def perform_task(self, task):
        if self.battery_level < 10:
            print(f"{self.name} is too low on battery to perform the task!")
        else:
            super().perform_task(task)
            self.battery_level -= 10  # Each task decreases battery by 10%

# Subclass for another specific type of robot
class EntertainmentRobot(Robot):
    def __init__(self, name, model, language):
        super().__init__(name, model)
        self.language = language

    def introduce(self):
        super().introduce()
        print(f"I speak {self.language}.")

    def play_music(self, song):
        print(f"{self.name} is now playing the song: {song}")

# Main program to test the robots
def main():
    # Create a general Robot
    robot1 = Robot("Robo", "X1000")
    robot1.introduce()
    robot1.perform_task("Cleaning the living room")

    print()

    # Create a Cleaning Robot
    robot2 = CleaningRobot("CleanBot", "X2000", 50)
    robot2.introduce()
    robot2.perform_task("Mopping the floor")
    robot2.check_battery()
    robot2.perform_task("Vacuuming the house")
    robot2.check_battery()

    print()

    # Create an Entertainment Robot
    robot3 = EntertainmentRobot("EnterBot", "X3000", "English")
    robot3.introduce()
    robot3.play_music("Shape of You")

# Run the main function
if __name__ == "__main__":
    main()

