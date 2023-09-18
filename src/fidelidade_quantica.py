import numpy as np
import quantum_gaussian_toolbox as qgt

vac = qgt.vacuum()  # Variável para estado no vácuo;
coh = qgt.coherent(1 - 20j)  # Variável para estado coerente;
sq = qgt.squeezed(1.2)  # Estado comprimido
th = qgt.thermal(4)  # Estádo térmico

R = np.array([1, 2, 3, 4])  # Vetor médio de quadratura
M = np.eye(4)  # Matriz de covariância | Definindo matriz identidade 4x4

V = 10 * M
alpha = 1 - 2.0j  # Representação de um número complexo.

state_0 = qgt.gaussian_state(R, V)  # Estado Gaussiano Multimodo

state_1 = qgt.coherent(alpha)

state_2 = qgt.tensor_product([state_1, state_1])
state_1.tensor_product([state_1])

F = qgt.fidelity(state_0, state_1)
