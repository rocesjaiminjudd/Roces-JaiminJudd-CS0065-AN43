"""TA2 - Rule-Based Vacuum Agent

CS0065 Intelligent Systems
Technical Assessment 2
Student: ROCES
"""


def get_room_state(room_name):
    """Ask for and validate the initial state of one room."""
    while True:
        state = input(f"Enter the initial state of Room {room_name} (dirty/clean): ").strip().lower()
        if state in {"dirty", "clean"}:
            return state
        print("Invalid input. Please enter only 'dirty' or 'clean'.")


def is_dirty(environment, room):
    """Return True when the selected room is dirty."""
    return environment[room] == "dirty"


def clean_room(environment, room):
    """Change the selected room's state to clean."""
    environment[room] = "clean"


class VacuumAgent:
    """A rule-based agent that cleans or moves according to room state."""

    def __init__(self, environment, start_room="A"):
        self.environment = environment
        self.current_room = start_room

    def move(self):
        """Move between the two rooms."""
        self.current_room = "B" if self.current_room == "A" else "A"

    def perceive_and_act(self):
        """Perceive the current room and apply the first matching rule."""
        if is_dirty(self.environment, self.current_room):
            clean_room(self.environment, self.current_room)
            return f"cleaned Room {self.current_room}"

        previous_room = self.current_room
        self.move()
        return f"moved from Room {previous_room} to Room {self.current_room}"


def display_environment(environment):
    """Return a readable representation of the environment."""
    return f"A = {environment['A']}, B = {environment['B']}"


def get_step_count():
    """Ask for a non-negative integer number of simulation steps."""
    while True:
        try:
            steps = int(input("How many simulation steps should run? "))
            if steps >= 0:
                return steps
        except ValueError:
            pass
        print("Invalid input. Please enter a non-negative whole number.")


def main():
    print("RULE-BASED VACUUM AGENT")
    print("The agent starts in Room A.\n")

    environment = {
        "A": get_room_state("A"),
        "B": get_room_state("B"),
    }
    steps = get_step_count()
    agent = VacuumAgent(environment)

    print(f"\nInitial environment: {display_environment(environment)}")
    print(f"Initial agent location: Room {agent.current_room}")

    for step in range(1, steps + 1):
        action = agent.perceive_and_act()
        print(f"Step {step}: {action}")
        print(f"  Agent location: Room {agent.current_room}")
        print(f"  Environment: {display_environment(environment)}")

    print("\nSimulation complete.")


if __name__ == "__main__":
    main()
