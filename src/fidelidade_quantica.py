import numpy as np
import quantum_gaussian_toolbox as qgt

# Verificar se a matriz resultante é não negativa definida (σ >= 0):
def check_condition(matriz):
    eigenvalues = np.linalg.eigvalsh(matriz) # Calcular os autovalores de uma matriz simétrica
    return all(eig >= 0 for eig in eigenvalues) # Verificar se todos os autovalores são não negativos

# Exemplo de uso:
sigma = np.eye(4)  # Matriz de covariancia | Definindo matriz identidade 4x4

sigma_cov = 10 * sigma  # Matriz de covariancia para o estado 0 (apenas parte real)

if check_condition(sigma_cov):
    print("A condição é satisfeita.")
else:
    print("A condição não é satisfeita.")

# Fidelidade Quântica

R = np.array([1, 2, 3, 4])  # Vetor médio de quadratura para o estado 0, sempre positivo
alpha = 1 - 2.0j  # Representacao de um numero complexo.

# Definição dos estados:

estado_0 = qgt.gaussian_state(R, sigma_cov)  # Estado Gaussiano Multimodo
estado_1 = qgt.coherent(alpha)

estado_2 = qgt.tensor_product([estado_1, estado_1])
estado_1.tensor_product([estado_1])

F = qgt.fidelity(estado_0, estado_1)

print(F)