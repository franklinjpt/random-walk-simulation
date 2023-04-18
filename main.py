import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
all_walks = []

for i in range(500):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step = max(0, step - 1)
        elif 2 < dice < 6:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        if np.random.rand() <= 0.0001:
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

np_aw = np.array(all_walks)
np_aw_t = np.transpose(np_aw)
#plt.plot(np_aw_t)
#plt.show()
ends = np_aw_t[-1, :]

plt.hist(ends)
plt.show()

#Calculate the odds
odds = len(ends[ends >= 60]) / 500
print(odds)

