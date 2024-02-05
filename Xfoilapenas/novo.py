import subprocess
import os
import random

airfoil_name = "NACA2412" #nome do arquivo ".dat" para o xfoil ler ou o próprio NACA
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

input_file = open("input_file.in", 'w') #cria um arquivo e escreve os comandos dentro do xfoil
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

#tudo que foi feito no arquivo que simula o xfoil vai ser levado pro próprio xfoil
subprocess.call("xfoil.exe < input_file.in", shell = True)
#só para ver quais foram os valores dos parâmetros
print("raio:{0}".format(raio)) 
print("raio:{0}".format(raio))
print("local:{0}".format(local))
print("gap:{0}".format(gap))
print("distance:{0}".format(distance))
print("thick:{0}".format(thick))
print("camber:{0}".format(camber))
print("max_thick:{0}".format(max_thick))
print("max_camber: {0}".format(max_camber))
