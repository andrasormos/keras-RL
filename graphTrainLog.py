import pandas as pd
import json
import matplotlib.pyplot as plt

with open('/home/andras/PycharmProjects/keras-RL/examples/dqn_BreakoutDeterministic-v4_log.json') as f:
   data = json.load(f)

trainLog = pd.DataFrame(data)

this = list(trainLog.columns.values)
print(this)

loss = trainLog['loss']
mean_absolute_error = trainLog['mean_absolute_error']
mean_q = trainLog['mean_q']
mean_eps = trainLog['mean_eps']
episode_reward = trainLog['episode_reward']
nb_episode_steps = trainLog['nb_episode_steps']
nb_steps = trainLog['nb_steps']
episode = trainLog['episode']
duration = trainLog['duration']

fig = plt.figure()


ax1 = fig.add_subplot(331)
ax1.plot(trainLog.index, loss, ".", color='r', markersize=1)
plt.title("Loss")


ax2 = fig.add_subplot(332)
ax2.plot(trainLog.index, mean_absolute_error, ".", color='r', markersize=1)
plt.title("Mean Absolute Error")

ax3 = fig.add_subplot(333)
ax3.plot(trainLog.index, mean_q, ".", color='g', markersize=1)
plt.title("Mean q")

ax4 = fig.add_subplot(334)
ax4.plot(trainLog.index, mean_eps, ".", color='c', markersize=1)
plt.title("Mean Epsilon")

ax5 = fig.add_subplot(335)
ax5.plot(trainLog.index, episode_reward, ".", color='g', markersize=1)
plt.title("Episode Reward")

ax6 = fig.add_subplot(336)
ax6.plot(trainLog.index, nb_episode_steps, ".", color='b', markersize=1)
plt.title("Nr of Episode Steps")

ax7 = fig.add_subplot(337)
ax7.plot(trainLog.index, nb_steps, ".", color='b', markersize=1)
plt.title("Nr of Steps")

ax8 = fig.add_subplot(338)
ax8.plot(trainLog.index, episode, ".", color='b', markersize=1)
plt.title("Episode")

ax9 = fig.add_subplot(339)
ax9.plot(trainLog.index, duration, ".", color='g', markersize=1)
plt.title("Duration")

#plt.tight_layout()
fig.suptitle('Training Analisys')
plt.show()

