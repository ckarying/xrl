#!/usr/bin/env python
# -*- coding: gbk -*-
"""
author: chenkangrui
email: chenkangrui@baidu.com
time: 2018-04-15
"""
import gym
import time
import random
envname = "Ant-v2"
max_steps = 100
max_rollouts = 20
show_render = True
def main():
    env = gym.make(envname)
    env.seed(0)
    print(env.action_space)
    for rollout in range(max_rollouts):
        obs = env.reset()
        done = False
        for step in range(max_steps):
#            action = [random.uniform(0, 1), random.uniform(0, 1)]
#            print("action:", action)
            action = env.action_space.sample()
            obs, r, done, _ = env.step(action)
#            print("done:", done)
            if show_render:
                env.render()
            if done:
                break
        print("rollout:%d, step:%d, done:%d" %(rollout, step, done))
        time.sleep(5)
        
if __name__ == "__main__":
    main()

    
