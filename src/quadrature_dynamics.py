import numpy as np
import quantum_gaussian_toolbox as qgt
import matplotlib.pyplot as plt

# Parâmetros para a dinâmica
omega = 2 * np.pi  # Frequência natural [Hz]
t = np.linspace(0, 2 / omega,
                int(200))  # Variavel para acompanhar a evolução de um sistema ou processo ao longo do tempo.

# Matriz de derivação
A = np.array([[0, -omega],
              [omega, 0]])

D = np.diag([0, 0])  # Matriz de difusão
N = np.zeros((2, 1))  # Vetor de conducao
