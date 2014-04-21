#! /usr/bin/env python
# coding: utf-8
import pylab as pl
from datetime import datetime
import sys

filenames = sys.argv[1:]

for filename in filenames:
	identify = filename.split('_')[-2]
	
	#~ if there is mobile_online info
	mobile = False
	line = open(filename).readline()
	if len(line.split()) == 3: mobile = True

	#~ cycle
	times, users_online, mobiles_online = [], [], []
	for line in open(filename):
		if line:
			values = line.split()
			
			time = values[0]
			onlines = values[1]
			if mobile: mob_onlines = values[2]

			times.append(float(time))
			users_online.append(int(onlines))
			if mobile: mobiles_online.append(int(mob_onlines))


	times_dt = [datetime.fromtimestamp(it) for it in times]
	pl.xticks(rotation=30)
	pl.plot(times_dt, users_online, label=identify)
	if mobile: pl.plot(times_dt, mobiles_online, label=identify+' mobile')

legend = pl.legend(loc='best', shadow=True, ncol=len(filenames)*2, prop={'size':12})
# legend = pl.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), shadow=True, ncol=len(filenames)*2, prop={'size':12})
for label in legend.get_lines():
    label.set_linewidth(4)

pl.grid()
pl.show()
