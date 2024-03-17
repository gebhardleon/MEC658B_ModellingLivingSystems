import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


L_vec = np.array([10, 30, 50, 100])
diff_vec = np.array([1, 10, 100, 1000])

equilibrium_time = np.array([
    [15.47, 36.91, 57.56, 108.46],
    [7.35, 15.82, 22.82, 39.53],
    [1.73, 6.10, 9.09, 15.08],
    [0.21, 1.12, 2.13, 4.47]
])
equilibrium_df = pd.DataFrame(equilibrium_time, index=diff_vec, columns=L_vec)

# Plotting data
for i in range(len(diff_vec)):
    plt.scatter(L_vec, equilibrium_time[i])
    plt.plot(L_vec, equilibrium_time[i], label=f'Diffusion constant = {diff_vec[i]}')
plt.legend()
plt.xlabel('L')
plt.ylabel('Equilibrium Time')
plt.title('Equilibrium Time vs. L for Different Diffusion Constants')
# plot predicted equilibrium time for each L and diff constant
plt.legend()
plt.savefig('Exc2_Time_length.png')
plt.show()

# plot predicted equilibrium over diffusion coefficient
for i in range(len(L_vec)):
    plt.scatter(diff_vec, equilibrium_time[:, i])
    plt.loglog(diff_vec, equilibrium_time[:, i], label=f'L = {L_vec[i]}')
plt.legend()
plt.xlabel('Diffusion Constant')
plt.ylabel('Equilibrium Time')
plt.title('Equilibrium Time vs. Diffusion Constant for Different L')
plt.savefig('Exc2_Time_diff.png')
plt.show()
# calculate the slope of each log-log plot and then
for i in range(len(L_vec)):
    slope = np.diff(np.log(equilibrium_time[:, i])) / np.diff(np.log(diff_vec))
    print(f'L = {L_vec[i]}: {slope}')
# plot the slope of each log-log plot
    plt.plot( slope)
plt.xlabel('L')
plt.ylabel('Slope')
plt.title('Slope of Equilibrium Time vs. Diffusion Constant for Different L')
plt.savefig('Exc2_slope_length.png')
plt.show()