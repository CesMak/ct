import streamlit as st
import control.matlab as cm
import matplotlib
import mpld3
import streamlit.components.v1 as components
import matplotlib.pyplot as plt   # MATLAB plotting functions

m = st.slider('Select mass ', min_value=10, max_value=500, value=250, step=10)
st.write(m, 'mass=', m)

# Parameters defining the system
#m = 250.0           # system mass
k = 40.0            # spring constant
b = 60.0            # damping constant

# System matrices
A = [[0, 1.], [-k/m, -b/m]]
B = [[0], [1/m]]
C = [[1., 0]]
sys = cm.ss(A, B, C, 0)

#Step response for the system
yout, T = cm.step(sys)
ff = plt.figure()
plt.plot(T.T, yout.T)
fig_html = mpld3.fig_to_html(ff)
components.html(fig_html, height=600)



# # Step response for the system
# yout, T = cm.step(sys)
# plt.plot(T.T, yout.T)
# plt.savefig("step.png")

# # Bode plot for the system
# mag, phase, om = cm.bode(sys, cm.logspace(-2, 2), plot=True)
# plt.savefig("bode.png")

# # Nyquist plot for the system
# cm.nyquist(sys, cm.logspace(-2, 2))
# plt.savefig("nyquist.png")

# # Root lcous plot for the system
# cm.rlocus(sys)
# plt.savefig("rlocus.png")


# # see here: https://python-control.readthedocs.io/en/0.8.4/secord-matlab.html
# # Parameters defining the system
# m = 250.0           # system mass
# k = 40.0            # spring constant
# b = 60.0            # damping constant
# kp = 4.0            # control kp constant
# kd = 3.0            # control kd constant

# A = [[0, 1.], [-(k+kp)/m, -(b+kd)/m]]
# B = [[kp/m], [kd/m]]
# C = [[1., 0]]
# sys = ct.ss(A, B, C, 0)

# # Step response for the system
# plt.figure(1)
# yout, T = ct.step(sys)
# plt.plot(T.T, yout.T)
# plt.show(block=False) # 

# # Bode plot for the system
# plt.figure(2)
# mag, phase, om = ct.bode(sys, ct.logspace(-2, 2), Plot=True)
# plt.show(block=False)

# # Nyquist plot for the system
# plt.figure(3)
# ct.nyquist(sys, ct.logspace(-2, 2))
# plt.show(block=False)

# # Root lcous plot for the system
# ct.rlocus(sys)
# plt.show()