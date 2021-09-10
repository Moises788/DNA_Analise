# O seguinte código realiza a crianção de dois genes fictícios e imprime o seu código genético 
# em dois arquivos.txt distintos

import random

nucleotidios = ['a','t','c','g']

gene = open("date/gene.txt", "w")

for i in range(20):
    for n in range(100):
        gene.write(random.choice(nucleotidios))      
    gene.write("\n")
gene.close