import matplotlib.pyplot as plt 
import numpy as np  
from random import randint
import subprocess

c = randint(1,3)
b = randint(3,10)


t1 = np.linspace(0, np.pi/2, 50)

x1 = b * np.cos(t1)
y1 = c * np.sin(t1)


t2 = np.linspace(3 * np.pi/2, 2* np.pi, 50)
x2 = b * np.cos(t2)
y2 = 3 * c * np.sin(t2)

plt.plot(x1,y1)
plt.plot(x2,y2)


sec = [] # sec = a posição x da seção
resultado = 0

for i in range (0,6):
    if i == 0:
        resultado = 0.
        sec.append(resultado)
    else:
        resultado+= b * 0.5 ** i  
        sec.append(resultado)
print(sec)


y2_inter = np.interp(sec, x2, y2) #y2_inter é a posição y inferior da seção


y1_inter = []

for val in sec:
    if abs(val) < b:
        xd = c * np.sqrt(1 - (val / b)**2)
        y1_inter.append(xd)
       

#print(y1_inter)

plt.scatter(sec, y1_inter)
plt.scatter(sec, y2_inter)



#offset = Xi - X1

y_shifter = []
for n in range(0,5):
    y_shifter.append(y1_inter[n]-y1_inter[0])
offset = list(np.round(y_shifter, 4))
print('Offset de cada secao: ', offset)


corda = []

for i in range(0,5):
    cd = abs(y2_inter[i]-y1_inter[i])
    corda.append(cd)
print(corda)
#calcular a área da meia asa (trapezio): B+b*h/2

S_total = 0
# Calcula a área de cada seção
for i in range(len(sec) - 1):
    # Calcula as bases B e b de cada seção
    B = abs(y2_inter[i] - y1_inter[i])
    b = abs(y2_inter[i + 1] - y1_inter[i + 1])
    # Calcula a altura h
    h = sec[i + 1] - sec[i]
    # Calcula a área do trapézio e adiciona à área total
    S_total += (B + b) * h / 2

print('Area total da asa: {0:.3f}m^2'.format(S_total*2))
#alongamnto = b²/S
AR = (2*b**2) / (S_total * 2)
print('Alongamento da asa: {0:.3f}'.format(AR))
                
plt.show()

avl = open('elipse.avl', 'w')
avl.write('elipse' + '\n')
avl.write('0.0\n')          # Mach
avl.write('0 0 0.0\n') # IYsym   IZsym   Zsym
avl.write('%.2f %.2f %.2f\n' % (S_total*2, corda[1], sec[5]*2)) # Sref    Cref    Bref
avl.write('%.3f 0.0 0.0\n' % (corda[0]/3)) # Xref    Yref    Zref 
avl.write("\nSURFACE\n")
avl.write("Asa\n")
avl.write("12 1.0 22 1.0\n") # Discretização
avl.write("TRANSLATE\n")
avl.write("0.0 0.0 0.0\n")
avl.write("YDUPLICATE\n0.0\n")
avl.write("ANGLE\n0.0\n")
avl.write("COMPONENT\n1\n")
for s in range(0,5):
    avl.write("SECTION\n")
    avl.write("%.2f %.2f 0.0 %.2f 0.0\n" % (offset[s], sec[s], corda[s])) # Xle    Yle    Zle     Chord   Ainc
    avl.write("NACA\n2412\n")
avl.close()

f= open('original.avl','w')
f.write("LOAD elipse.avl\n")
f.close()

subprocess.call("avl.exe < original.avl", shell = True)