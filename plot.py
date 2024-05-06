import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

oldTime = pd.read_csv('old.csv')
newTime = pd.read_csv('new.csv')

numreg = re.compile(r'\d+\.\d+')

oldt = round(float(re.findall(numreg, list(oldTime)[0])[0]) / 1000, 2)
newt = round(float(re.findall(numreg, list(newTime)[0])[0]) / 1000, 2)

x = ["old", "new"]
y_line = [223, 134]
y_time = [oldt, newt]

fig, axs = plt.subplots(1, 2, sharex=False, sharey=False)
ind = np.arange(len(x))
axs[0].bar(x, y_line)
for i in range(len(x)):
  axs[0].text(i, y_line[i] + 1, y_line[i], ha = 'center')


axs[1].bar(x, y_time)
for i in range(len(x)):
  axs[1].text(i, y_time[i] + 0.05, y_time[i], ha = 'center')

axs[0].set(xlabel='code generator', ylabel='generated code size (#Loc)')
axs[1].set(xlabel='code generator', ylabel='generated code execution time (s)')

fig.suptitle('Comparison of generated code for the Rhyme solution of\n Advent of Code day5-part1')

plt.savefig("evaluation.pdf")