# -*- coding: utf-8 -*-


import numpy as np

#entradas = np.array([[0,0],[0,1], [1,0], [1,1]])
#saidas = np.array([0,0,0,1])
#entradas = np.array([[0,0],[0,1], [1,0], [1,1]])
#saidas = np.array([0,1,1,1])

entradas = np.array([[1,1,1,0,1,0,0,1,0],[1,0,1,1,1,0,1,0,0],[0,1,0,1,1,1,0,1,0],[0,0,1,0,0,1,1,1,1],[1,1,0,0,1,0,0,1,1],[1,0,1,0,1,0,1,0,1],[0,1,0,1,0,1,1,0,1],[1,0,1,1,1,1,0,0,0],[0,1,1,0,0,0,1,1,1]])
                     
saidas = np.array([1,2,3,4,5,6,7,8,9])

pesos = np.array([0.0, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    return np.absolute( 10 / (1 + np.exp(-soma)))


def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = saidas[i] - saidaCalculada
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))
        
treinar()
print('Rede neural treinada')

while(True):

    my_array = []
    for i in range(9):
        my_array.append(float(input("Elemento:")))
    my_array = np.array(my_array)
    
    print(calculaSaida(np.floor(my_array)))


