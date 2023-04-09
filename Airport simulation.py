import random
import numpy as np
import matplotlib.pyplot as plt

# data
#p - number of runways
p = 3
pt = np.zeros(p)  # time that planes need to fly away from runway t
#s = int()  # ilosc samolotow na lotnisku

# w - number of planes that are operated on airport in time T
# w will be from uniform and normal distribution
#w = np.random.normal(5, 5, 24)
w = np.random.uniform(0, 10, 24)

c = [10, 20, 30]  # time needed to serve plane of specific type
r = 3  # number of types of planes

# number of planes that leave airport in time T
o = np.zeros(24)

# time starts at 0
T = 0

# restrictions:
w_abs = np.absolute(w)
w_abs_int = w_abs.astype(int)

print(w_abs_int)

while T < 24:
    T += 1

for i in range(0, len(w_abs_int)):
    if w_abs_int[i] > 0 and o[i] == 0:
        break

# criteria:
"""for i in range(0, len(w)):
    sum = w[i] - o[i]"""

# counting number of planes on airport
time = 60
t = 0
while t < len(w_abs_int):

    for j in range(len(pt)):
        if pt[j] == 0:
            if w_abs_int[t] > 0:
                w_abs_int[t] -= 1
                # draw type of plane that lands
                pt[j] = 10 * random.randint(1, 3)
        else:     # if there is any plane on runway
            pt[j] -= 5
            if pt[j] == 0:
                o[t] += 1
                #print(o)
    if time == 0:
        if t == 23:
            break
        w_abs_int[t+1] += w_abs_int[t]
        t += 1
        time = 60
    else:
        time -= 5

    print("time: ", time, " to operate: ", w_abs_int[t], " time needed for planes to take off: ", pt,
          " number of planes that already took of: ", o)


# chart representing changes in number of planes in time
x_data = list(range(24))
print("o = ", o )
y= w_abs.astype(int)
y_data = list()
for i in range(0, 24):
    y_data.append(y[i]-o[t])


plt.scatter(x_data, y_data, c='red', label='time to operate')
plt.show()
plt.scatter(x_data, y, c='coral', label='arrivals')
plt.scatter(x_data, o, c='lightblue', label='departure', s=20)
plt.legend()
plt.title('Plane service on airport')
plt.xlabel('Time')
plt.ylabel('Number of planes')
plt.show()
