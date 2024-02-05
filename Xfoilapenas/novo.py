import subprocess
import os
import random

airfoil_name = "a44975"
gap = 0.01
distance = random.uniform(0,1)
raio = random.uniform(0.25,3) #raio é uma proporção entre o antigo perfil e o novo
local = random.uniform(0,1) # posição referente ao raio
thick = random.uniform(0.05,0.2)
camber = random.uniform(0.001,0.04)
max_thick = random.uniform(0,1) #posição onde a espessura é máxima
max_camber = random.uniform(0,1) #posição onde o camber é máximo
codigo = random.randint(00000,99999) #criar arquivos dat com nomes diferentes

if os.path.exists("polar_file.txt"):
    os.remove("polar_file.txt")

input_file = open("input_file.in", 'w')
input_file.write("\nPLOP\nG\n\n")
if "NACA" in airfoil_name:
    input_file.write("{0}\n".format(airfoil_name))
else:
    input_file.write("LOAD {0}.dat\n".format(airfoil_name))

input_file.write("GDES\n")
input_file.write("TGAP {0} {1} \n".format(gap, distance))
input_file.write("LERA {0} {1} \n".format(raio, local))
input_file.write("TSET {0} {1}\n".format(thick, camber))
input_file.write("HIGH {0} {1}\n".format(max_thick, max_camber))
input_file.write("EXEC\n\n")
input_file.write("PPAR\n")
input_file.write("n\n")
input_file.write("120\n\n\n")
input_file.write("SAVE\n a{0}.dat\n".format(codigo))
input_file.write("ANNO\n\n")
input_file.write("HARD\n")
input_file.write("\n\n")
input_file.write("OPER\n")
input_file.write("VISC\n")
input_file.write("500000\n")
input_file.write("PACC\n")
input_file.write("polar_file.txt\n")
input_file.write("ITER 100\n")
input_file.write("alfa 3\n")
input_file.write("\n\n")


input_file.write("QUIT\n")
input_file.close()


subprocess.call("xfoil.exe < input_file.in", shell = True)
print("raio:{0}".format(raio))
print(local)
print(gap)
print(distance)
print(thick)
print(camber)
print(max_thick)
print(max_camber)