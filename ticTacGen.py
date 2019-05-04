
import numpy as np

entradas = []
saidas = []
pesos = []

def getWinner(board):
    if (win_check(board, 1)):
        return 1
    elif (win_check(board, 2)):
        return 2
    return 0

def win_check(arr, char): 
    matches = [[0, 1, 2], [3, 4, 5], 
               [6, 7, 8], [0, 3, 6], 
               [1, 4, 7], [2, 5, 8], 
               [0, 4, 8], [2, 4, 6]] 
  
    for i in range(8): 
        if(arr[matches[i][0]] == char and
            arr[matches[i][1]] == char and
            arr[matches[i][2]] == char): 
            return True
    return False

c = 0;
while (c < 262144):
    valid = (c & 3) < 3
    valid &= ((c >>  2) & 3) < 3
    valid &= ((c >>  4) & 3) < 3
    valid &= ((c >>  6) & 3) < 3
    valid &= ((c >>  8) & 3) < 3
    valid &= ((c >> 10) & 3) < 3
    valid &= ((c >> 12) & 3) < 3
    valid &= ((c >> 14) & 3) < 3
    valid &= ((c >> 16) & 3) < 3

    if valid:
        i = c
        j = 0
        ttmp = []
        while j < 9:
            ttmp.append(i & 3)
            i >>= 2
            j += 1

        entradas.append(ttmp)
        saidas.append(getWinner(ttmp))
        pesos.append(0.0)
    c += 1

print(len(entradas))

taxaAprendizagem = 0.1
entradas_np = np.array(entradas)
saidas_np = np.array(saidas)
pesos_np = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

def stepFunction(soma):
    return np.absolute( 10 / (1 + np.exp(-soma)))


def calculaSaida(registro):
    s = registro.dot(pesos_np)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas_np)):
            saidaCalculada = calculaSaida(np.asarray(entradas_np[i]))
            erro = saidas_np[i] - saidaCalculada
            erroTotal += erro
            for j in range(len(pesos_np)):
                pesos_np[j] = pesos_np[j] + (taxaAprendizagem * entradas_np[i][j] * erro)
        print('Total de erros: ' + str(erroTotal))
        
treinar()
print('Rede neural treinada')

while(True):

    my_array = []
    for i in range(9):
        my_array.append(float(input("Elemento:")))
    my_array = np.array(my_array)
    
    print(calculaSaida(np.floor(my_array)))
