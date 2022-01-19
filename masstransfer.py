#!/usr/bin/env python3.6

import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

M1 = 5
M2 = 4
M = M1 + M2
alpha = [0.5, 1.0, 2.0]
beta = [1.0, 0.8, 0.5]

fig, (ax0, ax1) = plt.subplots(nrows=2)
fig.set_size_inches(12,10, forward=True)
cc = ['red', 'green', 'blue'] #(cycler(color=list('rgb')))
cl = (cycler(linestyle=['-', '--', '-.']))
ax0.invert_xaxis()
ax1.invert_xaxis()

k=200
dM = -0.01
DM = np.zeros(k)
FI = np.zeros(k)
for i in range(k):
	DM[i]= dM
	FI[i] = ((M1 + dM) * (M2 - dM) / M1 / M2) ** -2
	dM += -0.01
ax0.plot(DM, FI, label='Conservative', color='yellow')
ax1.plot(DM, FI, label='Conservative', color='yellow')

#ax0.set_prop_cycle(cc)
for a in range(3):
	ax0.set_prop_cycle(cl)
	ax1.set_prop_cycle(cl)
	for b in range(3):
		dM = -0.01
		DM = np.zeros(k)
		FI = np.zeros(k)
		ncons1 = np.zeros(k)
		ncons2 = np.zeros(k)
		for i in range(k):
			DM[i]= dM
			ncons1[i] = ((M1 + dM) * (M2 - beta[b] * dM) / M1 / M2) ** (-2) * ((M + dM * (1 + beta[b])) / M) ** (2 * alpha[a] + 1)
			ncons2[i] = ((M + dM * (1 + beta[b])) / M) * ((M1 + dM) / M1) ** (2 * alpha[a] * (1 - beta[b]) - 2) * ((M2 - dM * beta[b]) / M2) ** (((-2) * alpha[a] * (1 - beta[b]) / beta[b]) - 2)
			dM += -0.01
		ax0.plot(DM, ncons1, label='a=%.1f, b=%.1f' %(alpha[a], beta[b]), color='%s'%cc[a])
		ax1.plot(DM, ncons2, label='a=%.1f, b=%.1f' %(alpha[a], beta[b]), color='%s'%cc[a])
ax0.set_xlabel('Mass loss from heavier star(dM) [Solar masses]', fontsize='x-large')
ax0.set_xlim([-0.01, -2])
ax0.set_ylabel('A_F/A_I', fontsize='x-large')
ax0.set_title('Conservative vs first non-conservative', fontsize='xx-large')
ax0.legend()

ax1.set_xlabel('Mass loss from heavier star(dM) [Solar masses]', fontsize='x-large')
ax1.set_xlim([-0.01, -2])
ax1.set_ylabel('A_F/A_I', fontsize='x-large')
ax1.set_title('Conservative vs second non-conservative', fontsize='xx-large')
ax1.legend()
plt.tight_layout()
fig.savefig('FI.png')
plt.show()
