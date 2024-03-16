import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols

time_steps = 100000
delta_l = 0.5
L_vec = [10, 30, 50, 100]
diff_vec = [1, 10, 100, 1000]
conv_time = []
for diff in diff_vec:
    for L  in L_vec:

        print(f'L = {L}, diff = {diff}')

        conv_time.append(0)
        # Set initial time step
        delta_t_max = 0.0001
        delta_t_min = 0.000001

        # Set convergence criteria
        convergence_threshold = 1e-5  # Change in concentration threshold
        consecutive_steps = 10  # Number of consecutive steps below threshold to consider quasi-stationary

        c_0 = np.array([np.tanh(i * delta_l) for i in range(round(L / delta_l))])
        c_0[0] = 0
        c_0[-1] = c_0[-2]
        c_n = np.array([c_0])

        c, dt, ddcxx = symbols('c dt ddcxx')
        c_new = c + dt * (c ** 2 / (1 + c ** 2) - c / (1 + c) + diff * ddcxx)

        # Initialize convergence tracking variables
        consecutive_converged_steps = 0
        last_concentration = c_n[-1]

        for i in range(time_steps):
            c_temp = np.zeros_like(c_n[-1])

            # Calculate CFL condition
            max_gradient = np.max(np.abs(np.gradient(c_n[-1], delta_l)))
            delta_t = min(delta_t_max, delta_l ** 2 / (2 * diff * max_gradient))
            delta_t = max(delta_t, delta_t_min)
            conv_time[-1] = conv_time[-1] + delta_t
            if i/time_steps == 0.1:
                print(f'Length {L} and Diff {diff} did not converge at time  {conv_time[-1]}.')
            elif i/time_steps ==  0.3:
                print(f'Length {L} and Diff {diff} did not converge at time  {conv_time[-1]}.')
            elif i/time_steps == 0.5:
                print(f'Length {L} and Diff {diff} did not converge at time  {conv_time[-1]}.')
            for j in range(1, len(c_n[-1]) - 1):  # Skipping first and last elements
                # Calculate diffusion term
                diffusion_term = c_n[-1][j + 1] / delta_l ** 2 - 2 * c_n[-1][j] / delta_l ** 2 + c_n[-1][j - 1] / delta_l ** 2
                # Evaluate new concentration using the symbolic expression
                c_temp[j] = c_new.evalf(subs={c: c_n[-1][j], dt: delta_t, ddcxx: diffusion_term}, chop=True)

            # Set boundary conditions
            c_temp[0] = 0
            c_temp[-1] = c_temp[-2]

            # Check for convergence
            change_in_concentration = np.max(np.abs(c_temp - last_concentration))
            if change_in_concentration < convergence_threshold:
                consecutive_converged_steps += 1
                if consecutive_converged_steps >= consecutive_steps:
                    print(f"Length {L} and Diff {diff} Converged at time  {conv_time[-1]}.")
                    break
            else:
                consecutive_converged_steps = 0


            # Update last concentration for next iteration
            last_concentration = c_temp.copy()

            c_n = np.append(c_n, [c_temp], axis=0)

        # Plot every nth line in a different color on a labeled plot
        import matplotlib.colors as mcolors

        n = 100
        for i in range(0, len(c_n), n):
            # Calculate the color based on progress in time
            progress = i / (len(c_n) - 1)  # Progress normalized between 0 and 1
            color = mcolors.to_rgba((1 - progress, 0, progress))  # Fade from red to blue

            plt.plot(np.linspace(0, L, int(L / delta_l)), c_n[i], label='t = ' + str(i * delta_t), color=color)

        plt.xlabel('l (arbitrary units)')
        plt.ylabel('concentration (arbitrary units)')
        pltname = f'Exc4_sol_{L}_{diff}.png'
        plt.savefig(pltname)
        plt.show()
