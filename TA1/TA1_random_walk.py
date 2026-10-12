import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# -----------------------------------------
# Get user input
# -----------------------------------------
num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
num_steps = int(input("Enter number of steps: "))


# -----------------------------------------
# Agent Definition
# -----------------------------------------
class RandomWalker(ap.Agent):

    def setup(self):
        # Starting position of the agent
        self.position = (
            random.randint(0, self.model.p.grid_size[0] - 1),
            random.randint(0, self.model.p.grid_size[1] - 1)
        )

        # Store the agent's movement history
        self.path = [self.position]

    def step(self):
        # Possible movement directions
        directions = [
            (1, 0),    # Right
            (-1, 0),   # Left
            (0, 1),    # Up
            (0, -1)   # Down
        ]

        # Shuffle directions so the agent still moves randomly
        random.shuffle(directions)

        old_position = self.position

        # Try each direction until a valid movement is found
        for direction in directions:

            new_x = old_position[0] + direction[0]
            new_y = old_position[1] + direction[1]

            # Check if the new position is inside the grid
            if (
                0 <= new_x < self.model.p.grid_size[0]
                and
                0 <= new_y < self.model.p.grid_size[1]
            ):

                new_position = (new_x, new_y)

                # -----------------------------------------
                # Task 2: Avoid other agents
                # -----------------------------------------
                occupied_positions = [
                    agent.position
                    for agent in self.model.agents
                    if agent != self
                ]

                # Move only if another agent is not occupying
                # the new position
                if new_position not in occupied_positions:
                    self.position = new_position
                    break

        # -----------------------------------------
        # Task 1: Track the agent's path
        # -----------------------------------------
        self.path.append(self.position)


# -----------------------------------------
# Model Definition
# -----------------------------------------
class RandomWalkModel(ap.Model):

    def setup(self):

        # Create the agents
        self.agents = ap.AgentList(
            self,
            self.p.agents,
            RandomWalker
        )

        # Create the grid
        self.grid = ap.Grid(
            self,
            self.p.grid_size,
            torus=False
        )

        # Add agents to the grid
        self.grid.add_agents(self.agents)


    def step(self):

        # Move every agent
        for agent in self.agents:
            agent.step()


# -----------------------------------------
# Parameters
# -----------------------------------------
parameters = {
    'agents': num_agents,
    'grid_size': (grid_size, grid_size),
    'steps': num_steps
}


# -----------------------------------------
# Create and setup the model
# -----------------------------------------
model = RandomWalkModel(parameters)
model.setup()


# -----------------------------------------
# Animation setup
# -----------------------------------------
fig, ax = plt.subplots()

ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)

ax.set_xticks(range(grid_size + 1))
ax.set_yticks(range(grid_size + 1))

ax.grid(True)

ax.set_title("Random Walk Simulation")


# Display agents as dots
scat = ax.scatter([], [], s=200)


# -----------------------------------------
# Update animation
# -----------------------------------------
def update(frame):

    # Move all agents
    model.step()

    # Get the x and y positions
    x = [agent.position[0] for agent in model.agents]
    y = [agent.position[1] for agent in model.agents]

    # Update the dots
    scat.set_offsets(list(zip(x, y)))

    return scat,


# -----------------------------------------
# Run the animation
# -----------------------------------------
ani = animation.FuncAnimation(
    fig,
    update,
    frames=num_steps,
    blit=True,
    repeat=False
)

plt.show()


# -----------------------------------------
# Task 3: Display final positions
# -----------------------------------------
print("\n========== FINAL POSITIONS ==========")

for i, agent in enumerate(model.agents):
    print(
        f"Agent {i + 1}: "
        f"Final Position = {agent.position}"
    )


# -----------------------------------------
# Display paths
# -----------------------------------------
print("\n========== AGENT PATHS ==========")

for i, agent in enumerate(model.agents):

    print(f"\nAgent {i + 1} Path:")

    for step_number, position in enumerate(agent.path):
        print(
            f"Step {step_number}: {position}"
        )


# -----------------------------------------
# Task 3: Analyze final position distribution
# -----------------------------------------
print("\n========== POSITION ANALYSIS ==========")

position_count = {}

for agent in model.agents:

    position = agent.position

    if position in position_count:
        position_count[position] += 1
    else:
        position_count[position] = 1


for position, count in position_count.items():

    print(
        f"Position {position}: "
        f"{count} agent(s)"
    )


print("\nSimulation complete.")