from env import SmartClassroomEnv
import numpy as np
import matplotlib.pyplot as plt
import random

env = SmartClassroomEnv()

episodes = 300
steps_per_episode = 20

# Q-learning parameters
alpha = 0.1
gamma = 0.9
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01

# discretization helper
def discretize(state):
    students, temp, lights, ac, computers, time = state
    return (
        int(students // 10),
        int((temp - 20) // 5),
        int(lights),
        int(ac),
        int(computers),
        int(time)
    )

q_table = {}

rewards = []

for episode in range(episodes):

    state, _ = env.reset()
    state = discretize(state)
    total_reward = 0

    for step in range(steps_per_episode):

        if random.uniform(0,1) < epsilon:
            action = env.action_space.sample()
        else:
            qs = [q_table.get((state,a),0) for a in range(env.action_space.n)]
            action = np.argmax(qs)

        next_state, reward, done, _, _ = env.step(action)
        next_state = discretize(next_state)

        old_q = q_table.get((state,action),0)
        next_max = max([q_table.get((next_state,a),0) for a in range(env.action_space.n)])

        new_q = old_q + alpha * (reward + gamma * next_max - old_q)
        q_table[(state,action)] = new_q

        state = next_state
        total_reward += reward

    rewards.append(total_reward)

    epsilon = max(epsilon*epsilon_decay, epsilon_min)

    if (episode+1) % 20 == 0:
        print(f"Episode {episode+1} Reward: {total_reward}")

# Smooth graph
window = 20
smooth = np.convolve(rewards, np.ones(window)/window, mode="valid")

plt.figure(figsize=(8,5))
plt.plot(smooth)

plt.title("AI Learning Progress – Smart Classroom Energy System")
plt.xlabel("Training Episodes")
plt.ylabel("Average Reward")
plt.grid(True)

plt.show()