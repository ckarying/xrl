#!/usr/bin/env python

import gym
import time
import random
import configparser

config = configparser.ConfigParser()
config["default"] = {
    "env_name" : "Alien-v0" ,
    "max_steps" : 100 ,
    "max_rollouts" : 20 ,
    "show_render" : True
}

def rand_policy(config):
    envname = config['env_name']
    max_rollouts = int(config['max_rollouts'])
    max_steps = int(config['max_steps'])
    show_render = config['show_render']
    
    env = gym.make(envname)
    env.seed(0)
    for rollout in range(max_rollouts):
        obs = env.reset()
        done = False
        for step in range(max_steps):
            action = env.action_space.sample()
            obs, r, done, _ = env.step(action)
            if show_render:
                env.render()
            if done:
                break
        print("rollout:%d, step:%d, done:%d" %(rollout, step, done))
        time.sleep(5)
    
def main():
    rand_policy(config['default'])
    
if __name__ == "__main__":
    main()

    
