import numpy as np
import gym
import torch
# from stable_baselines3.common.utils import set_random_seed
from stable_baselines3 import PPO
import pickle
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv, VecEnv
from environment import environment
from stable_baselines3.common.callbacks import CheckpointCallback
from torch import nn
from GL_Policy import CustomGLPolicy
from stable_baselines3.common.torch_layers import BaseFeaturesExtractor


# policy_kwargs = dict(
#     features_extractor_class = CustomGLPolicy,
#     features_extractor_kwargs=dict(
#     features_dim = 134,
#     )
# )

# Save a checkpoint every 1000 steps
checkpoint_callback = CheckpointCallback(save_freq=1000, save_path='./UAM_RL_Model/',
                                         name_prefix='UAM_RL_Model')


# env = DummyVecEnv([lambda: environment(5)])
# env = SubprocVecEnv([lambda: environment(5)])

env = environment(no_of_drones=5)

model = PPO(CustomGLPolicy,env=env,tensorboard_log='UAM_RL_Model/',verbose=1,n_steps=50,batch_size=10,gamma=1,learning_rate=0.001,device='cuda')
model.learn(total_timesteps=10000,n_eval_episodes=1,log_interval=1,callback=checkpoint_callback)


model.save("final_model")


