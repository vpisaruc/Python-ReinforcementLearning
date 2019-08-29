import gym
import numpy as np

# set our environment
env = gym.make("MountainCar-v0")
env.reset()

# highest point of the map
print(env.observation_space.high)
# lowest point of the map
print(env.observation_space.low)
# how many actions we can atualy take
print(env.action_space.n)

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

# make a random distribution from -2 to 0
q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))
print(q_table.shape)

"""
done = False

while not done:
    # we have 3 actions
    # 0 - push car left
    # 2 - push car right
    # 1 - do nothing
    action = 2
    new_state, reward, done, _ = env.step(action)
    print(reward, new_state)
    # render our car environment
    env.render()

env.close()
"""