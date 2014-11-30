import numpy as math
dataset = [90.75,90.58,82.33,88.36,90.13,99.72,99.16,91.2,89.31,85.3,95.93,101.59,106.85,115.99,119.57]

def GetDataExp(values, window, target):
	weights = math.exp(math.linspace(-1., 0., window))
	weights = weights / weights.sum()
	a = math.convolve(values, weights)[:len(values)]
	a[:window] = a[window]
	b = [(2 * values[-1]) - a[-1], target - (2 * values[-1]) + a[-1]]
	return a




def GetDataSim(values, window, target):
	avg = []
	for i in range(len(values) - window):
		tot = 0
		for j in range(window):
			tot += values[i + j]
		avg.append(tot/window)
	b = [(2 * values[-1]) - avg[-1], target - (2 * values[-1]) + avg[-1]]
	return avg




expavg = GetDataExp(dataset, 2, 124.42)
mvavg = GetDataSim(dataset, 2, 124.42)
