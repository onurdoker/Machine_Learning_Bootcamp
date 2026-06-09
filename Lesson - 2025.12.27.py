import gymnasium as gym
import numpy as np

# 1. Create environment (FrozenLake-v1)
env = gym.make("FrozenLake-v1", map_name="4x4", render_mode="human")


# 2. Define Q-table
state_space = env.observation_space.n
action_space = env.action_space.n
q_table = np.zeros([env.observation_space.n, env.action_space.n])

# 3. Hyperparameters
num_episode = 10  # Agent plays the game for how many episodes?
learning_rate = 0.8  # How much value do you assign to new information?
discount_factor = 0.95  # How much value do you assign to future rewards?
epsilon = 1.0  # Exploration rate (Start at 100% - random walk)
epsilon_decay = 0.995  # Decrease the random (exploration) rate after each game.
min_epsilon = 0.01  # Minimum exploration probability

# Training Loop
print("The agent is starting to learn")

for episode in range(num_episode):
    state, info = env.reset()
    done = False

    while not done:
        # Exploration vs Exploitation
        if np.random.uniform(0, 1) < epsilon:  # Explore (random walk)
            action = env.action_space.sample()  # Choose a random action
        else:  # Exploit (use the best known action)
            action = np.argmax(q_table[state, :])  # Choose the best action

        # Take an action and observe the reward and next state
        new_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

        # Update Q-table using the Bellman equation
        q_table[state, action] += learning_rate * (
            reward
            + discount_factor * np.max(q_table[new_state, :])
            - q_table[state, action]
        )  # <--- Complete this line of code

        # Move to the next state
        state = new_state

    # Update epsilon for exploration rate decay
    epsilon = max(min_epsilon, epsilon * epsilon_decay)

print("Training completed")
print(q_table)
env.close()
