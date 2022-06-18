import numpy as np
matriz = np.array([
    ['Nome', 'Tipo', 'Barbeiro', 'Dia da Semana', 'Horarios'],
    ['Bernardo', 'Completo', 'Barbeiro 1', 'Segunda', '14:00']
])

linha = np.array([7,8,9])

numero_linha = matriz.shape[0] ##last row

matriz = np.insert(matriz, 0,[linha],axis= 1)

print(matriz.shape[0])