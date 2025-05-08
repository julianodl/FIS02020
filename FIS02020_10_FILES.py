dir_dados = "/home/julianodl/work/disciplinas/fis02020/Dados/"

#%% 1. Escrevendo em um arquivo (modo texto)
file1 = dir_dados + "exemplo.txt"

with open(file1, "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")
    arquivo.write("Terceira linha\n")

#%% 2. Lendo aquivo linha por linha

with open(file1, "r") as arquivo:
    for linha in arquivo:
        #print(linha, end='')
        print(linha.strip())

#%% 3. Lendo todo conteúdo de uma vez

with open(file1, "r") as arquivo:
    conteudo = arquivo.read()
    
print(conteudo)
print(type(conteudo))

#%% 4 Acrescentando dados no final do arquivo

with open(file1, "a") as arquivo:
    arquivo.write("Mais uma linha.\n")
    
#%% 5 Lendo e escrevendo dados tabulares

import csv

file2 = dir_dados + "stars.csv"

with open(file2, "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    
    escritor.writerow(["Id", "DEC", "RA"])
    escritor.writerow(['star1', -30.001, 3.415])
    escritor.writerow(['star2', -29.232, 12.789])
    escritor.writerow(['star3', +40.123, 23.123])

#%%
with open(file2, "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

#%% 6 Lendo dados tabulares

file3 = dir_dados + "dados2.csv"

with open(file3, 'r') as fid:
    leitor = csv.reader(fid)
    matriz = []
    for linha in leitor:
        t = int(linha[0])
        x = float(linha[1])
        y = float(linha[2])
        matriz.append([t, x, y])
    
print(matriz)
        

#%% 
file3 = dir_dados + "dados2.csv"

with open(file3, 'r') as fid:
    leitor = csv.reader(fid)
    matriz = []
    for linha in leitor:
        row = [float(e) for e in linha]
        matriz.append(row)
        
print()    
print(matriz)



        