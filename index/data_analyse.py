import numpy as np
import matplotlib
import matplotlib.pyplot as plt

gene = open("date/gene.txt").read()
gene = gene.replace("\n","")

mapeamento = {} 

for i in ['a', 't', 'c', 'g']: 
    for j in ['a', 't', 'c', 'g']:
        mapeamento[i+j] = 0

for i in range(len(gene)-1):
    mapeamento[gene[i]+gene[i+1]] += 1

print(mapeamento)
mapeamento_lista = mapeamento.values()
mapeamento_lista = list(mapeamento_lista)

vegetables = ["A", "T", "C", "G"]
farmers = ["A", "T", "C","G"]

harvest = np.array([[mapeamento_lista[0],mapeamento_lista[1], mapeamento_lista[2], mapeamento_lista[3],],
                    [mapeamento_lista[4], mapeamento_lista[5], mapeamento_lista[6], mapeamento_lista[7],],
                    [mapeamento_lista[8],mapeamento_lista[9], mapeamento_lista[10], mapeamento_lista[11],],
                    [mapeamento_lista[12], mapeamento_lista[13], mapeamento_lista[14], mapeamento_lista[15],]])


fig, ax = plt.subplots()
im = ax.imshow(harvest)

# We want to show all ticks...
ax.set_xticks(np.arange(len(farmers)))
ax.set_yticks(np.arange(len(vegetables)))
# ... and label them with the respective list entries
ax.set_xticklabels(farmers)
ax.set_yticklabels(vegetables)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Pares de nucleotídios em uma molécula de DNA")
fig.tight_layout()
plt.show()
