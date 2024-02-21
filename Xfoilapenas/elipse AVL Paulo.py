#####################################################################################
#------------Codigo desenvolvido por Paulo Robson - Fevereiro de 2024---------------#
#####################################################################################

#import matplotlib.pyplot as plt
import numpy as np
from random import randint

c = randint(5, 15)/100 #0.75 <-- valor aleatório // c stands for Chord
b = 1.2 #5.0 <-- valor aleatório // b stands for Span ***ATENÇÃO!!! O CÓDIGO GERA MEIA ASA*** (mas no AVL ele duplica)

# FUNÇÃO DE PI À POTÊNCIA 0.5^i   (valores em radiano)
p = 0 #power function
posi_b = 0 #posição na envergadura
parametro1 = []
parametro2 = []
span_points = []
for i in range(1,6): # 5 seções
    p = (1/(2 ** i))
    posi_b += p
    span_points.append(posi_b * b) # posi_b é função para o circulo unitário
    theta1 = np.arccos(posi_b) # angulos no priemiro quadrante
    parametro1.insert(0,theta1)
    theta2 = 2 * np.pi - theta1 # angulos no quarto qudrante
    parametro2.append(theta2)
span_points.insert(0,0.0) # insere o valor 0 no inicio da lista (posição inicial)
Span = list(np.round(span_points, 4))

parametro1.append(np.arccos(0)) # insere o valor para a posição 0 ja que a função não calcula
parametro2.insert(0,2 * np.pi - np.arccos(0)) # aqui tambem insere o 0
print('Posicoes Y da envergadura:',Span)

x1 = b * np.cos(parametro1)
y1 = c * np.sin(parametro1) # 1/4 superior da corda

x2 = b * np.cos(parametro2)
y2 = 3 * c * np.sin(parametro2) # 3/4 inferior da corda


#------------------plotagem-----------------------#
#plt.plot([x1[5],x2[0]],[y1[5],y2[0]], color = 'k')
#plt.plot([x1[0],x2[5]],[y1[0],y2[5]], color = 'k')
#plt.plot(x1,y1,'-k')
#plt.plot(x2,y2,'-k')


#1 - PROXIMO PASSO É DETERMINAR O TAMANHO DE CADA CORDA (OK) ;
#2 - A SUA DISPOSIÇÃO NA ENVERGADURA *easy* ;
#3 - e os offsets de cada seção (OK) PARAR DAR O INPUT NO AVL.
y1reversed = []
for j in reversed(range(0,6)):
    y1reversed.append(y1[j])
print(y1reversed)
corda = []
for k in range(0,6):
    corda.append(y1reversed[k] + abs(y2[k]))
chord = list(np.round(corda, 4))
print('Cordas:',chord)

# OFFSET = Xi - X1
x_shifter = []
for n in range(0,6):
    x_shifter.append(y1[n] - y1[0])
offset = list(np.round(x_shifter, 4))  # kkkk "deslocador" coloquei isso só pra mudar o nome
print('Offset de cada secao:',offset)

# CALCULAR A ÁREA DA MEIA ASA formula --> trapézio = (B + b)*h/2
S = 0
h = 0
S_total = 0
for z in range(0,5):
    S = (chord[z] + chord[z+1]) * (Span[z+1] - h) / 2
    h = Span[z+1]
    S_total += S # Area total da meia asa
print('Area da asa: {0:.3f} m^2'.format(S_total*2)) # Area total da asa inteira

AR = ((Span[5]*2) ** 2) / (S_total*2) # Span(asa)^2/Area(asa) ASA INTEIRA
print('Alongamento da asa: {0:.3f}'.format(AR))

#plt.axis('equal') usado inicialmente para a plotagem

#plt.show() usado inicialmente para a plotagem

# ULTIMA ETAPA É IMPORTAR OS VALORES PRO AVL \o/
#                                            ||
avl = open('elipse.avl', 'w')
avl.write('elipse' + '\n')
avl.write('0.0\n')          # Mach
avl.write('0 0 0.0\n') # IYsym   IZsym   Zsym
avl.write('%.2f %.2f %.2f\n' % (S_total*2, chord[1], Span[5]*2)) # Sref    Cref    Bref
avl.write('%.3f 0.0 0.0\n' % (chord[0]/3)) # Xref    Yref    Zref 
avl.write("\nSURFACE\n")
avl.write("Asa\n")
avl.write("12 1.0 22 1.0\n") # Discretização
avl.write("TRANSLATE\n")
avl.write("0.0 0.0 0.0\n")
avl.write("YDUPLICATE\n0.0\n")
avl.write("ANGLE\n0.0\n")
avl.write("COMPONENT\n1\n")
for s in range(0,6):
    avl.write("SECTION\n")
    avl.write("%.2f %.2f 0.0 %.2f 0.0\n" % (offset[s], Span[s], chord[s])) # Xle    Yle    Zle     Chord   Ainc
    avl.write("NACA\n2412\n")
avl.close()
