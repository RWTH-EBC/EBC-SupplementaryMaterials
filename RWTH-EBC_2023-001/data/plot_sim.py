import pickle 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import gridspec
import pandas as pd
from sklearn.metrics import mean_squared_error

# font = {'family' : 'normal',
#         'weight' : 'normal',
#         'size'   : 18}

# matplotlib.rc('font', **font)
matplotlib.rc('font', size=42)
matplotlib.rc('pdf', fonttype=42)

lw = 5

#plt.rcParams["figure.figsize"] = (20,30)

# Get the simulation result
with open(r"./result.PICKLE", 'rb') as f:
    sim_seq = pickle.load(f)

sim_seq["hallFloor"] = []
sim_seq["hallFloor_ref"] = []

for s in sim_seq["hall.hallBaseClass.floor.thermCapExt[1].port.T"]:
       sim_seq["hallFloor"].append(s - 273.15)

for s in sim_seq["hall_ref.hallBaseClass.floor.thermCapExt[1].port.T"]:
        sim_seq["hallFloor_ref"].append(s - 273.15)

times = [s / 3600. for s in sim_seq["SimTime"]]
xlim = 36

ls = ["-", "--", "-.", "-", "--", "-.", "-", "--", "-.", "-", "--", "-."]

fig = plt.figure(figsize=(20,20))

gs = gridspec.GridSpec(4, 4)

plt.subplots_adjust(hspace = 0.6)

l = len(times)
setpoint = [23.02] * l

ax = fig.add_subplot(411)

ax.title.set_text('Hall')
ax.plot(times, sim_seq["T_hall"], label="BExMoC", linewidth=lw)
ax.plot(times, sim_seq["T_hall_ref"], label="Benchmark", linestyle = "--", linewidth=lw)
ax.plot(times, setpoint, label="setpoint", color = 'k', linestyle = ":", linewidth=lw)

rmse = (mean_squared_error(y_true=setpoint, y_pred=sim_seq["T_hall"])**0.5)
average =  sum(sim_seq["T_hall"]) / len(sim_seq["T_hall"])

print(f"BExMoC RMSE: {rmse}")
print(f"BExMoC average: {average}")

rmse = (mean_squared_error(y_true=setpoint, y_pred=sim_seq["T_hall_ref"])**0.5)
average =  sum(sim_seq["T_hall_ref"]) / len(sim_seq["T_hall_ref"])


print(f"Benchmark RMSE: {rmse}")
print(f"Benchmark average: {average}")

ax.set_ylabel("Temperature in °C")
mi = 20.0
ma = 25
ax.set_ylim(mi, ma)
ax.set_xlim(0, xlim)
ax.set_yticks(np.arange(mi, ma, 1))

plt.legend(loc='lower left',
        ncol=3, borderaxespad=0.)

ax2 = ax.twinx()
ax2.plot(times, sim_seq["weatherCelsius.Celsius"], label="outdoor temperature (right axis)", linestyle = "-.", color = 'g', linewidth=lw)

mi = 0
ma = 10
ax2.set_ylim(mi, ma)
ax2.set_yticks(np.arange(mi, ma, 2))
ax2.set_ylabel("Temperature in °C")
ax2.grid()

plt.legend(loc='lower right',
        ncol=1, borderaxespad=0.)

ax = fig.add_subplot(412)
ax.title.set_text('Air handling unit')
ax.plot(times, sim_seq["T_in1"], label="BExMoC", linestyle = "-", linewidth=lw)
ax.plot(times, sim_seq["T_AHU_ref.y[1]"], label="Benchmark", linestyle = "--", linewidth=lw)

ax.set_ylabel("Temperature in °C")
mi = 15
ma = 27
ax.set_ylim(mi, ma)
ax.set_xlim(0, xlim)
ax.set_yticks(np.arange(mi, ma, 2))
ax.grid()

plt.legend(loc='lower left',
        ncol=4, borderaxespad=0.)

ax = fig.add_subplot(413)
ax.title.set_text('Thermally activated building system')
ax.plot(times, sim_seq["hallFloor"] , label="BExMoC", linestyle = "-", linewidth=lw)
ax.plot(times, sim_seq["hallFloor_ref"] , label="Benchmark", linestyle = "--", linewidth=lw)

ax.set_ylabel("Temperature in °C")
mi = 20
ma = 28
ax.set_ylim(mi, ma)
ax.set_xlim(0, xlim)
ax.set_yticks(np.arange(mi, ma, 2))
ax.grid()

plt.legend(loc='lower left',
        ncol=2, borderaxespad=0.)


ax = fig.add_subplot(414)

ax.title.set_text('Reheater/recooler')
ax.plot(times, sim_seq["hall.conPID.y"], label="BExMoC", linestyle = "-", linewidth=lw)
ax.plot(times, sim_seq["hall_ref.conPID.y"], label="Benchmark", linestyle = "--", linewidth=lw)
mi = -4
ma = 4
ax.set_ylim(mi, ma)
ax.set_yticks(np.arange(mi, ma, 1))
ax.set_ylabel("Temperature \ndifference in K")
ax.set_xlabel("Time in hours")
ax.grid()

plt.legend(loc='lower left',
        ncol=2, borderaxespad=0.)

print("total: " + str(sim_seq["energy"][-1] / sim_seq["energy_ref"][-1] - 1))
print("AHU: " + str(sim_seq["AHU_energy.y"][-1] / sim_seq["AHU_energy_ref.y"][-1] - 1))
print("hall: " + str(sim_seq["hall.hallEnergy"][-1] / sim_seq["hall_ref.hallEnergy"][-1] - 1))
print("office1: " + str(sim_seq["office.energy"][-1] / sim_seq["office.energy_ref"][-1] - 1))
print("office2: " + str(sim_seq["office2.energy"][-1] / sim_seq["office2.energy_ref"][-1] - 1))
print("hall.reheater: " + str(sim_seq["hall.reheaterEnergy"][-1] / sim_seq["hall_ref.reheaterEnergy"][-1] - 1))

fig = plt.gcf()
fig.tight_layout()
fig.set_size_inches(38.0, 36.0)
plt.subplots_adjust(hspace = 0.3)
fig.tight_layout()

plt.savefig('210730_hall_sim_bexmoc.pdf')

plt.show()