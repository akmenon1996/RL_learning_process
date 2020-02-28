import numpy as np
import matplotlib.pyplot as plt
import sys

#sys.setrecursionlimit(10**6)
## from scipy.integrate import odeint
## import time


def lab_sim(TC):
    dTCdt = ((23-TC)+0.8*50)/120
    return dTCdt

new_temp_arr=[]
def run_sim(TC,optimum_temp,arr):
    arr.append(TC)
    if TC<optimum_temp:
        dtCdt = lab_sim(TC)
        TC+=dtCdt
        return run_sim(TC,optimum_temp,arr)
    else:
        return arr

Tsim_23 = run_sim(23,40,[])
Tsim_28 = run_sim(25,28,[])
Tsim_42 = run_sim(27,62.5,[])

plt.figure(1)
plt.plot(np.linspace(0,len(Tsim_23),len(Tsim_23)),Tsim_23,'b-',label="simulated23")
plt.plot(np.linspace(0,len(Tsim_28),len(Tsim_28)),Tsim_28,'b-',label="simulated28")
plt.plot(np.linspace(0,len(Tsim_42),len(Tsim_42)),Tsim_42,'b-',label="simulated42")
plt.ylabel("Temperature(Degree Celsius)")
plt.xlabel("Time(Seconds)")
plt.legend()
plt.show()