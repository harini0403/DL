# File: src/rl_env.py
import gymnasium as gym
from gymnasium import spaces
import numpy as np

class AdaptiveLearningEnv(gym.Env):
    def __init__(self):
        super(AdaptiveLearningEnv, self).__init__()
        # Define action and observation spaces
        self.action_space = spaces.Discrete(3)  # 0: easier, 1: same, 2: harder
        self.observation_space = spaces.Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)

        # Internal state
        self.current_difficulty = 0.5
        self.last_reward = 0.0
        self.steps = 0
        self.max_steps = 50
        self.history = []  # Track (difficulty, reward) per step

    def reset(self, *, seed=None, options=None):
        # Seed for reproducibility
        if seed is not None:
            np.random.seed(seed)

        self.current_difficulty = 0.5
        self.last_reward = 0.0
        self.steps = 0
        obs = np.array([self.current_difficulty], dtype=np.float32)
        info = {}
        return obs, info

    def step(self, action):
        # Increment step counter
        self.steps += 1

        # Adjust difficulty based on action
        if action == 0:
            self.current_difficulty = max(0.0, self.current_difficulty - 0.1)
        elif action == 2:
            self.current_difficulty = min(1.0, self.current_difficulty + 0.1)
        # action == 1 leaves difficulty unchanged

        # Simulate performance around an optimal difficulty of 0.7
        performance = np.clip(
            np.random.normal(loc=1 - abs(self.current_difficulty - 0.7), scale=0.1),
            0.0, 1.0
        )
        reward = performance - abs(self.current_difficulty - 0.7)
        self.last_reward = reward

        # Determine termination and truncation
        terminated = self.steps >= self.max_steps
        truncated = False

        obs = np.array([self.current_difficulty], dtype=np.float32)
        info = {}
        return obs, reward, terminated, truncated, info




