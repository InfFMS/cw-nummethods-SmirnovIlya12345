import numpy as np
import matplotlib.pyplot as plt
# Задача 1
def pressure(V,T):
    R=8.314
    b=0.0000319
    a=0.1382
    return R*T/(V-b)-(a/(V**2))
# Первый график
x=np.linspace(0.0000419,0.001,1000)
x0=np.linspace(0.0000419,0.0001,500)
y_133=plt.plot(pressure(x,133),color='red')
y_143=plt.plot(pressure(x,143),color='red')
y_153=plt.plot(pressure(x,153),color='red')
y_163=plt.plot(pressure(x,163),color='red')
y_173=plt.plot(pressure(x,173),color='red')
plt.title('P-V diagram for O2')
plt.xlabel('Volume')
plt.ylabel('Pressure, 100 of atmospheres')
plt.show()
# Второй график
y0_133=plt.plot(pressure(x0,133),color='red')
y0_143=plt.plot(pressure(x0,143),color='red')
y0_153=plt.plot(pressure(x0,153),color='red')
y0_163=plt.plot(pressure(x0,163),color='red')
y0_173=plt.plot(pressure(x0,173),color='red')
plt.title('P-V diagram for O2')
plt.xlabel('Volume')
plt.ylabel('Pressure, 100 of atmospheres')
plt.show()
# Задача 2
dx=10**(-6)
extremes=[]
extremes2=[]
for i in range(50,1000):
    if (pressure(i*dx,143)-pressure((i+1)*dx,143))*(pressure((i+1)*dx,143)-pressure((i+2)*dx,143))<0:
        extremes.append(extremes.append(i*dx))
for i in range(len(extremes)):
    if extremes[i]!=None:
        extremes2.append(round(extremes[i],6))
print(extremes2)
# Задача 3
length_of_the_dead_zone=0
what=extremes2[1]-extremes2[0]
for i in range(1000):
    length_of_the_dead_zone+=np.sqrt((what/1000)**2+(pressure(extremes2[0]+i*what,143)-pressure(extremes2[0]+(i+1)*what,143))**2)
print(length_of_the_dead_zone)
# Задача 4
volume=10**(-6)
good_volumes=[0]
mister_pressure=3664187
# Проверка того, близко ли давление при каком-то объёме к необходимому
while True:
    if pressure(volume,143)>0.9999*mister_pressure and pressure(volume,143)<1.0001*mister_pressure and volume-good_volumes[-1]>10**(-6):
        good_volumes.append(round(volume,7))
    if volume>extremes2[1] and pressure(volume,143)<3640000:
        break
    volume+=10**(-8)
# Просто выкинуть 0
good_volumes_without_0=[]
for i in range(len(good_volumes)):
    if good_volumes[i]!=0:
        good_volumes_without_0.append(good_volumes[i])
print(good_volumes_without_0)
# Задача 5
integral_1=0
for i in range(1000):
    integral_1+=(good_volumes_without_0[2]-good_volumes_without_0[0])/1000*pressure(good_volumes_without_0[0]*i/1000+good_volumes_without_0[0]*(1000-i)/1000,143)
# Второй интеграл - просто прямоугольник
integral_2=(good_volumes_without_0[2]-good_volumes_without_0[0])*mister_pressure
print(integral_1,integral_2)
if abs(integral_1-integral_2)<integral_2*0.1:
    print("Maxwell's rule works!")