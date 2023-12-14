import numpy as np
import quantum_gaussian_toolbox as qgt
import matplotlib.pyplot as plt

# Parâmetros para a dinâmica
omega = 2 * np.pi  # Frequência natural [Hz]
t = np.linspace(0, 2, int(200))  # Variável para acompanhar a evolução de um sistema ou processo ao longo do tempo.

# Matriz de derivação
A = np.array([[0, -omega],
              [omega, 0]])

if A[0, 0] >= 0 and A[1, 1] <= 0:
    print("Os valores de A são válidos.")
else:
    print("Os valores de A são inválidos.")

D = np.diag([0, 0])  # Matriz de difusão
N = np.zeros((2, 1))  # Vetor de condução

# Simulando estado coerente, tempo e evolução
initial_0 = qgt.coherent(alpha=2)
simulation_0 = qgt.gaussian_dynamics(A, D, N, initial_0)
states_0 = simulation_0.unconditional_dynamics(t)

# Simulando a evolução temporal do estado comprimido coerente
initial_1 = initial_0.copy()
initial_1.squeeze(1.2)

simulation_1 = qgt.gaussian_dynamics(A, D, N, initial_1)
states_1 = simulation_1.unconditional_dynamics(t)

# Armazenar as informações da evolução do tempo para Squeezed:
mean_x_1 = np.zeros(len(t))
var_x_1 = np.zeros(len(t))
mean_x_0 = np.zeros(len(t))
var_x_0 = np.zeros(len(t))

# Loop através de estados evoluídos no tempo
for i in range(len(t)):
    mean_x_0[i] = states_0[i].R[0]
    var_x_0[i] = states_0[i].V[0, 0]
    mean_x_1[i] = states_1[i].R[0]
    var_x_1[i] = states_1[i].V[0, 0]

print("Mean Coherent:", mean_x_0)
print("Var Coherent:", var_x_0)
print("Mean Squeezed:", mean_x_1)
print("Var Squeezed:", var_x_1)

# PLOTAR GRÁFICO:
plt.figure(figsize=(6, 8))

plt.subplot(2, 1, 1)
plt.plot(t, mean_x_0, label='Coherent')  # Plot da função
plt.fill_between(t, mean_x_0 - np.sqrt(var_x_0), mean_x_0 + np.sqrt(var_x_0), color='orange', alpha=0.1,
                 label='Variância')
plt.xlabel('$\omega$ t')  # Rótulo do eixo x
plt.ylabel('$\langle x \u27E9$')  # Rótulo do eixo y
plt.title('$\langle x \u27E9 ~~~ versus ~~~ \omega$ t')
plt.legend()
plt.xlim(0, 2)  # Define o limite do eixo x de -1 a 5
plt.ylim(-5, 5)  # Define o limite do eixo y de -3 a 25
plt.grid(True, color='0.7')

plt.subplot(2, 1, 2)
plt.plot(t, mean_x_1, label='Squeezed')  # Plot da função
plt.fill_between(t, (mean_x_1 - np.sqrt(var_x_1)), (mean_x_1 + np.sqrt(var_x_1)), color='orange', alpha=0.1,
                 label='Variância')
plt.xlabel('$\omega$ t')  # Rótulo do eixo x
plt.ylabel('$\langle x \u27E9$')  # Rótulo do eixo y
plt.title('$\langle x \u27E9 ~~~ versus ~~~ \omega$ t')
plt.legend()
plt.xlim(0, 2)  # Define o limite do eixo x de -1 a 5
plt.ylim(-5, 5)  # Define o limite do eixo y de -3 a 25
plt.grid(True, color='0.8')

plt.tight_layout()
plt.show()
