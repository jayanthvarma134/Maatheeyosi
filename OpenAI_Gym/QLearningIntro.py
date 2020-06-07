'''import gym 
import numpy as np

env_name = 'CartPole-v1'
env = gym.make(env_name)

print('obsrvation space n :', env.observation_space)

env.reset()

for _ in range(200):
	action = env.action_space.sample()
	env.step(action)
	env.render()'''

import numpy as np 
import gym
import matplotlib.pyplot as plt 
