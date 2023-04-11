import pickle 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager
from matplotlib import gridspec
import pandas as pd


#matplotlib.rcParams['backend'] = 'pdf'

from matplotlib import rc

font = {'size'   : 24}

# matplotlib.rc('font', **font)
matplotlib.rc('font', size=24)
# matplotlib.rc('font', **{'family':'sans-serif'})
# matplotlib.rc('font', **{'family':'sans-serif','sans-serif':['Helvetica']})
# matplotlib.rc('text', usetex=True)
matplotlib.rc('pdf', fonttype=42)

ls = ["-", "--", "-.", "-", "--", "-.", "-", "--", "-.", "-", "--", "-."]

fig = plt.figure(figsize=(20,20))

gs = gridspec.GridSpec(3, 3)

plt.subplots_adjust(hspace = 0.6)

with open(r"200917_data.PICKLE", 'rb') as f:
    data = pickle.load(f)

with open(r"setpoint.PICKLE", 'rb') as f:
    setpoint = pickle.load(f)

ax = fig.add_subplot(311)

df = data[0]
ax.plot(df.index.values, df["Value"].values, label=r"Extract air temperature")

l = len(df.index.values)

ax.plot(df.index.values, setpoint, label=r"Hall temperature setpoint", linestyle = "--")
ax.set_ylabel("Temperature in °C")
mi = 17
ma = 27
ax.set_ylim(mi, ma)
ax.set_yticks(np.arange(mi, ma, 2))
ax.grid()


plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=3,borderaxespad=0.)


ax = fig.add_subplot(312)
df = data[1]
ax.plot(df.index.values, df["Value"].values, label=r"Supply air temperature")

df = data[2]
ax.plot(df.index.values, df["Value"].values, label=r"Supply air temperature setpoint", linestyle = "--")

mi = 14
ma = 27
ax.set_ylim(mi, ma)
ax.set_yticks(np.arange(mi, ma, 2))
ax.set_ylabel("Temperature in °C")
ax.grid()

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=3, borderaxespad=0.)


ax = fig.add_subplot(313)
df = data[3]
ax.plot(df.index.values, df["Value"].values, label=r"TABS temperature setpoint")

df = data[4]
ax.plot(df.index.values, df["Value"].values, label=r"Outdoor air temperature", linestyle = "--")
ax.set_ylabel("Temperature in °C")
mi = 5
ma = 25
ax.set_ylim(mi, ma)
ax.set_yticks(np.arange(mi, ma, 5))
ax.grid()

ax.set_xlabel("Time in hours")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=3, borderaxespad=0.)

plt.tight_layout()
plt.savefig('200714_hall_real_control_shortSlim.pdf')




