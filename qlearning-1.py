import gym
import numpy as np
# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)

env=gym.make("MountainCar-v0", render_mode="human")
env.reset()

## printing highest coordinates
print(env.observation_space.high)
## printing lowest coordinates
print(env.observation_space.low)

print(env.action_space.n)

DISCRETE_OS_SIZE=[20]*len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high-env.observation_space.low)/DISCRETE_OS_SIZE

print(discrete_os_win_size)

q_table=np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE+[env.action_space.n]))
print(q_table.shape)
print(q_table)

# done=False

# while not done:
#     action=2
#     new_state, reward, terminated, truncated, _ = env.step(action)
#     done = terminated or truncated
#     # print(reward, new_state)
#     env.render()

# env.close()

# ## Q-Table: Shows q values for every possible combination of position and velocity