import gymnasium as gym
from gymnasium import spaces
import numpy as np
import random

class SmartClassroomEnv(gym.Env):

    def __init__(self):
        super(SmartClassroomEnv, self).__init__()

        # Actions
        self.action_space = spaces.Discrete(4)

        # Observation space
        self.observation_space = spaces.Box(
            low=np.array([0, 20, 0, 0, 0, 0]),
            high=np.array([40, 40, 1, 1, 1, 2]),
            dtype=np.float32
        )

        self.state = None

    def reset(self, seed=None, options=None):

        students = random.randint(0, 40)
        temperature = random.randint(20, 40)
        lights = random.randint(0, 1)
        ac = random.randint(0, 1)
        computers = random.randint(0, 1)
        time_of_day = random.randint(0, 2)

        self.state = np.array([
            students,
            temperature,
            lights,
            ac,
            computers,
            time_of_day
        ], dtype=np.float32)

        return self.state, {}

    def step(self, action):

        students, temperature, lights, ac, computers, time_of_day = self.state

        # Apply action
        if action == 0:
            lights = 1 - lights
        elif action == 1:
            ac = 1 - ac
        elif action == 2:
            computers = 1 - computers
        elif action == 3:
            pass

        reward = 0

        # Comfort reward
        comfort = abs(temperature - 24)
        reward += (10 - comfort)

        # Lights logic
        if students > 0 and lights == 1:
            reward += 5

        if students == 0 and lights == 1:
            reward -= 5

        # AC logic
        if students > 0 and temperature > 30 and ac == 1:
            reward += 8

        if students == 0 and ac == 1:
            reward -= 5

        # Energy consumption penalty
        energy_usage = (lights * 2) + (ac * 5) + (computers * 3)
        reward -= energy_usage * 0.3

        self.state = np.array([
            students,
            temperature,
            lights,
            ac,
            computers,
            time_of_day
        ], dtype=np.float32)

        done = False

        return self.state, reward, done, False, {}