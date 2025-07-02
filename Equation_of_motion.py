#wap to input initial velocity and acceleration and plot the following graph depicting equation on motion 
#velocity wrt time (v=u+at)
#distance wrt time (s=u+.5* at^2)
#distance wrt to velocity (s=v^2-u^2/2a)


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

u = float(input("Enter initial velocity (u) in m/s: "))
a = float(input("Enter acceleration (a) in m/s²: "))

t = np.linspace(0, 10)

v = u + a * t
s = u * t + 0.5 * a * t**2


if a != 0:
    k = (v**2 - u**2) / (2 * a)
else:
    k = u * t  

# Plotting
plt.figure(figsize=(15, 5))

# Velocity vs. Time

plt.subplot(1, 3, 1)
plt.plot(t, v, color='blue')
plt.title('Velocity vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid(True)

# Distance vs. Time

plt.subplot(1, 3, 2)
plt.plot(t, s, color='green')
plt.title('Distance vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.grid(True)

# Distance vs. Velocity

plt.subplot(1, 3, 3)
plt.plot(v, k, color='red')
plt.title('Distance vs. Velocity')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Distance (m)')
plt.grid(True)

plt.tight_layout()
plt.show()
