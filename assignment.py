import matplotlib.pyplot as plt
import math as mth

x_axis=[]
y_axis=[]
for i in range(1,160):
    x_axis.append(i)
    frequency=1/(2*mth.pi*mth.sqrt(5*(10**-9)*(1.6*10**-19)/i))
    y_axis.append(frequency)

plt.xlabel("Voltage(V)")
plt.ylabel("Frequency")
plt.title("Graphof Frequecy aginst voltage")
plt.plot(x_axis,y_axis)
plt.show()