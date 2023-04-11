import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import gridspec
import pandas as pd
from modelicares import SimRes

from matplotlib import rc

font = {'size'   : 24}

# matplotlib.rc('font', **font)
matplotlib.rc('font', size=20)
# matplotlib.rc('font', **{'family':'sans-serif'})
# matplotlib.rc('font', **{'family':'sans-serif','sans-serif':['Helvetica']})
# matplotlib.rc('text', usetex=True)
matplotlib.rc('pdf', fonttype=42)

# fm = matplotlib.font_manager.json_load("C:/Users/Markus/.matplotlib/fontlist-v310.json")
# fm.findfont("serif", rebuild_if_missing=False)
# fm.findfont("serif", fontext="afm", rebuild_if_missing=False)

# Get the simulation result
sim = SimRes(r'.\200714_hall_real_calibration.mat')

times = sim["Time"].values() / 3600

ls = ["-", "--", "-.", "-", "--", "-.", "-", "--", "-.", "-", "--", "-."]

fig = plt.figure(figsize=(15,15))

gs = gridspec.GridSpec(3, 3)

plt.subplots_adjust(hspace = 0.5)

l = len(times)

ax = fig.add_subplot(311)
ax.plot(times, sim["hallBaseClass.hallTemperature"].values(), label="Hall temperature simulation")
ax.plot(times, sim["weather.y[4]"].values(), label="Hall temperature measurement", linestyle = "--")
ax.set_ylabel("Temperature in °C")
mi = 18
ma = 26
ax.set_ylim(mi, ma)
ax.set_yticks(np.arange(mi, ma, 2))
ax.grid()

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
        ncol=3, borderaxespad=0.)

ax = fig.add_subplot(312)
ax.plot(times, sim["weather.y[7]"].values(), label="TABS meas.")
ax.plot(times, sim["weather.y[3]"].values(), label="Outdoor meas.", linestyle = "--")
ax.plot(times, sim["weather.y[5]"].values(), label="Supply air meas.", linestyle = "--")
ax.set_ylabel("Temperature in °C")
mi = 0
ma = 35
ax.set_ylim(mi, ma)
ax.set_yticks(np.arange(mi, ma, 5))
ax.grid()

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
        ncol=3, borderaxespad=0.)


ax = fig.add_subplot(313)
ax.plot(times, sim["hallBaseClass.FloorConductor.port_a.Q_flow"].values() / 1000., label="TABS heat flux simulation")

ax.set_ylabel("Heat flux in kW")
mi = -10
ma = 30
ax.set_ylim(mi, ma)
ax.set_yticks(np.arange(mi, ma, 10))
ax.grid()

ax.set_xlabel("Time in hours")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
        ncol=3, borderaxespad=0.)

#plt.show()
plt.tight_layout()
plt.savefig(r'.\200714_hall_real_calibrationSlim2.pdf')



