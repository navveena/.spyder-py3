import numpy as np
import matplotlib.pyplot as plt
Data=[[5.,25.,45.,20.],[8.,13.,29.,27.],[9.,29.,27.,39.]]


X=np.arange(4)
plt.plot(X,Data[0],color='b',label='data1')
plt.plot(X,Data[1],color='g',label='data2')
plt.plot(X,Data[2],color='r',label='data3')


plt.legend(loc='upper left')
plt.title('LINE CHART DEMO')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig("c:\\intel.pdf")
plt.show()
