from itertools import permutations           
from itertools import combinations
import matplotlib.pyplot as plt
import time
def main():
    
    n = int(input('Insira o número de clientes: '))
    print("")
    t1 = time.time()
    arquivo = open('R101.txt','r')
    relatorio = open('relatório.txt','w')
    dados = []
    for i in arquivo:
        dados.append(i.strip())
    novaLista = []
    capacity = dados[4].split()
    capacidade = 80
    print ("A capacidade do veículo é ",capacidade)
    relatorio.write("Número de clientes: %d\n"%n)
    relatorio.write("\n")
    relatorio.write("Capacidade do veículo: %d\n"%capacidade)
    relatorio.write("\n")
    relatorio.write("\n")
    print("")
    for i in range (9, 10 + n):
        novaLista.append(dados[i].split())
   
    dadosFinais = []
    plt.plot(int(novaLista[0][1]),int(novaLista[0][2]),'ro')
    for i in range (len(novaLista)):
        linha = []
        for j in range (len(novaLista[0])):
            linha.append(int(novaLista[i][j]))
        if i > 0:
            plt.plot(linha[1],linha[2],'bo')
        dadosFinais.append(linha)
        
    #combinações
    lista = []
    for i in range(1,n+1):
        lista.append(dadosFinais[i][0])
    combina = []
    
    for m in range(1,len(lista)+1):
        for n in combinations(lista,m):
            combina.append(n)

    rotas = 0
    #Permutações e PCV
    
    tamanho = 0
    print("Tamanho das combinações em análise:")
    for tam in range (len(combina)):
        if len(combina[tam])>tamanho:
            tamanho = len(combina[tam])
            print(tamanho)
        somaDemanda = 0
        for i in range(len(combina[tam])):
            somaDemanda = somaDemanda + dadosFinais[combina[tam][i]][3]
        relatorio.write("Demanda da combinação %s é %d.\n"%(combina[tam],somaDemanda))

        if capacidade >= somaDemanda:
            relatorio.write("Combinação " + str(combina[tam]) + " é possível.\n")
            permut = list(permutations(combina[tam]))

            somaDist = 10000000000000000000000000000000
            for k in range(len(permut)):
                soma = ((dadosFinais[0][1]-dadosFinais[permut[k][0]][1])**2+(dadosFinais[0][2]-dadosFinais[permut[k][0]][2])**2)**0.5
                
                for j in range(len(permut[0])-1):
                    soma = soma + ((dadosFinais[permut[k][j+1]][1]-dadosFinais[permut[k][j]][1])**2+(dadosFinais[permut[k][j+1]][2]-dadosFinais[permut[k][j]][2])**2)**0.5
                soma = soma + ((dadosFinais[0][1]-dadosFinais[permut[k][len(permut[k])-1]][1])**2+(dadosFinais[0][2]-dadosFinais[permut[k][len(permut[k])-1]][2])**2)**0.5
                if soma < somaDist:
                    permutEscolhida = k
                    somaDist = soma
                    
            relatorio.write("A permutação escolhida é a " + str(permut[permutEscolhida]) + "\n")
            relatorio.write("O tamanho da rota é " + str(somaDist) + ".\n")
            X = [dadosFinais[0][1]]
            Y = [dadosFinais[0][2]]
            for j in range(len(permut[0])):
                X.append(dadosFinais[permut[permutEscolhida][j]][1])
                Y.append(dadosFinais[permut[permutEscolhida][j]][2])
            X.append(dadosFinais[0][1])
            Y.append(dadosFinais[0][2])
            plt.plot(X,Y,'-.')
            relatorio.write("A rota é: \n")
            relatorio.write(str(X) + "\n")
            relatorio.write(str(Y) + "\n")
            rotas = rotas + 1
            relatorio.write("\n")
        else:
            relatorio.write("Combinação " + str(combina[tam]) + " não é possível.\n")
            relatorio.write("\n")
    relatorio.write("Rotas construídas: " + str(rotas) + ".\n")
    relatorio.write("\n")
    t2 = time.time()
    relatorio.write("Tempo total de execução do programa: " + str(t2-t1) + "s.\n")
    print("Tempo total de execução do programa: " + str(t2-t1) + "s.\n")
    plt.show()
main()
