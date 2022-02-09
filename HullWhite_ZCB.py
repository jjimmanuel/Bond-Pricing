
import numpy as np
import matplotlib.pyplot as plt
import QuantLib as ql
from QuantLib import *
import pandas as pd


# Variables

today = Date(1, 1, 2010)
Settings.instance().evaluationDate = today

a = 0.1
sigma = 0.01
dayCounter = Actual365Fixed()
length  = 30 # in years
steps = 360 # 12/year
rate = 0.01
steps_per_year = 12
dt = 1/12

# Yield Curve

curve = FlatForward(today, rate, dayCounter)
curveHandle = YieldTermStructureHandle(curve)

# Hull White

hw_process = HullWhiteProcess(curveHandle, a, sigma)
rng = ql.GaussianRandomSequenceGenerator(ql.UniformRandomSequenceGenerator(steps, ql.UniformRandomGenerator()))
seq = ql.GaussianPathGenerator(hw_process, length, steps, rng, False)

# Interest Rate Generator

def generate_paths(n_scenarios):
    arr = np.zeros((n_scenarios, steps+1))
    for i in range(n_scenarios):
        sample_path = seq.next()
        path = sample_path.value()
        time = [path.time(j) for j in range(len(path))]
        value = [path[j] for j in range(len(path))]
        arr[i, :] = np.array(value)
    return np.array(time), arr

n_scenarios = 1
time, paths = generate_paths(n_scenarios)
rates = pd.DataFrame(paths).T
prices = np.empty_like(rates)

#price a zero coupon bond

def price(T, t, f0, rt):
    tau = T - t
    B = (1 - np.exp(-a * tau)) / a
    A = np.exp(-f0 * tau + B * f0 - sigma ** 2 / (4 * a ** 3) *
               (np.exp(-a * T) - np.exp(-a * t)) * (np.exp(2 * a * t) - 1))
    return A * np.exp(-rt * B)

for i in range(1, steps+1):
    prices[i] = price(length, dt * i, rate, rates.values[i])


print(prices)

plt.plot(prices)
plt.show()



    





