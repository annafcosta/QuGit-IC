import numpy as np
import quantum_gaussian_toolbox as qgt

# aplicar uma condicao para a matriz, pag 33. Tem que ser simetrica
# forma simplética. conferir se é fisicamente aceitavel

R = np.array([1, 2, 3, 4])  # Vetor médio de quadratura para o estado 0, sempre positivo
M = np.eye(4)  # Matriz de covariancia | Definindo matriz identidade 4x4

V = 10 * M  # Matriz de covariancia para o estado 0
alpha = 1 - 2.0j  # Representacao de um numero complexo.

estado_0 = qgt.gaussian_state(R, V)  # Estado Gaussiano Multimodo

estado_1 = qgt.coherent(alpha)

estado_2 = qgt.tensor_product([estado_1, estado_1])
estado_1.tensor_product([estado_1])

F = qgt.fidelity(estado_0, estado_1)

print(F)

