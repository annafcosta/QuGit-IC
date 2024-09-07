import numpy as np
import quantum_gaussian_toolbox as qgt

# Verificar se a matriz resultante é não negativa definida (σ + iΩ ≥ 0):
def check_condition(matrix):
    matrix_real = matrix.real
    eigenvalues = np.linalg.eigvals(matrix_real)
    return all(eig >= 0 for eig in eigenvalues)

def main():

    # Aplicação para matrizes aleatórias:
    sigma = np.random.rand(4, 4) # Matriz gerada
    print(sigma)
    sigma_cov = 10 * sigma  # Matriz de covariancia para o estado 0

    if check_condition(sigma_cov):
        print("\nA condição é satisfeita.")
    else:
        print("\nA condição não é satisfeita.")

    # Fidelidade Quântica

    R = np.array([1, 2, 3, 4])  # Vetor médio de quadratura para o estado 0, sempre positivo
    alpha = 1 - 2.0j  # Representação de um número complexo.

    # Definição dos estados:
    estado_0 = qgt.gaussian_state(R, sigma_cov)  # Estado Gaussiano Multimodo
    estado_1 = qgt.coherent(alpha)

    if not check_condition(sigma_cov):
        print("Não é possível calcular a fidelidade.")
        return

    estado_2 = qgt.tensor_product([estado_1, estado_1])
    estado_1.tensor_product([estado_1])

    F = qgt.fidelity(estado_0, estado_2)

    print("Fidelidade:", F)

main()
