# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:52:05 2020

@author: aku
"""
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# matplotlib.use("pgf")
# matplotlib.rcParams.update({
#     "pgf.texsystem": "pdflatex",
#     'font.family': 'serif',
#     'text.usetex': True,
#     'pgf.rcfonts': False,
# })
matplotlib.rc('font', size=12)
matplotlib.rc('pdf', fonttype=42)

df = pd.read_csv('BKTData.csv', sep=';')
df['Date']= pd.to_datetime(df['Datum/Uhrzeit'], dayfirst=True)
a = df['Date'] - df['Date'][0]
df['Time'] =  a.dt.total_seconds()

start=0
end=17150
plt.close()
plt.plot(df['Time'].iloc[start:end]/(3600*24),df['Temperatur'].iloc[start:end], linewidth=1, markersize=0.5)#, linestyle='-.')
plt.xlabel('Time in days')
plt.ylabel('Temperature in °C')
plt.ylim(12.0, 55.0)
plt.xlim(-1, 15)
plt.yticks(np.arange(10, 60, 5))
plt.xticks(np.arange(0, 16, 2))
plt.grid(True)
plt.tight_layout()

plt.savefig('CCA.pdf')