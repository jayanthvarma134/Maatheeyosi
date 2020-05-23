import gym 
import numpy as np

env_name = 'CartPole-v1'
env = gym.make(env_name)

print('obsrvation space n :', env.observation_space)