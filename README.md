# QuGit-Scientific-Initiation

The project in question emerged as an initiative to explore the intersection between computing and quantum mechanics, under the coordination of Professor Leonardo Antônio Mendes de Souza. Studies in this domain aim at developing algorithms primarily for the simulation of a special class of continuous-variable Gaussian quantum states. To achieve this goal, we are utilizing the **Quantum Gaussian Information Toolbox**, or QuGIT, a Python numerical toolkit dedicated to Gaussian quantum information applications.
___

**TASKS IN PROGRESS**

🔵 [Quantum fidelity](#Objetivos-1)

<div id="Objetivos-1">
<!-- Seu conteúdo para a Objetivos -->
</div>

⚪ [Unitary Field Quadrature Dynamics](#autores-4) 

<div id="autores-4">
<!-- Seu conteúdo para Autores -->
</div>

🔵 [Citations](#autores-3)

<div id="autores-3">
<!-- Seu conteúdo para Autores -->
</div>

⚪ [Collaborators](#colab-4)

<div id="colab-4">
<!-- Seu conteúdo para Autores -->
</div>

🔵 [Author](#autor-5)

<div id="autor-5">
<!-- Seu conteúdo para Autores -->
</div>

___

### 🔵 Quantum Fidelity

___


Quantum fidelity is a fundamental concept in quantum mechanics, employed to assess the similarity between quantum states. Simply put, it quantifies the probability of the two states being the same. Taking these factors into consideration, the *initial code* aims to calculate the quantum fidelity between a pair of Gaussian states of two modes. To do so, it is necessary to create the commented Gaussian state, which can be described by a mean vector of quadratures and a covariance matrix. Given this information, the algorithm is structured as follows::

* *Creation of an arbitrary two-mode Gaussian states*: This is achieved by initializing a covariance matrix using arrays from the numpy library;
 
 * *Verification of the resulting matrix*: It is necessary to check if the generated matrix is non-negative definite, respecting the limitation given by the expression $σ + iΩ ≥ 0$.

```python
 def check_condition(matrix):
    matrix_real = matrix.real
    eigenvalues = np.linalg.eigvals(matrix_real)
    return all(eig >= 0 for eig in eigenvalues)

    sigma = np.random.rand(4, 4) # Matriz de covariancia
    sigma_cov = 10 * sigma 
```

* *Initializing a Gaussian state*: Through an integrated function and the parameter associated with the state, it is possible to initialize a Gaussian state. To do so, a complex number $(\alpha)$ is defined along with the coherent state, which is initialized with a corresponding complex amplitude defined by qgt.coherent(alpha) from the QuGit library.

```python
 alpha = 1 - 2.0j  # Representacao de um numero complexo.

    # Definição dos estados:
    estado_0 = qgt.gaussian_state(R, sigma_cov)  # Estado Gaussiano Multimodo
    estado_1 = qgt.coherent(alpha)
```

* *Tensor product*: Finally, the tensor product of the initialized coherent state is calculated using the **qgt.tensor** product function from the QuGIT library.

___

### ⚪ Unitary Field Quadrature Dynamics
___

#### 🔵 Citations

This work utilizes the QuGIT toolbox. [[QuGIT Toolbox]](https://arxiv.org/abs/2201.06368).

#### ⚪ Collaborators

Leonardo Antônio Mendes de Souza - Supervisor. [[Perfil-Lattes]](http://lattes.cnpq.br/9817332779478274).

#### 🔵 Author


Anna Luísa Ferreira. [[annafcosta]](https://github.com/annafcosta).


