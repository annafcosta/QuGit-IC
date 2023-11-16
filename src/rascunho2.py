import numpy as np
import matplotlib.pyplot as plt

import quantum_gaussian_toolbox as gauss

omega = 2 * np.pi  # omega = 2 pi em Hz
t = np.linspace(0, 2, int(200))  # intervalo de tempo

A = np.array([[0, +omega],
              [-omega, 0]])  # matriz drift

D = np.diag([0, 0])  # matriz de difusão

N = np.zeros((2, 1))  # vetor direção

initial_0 = gauss.coherent(2)

simulation_0 = gauss.gaussian_dynamics(A, D, N, initial_0)

states_0 = simulation_0.unconditional_dynamics(t)

initial_1 = initial_0.copy()

initial_1.squeeze(1.2)

simulation_1 = gauss.gaussian_dynamics(A, D, N, initial_1)

states_1 = simulation_1.unconditional_dynamics(t)

mean_x_1 = np.zeros(len(t))
var_x_1 = np.zeros(len(t))
mean_p_1 = np.zeros(len(t))
var_p_1 = np.zeros(len(t))

mean_x_0 = np.zeros(len(t))
var_x_0 = np.zeros(len(t))
mean_p_0 = np.zeros(len(t))
var_p_0 = np.zeros(len(t))

for i in range(len(t)):
    mean_x_0[i] = states_0[i].R[0]
    var_x_0[i] = states_0[i].V[0, 0]
    mean_p_0[i] = states_0[i].R[1]
    var_p_0[i] = states_0[i].V[1, 1]

    mean_x_1[i] = states_1[i].R[0]
    var_x_1[i] = states_1[i].V[0, 0]
    mean_p_1[i] = states_1[i].R[1]
    var_p_1[i] = states_1[i].V[1, 1]
# # Cria um estado quântico gaussiano
#
# R_initial=np.array([[0],[0]])
# estado_teste=gauss.gaussian_state("squeezed",1.5)
# V_initial=estado_teste.V
# initial_state = gauss.gaussian_state(R_initial, V_initial)
#
#
# # Realiza um deslocamento
# alpha = complex(1, 1)
# displaced_state = gauss.displace(initial_state,alpha,0)
# print(displaced_state)
# # Calcula a pureza do estado deslocado
# purity = displaced_state.purity()
#
# # Aplica uma matriz unitária e deslocamento
# S = np.array([[1, 0], [0, 1]])
# d = np.array([0.1, 0.2])
# transformed_state = initial_state.apply_unitary(S, d)
#
# # Plota as médias quadráticas do estado transformado
# transformed_state.plot()

plt.figure(figsize=(6, 8))

plt.subplot(2, 1, 1)
plt.plot(t, mean_x_0, label='Coherent')  # Plot da função
plt.fill_between(t, mean_x_0 - np.sqrt(var_x_0), mean_x_0 + np.sqrt(var_x_0), color='blue', alpha=0.1,
                 label='Variância')
plt.xlabel('$\omega$ t')  # Rótulo do eixo x
plt.ylabel('$\langle x \u27E9$')  # Rótulo do eixo y
plt.title('$\langle x \u27E9 ~~~ versus ~~~ \omega$ t')  # Título do gráfico
plt.legend()  # Mostra a legenda
plt.xlim(0, 2)  # Define o limite do eixo x de -1 a 5
plt.ylim(-5, 5)  # Define o limite do eixo y de -3 a 25
plt.grid(True, color='0.7')  # Mostra as grades
# plt.show()

plt.subplot(2, 1, 2)
plt.plot(t, mean_x_1, label='Squeezed')  # Plot da função
plt.fill_between(t, (mean_x_1 - np.sqrt(var_x_1)), (mean_x_1 + np.sqrt(var_x_1)), color='blue', alpha=0.1,
                 label='Variância')
plt.xlabel('$\omega$ t')  # Rótulo do eixo x
plt.ylabel('$\langle x \u27E9$')  # Rótulo do eixo y
plt.title('$\langle x \u27E9 ~~~ versus ~~~ \omega$ t')  # Título do gráfico
plt.legend()  # Mostra a legenda
plt.xlim(0, 2)  # Define o limite do eixo x de -1 a 5
plt.ylim(-5, 5)  # Define o limite do eixo y de -3 a 25
plt.grid(True, color='0.7')  # Mostra as grades
# plt.show()

plt.tight_layout()

plt.show()

plt.figure(figsize=(6, 8))

plt.subplot(2, 1, 1)
plt.plot(t, mean_p_0, label='Coherent')  # Plot da função
plt.fill_between(t, mean_p_0 - np.sqrt(var_p_0), mean_p_0 + np.sqrt(var_p_0), color='red', alpha=0.1, label='Variância')
plt.xlabel('$\omega$ t')  # Rótulo do eixo x
plt.ylabel('$\langle p \u27E9$')  # Rótulo do eixo y
plt.title('$\langle p \u27E9 ~~~ versus ~~~ \omega$ t')  # Título do gráfico
plt.legend()  # Mostra a legenda
plt.xlim(0, 2)  # Define o limite do eixo x de -1 a 5
plt.ylim(-5, 5)  # Define o limite do eixo y de -3 a 25
plt.grid(True, color='0.7')  # Mostra as grades
# plt.show()

plt.subplot(2, 1, 2)
plt.plot(t, mean_p_1, label='Squeezed')  # Plot da função
plt.fill_between(t, (mean_p_1 - np.sqrt(var_p_1)), (mean_p_1 + np.sqrt(var_p_1)), color='red', alpha=0.1,
                 label='Variância')
plt.xlabel('$\omega$ t')  # Rótulo do eixo x
plt.ylabel('$\langle p \u27E9$')  # Rótulo do eixo y
plt.title('$\langle p \u27E9 ~~~ versus ~~~ \omega$ t')  # Título do gráfico
plt.legend()  # Mostra a legenda
plt.xlim(0, 2)  # Define o limite do eixo x de -1 a 5
plt.ylim(-5, 5)  # Define o limite do eixo y de -3 a 25
plt.grid(True, color='0.7')  # Mostra as grades
# plt.show()

plt.tight_layout()

plt.show()

