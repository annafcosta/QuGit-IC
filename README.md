# QuGit-Iniciação-Científica

O projeto em questão surgiu como uma iniciativa para explorar a interseção entre a computação e a mecânica quântica, sob a coordenação do professor Leonardo Antônio Mendes de Souza. Os estudos nesse domínio visam o desenvolvimento de algoritmos voltados principalmente para a simulação de uma classe especial de *estados quânticos gaussianos de variáveis contínuas*. Para alcançar esse objetivo, estamos utilizando a biblioteca **Quantum Gaussian Information Toolbox**, ou QuGIT, uma caixa de ferramentas numérica em Python dedicada a aplicações de informação quântica gaussiana.
___

**TAREFAS EM DESENVOLVIMENTO**

🔵 [Fidelidade Quântica](#Objetivos-1)

<div id="Objetivos-1">
<!-- Seu conteúdo para a Objetivos -->
</div>

⚪ [Citações](#autores-3)

<div id="autores-3">
<!-- Seu conteúdo para Autores -->
</div>

🔵 [Colabaradores](#colab-4)

<div id="colab-4">
<!-- Seu conteúdo para Autores -->
</div>

⚪ [Autor](#autor-5)

<div id="autor-5">
<!-- Seu conteúdo para Autores -->
</div>

___

### 🔵 Fidelidade Quântica
___

A fidelidade quântica, é um conceito fundamental na mecânica quântica, empregada para avaliar a similaridade entre estados quânticos. Em termos simples, ela quantifica a probabilidade dos dois estados analisados serem os mesmos. Levando em consideração esses fatores, o *código inicial* tem como objetivo calcular a fidelidade quântica entre um par de estados gaussianos de dois modos. Para tal, é necessário criar um estado gaussiano de dois modos, o qual pode ser descrito por um vetor médio de quadratura e uma matriz de covariância. Dada essas informações, o algortimo foi estruturado da seguinte maneira:

* *Criação de um estado gaussiano de dois modos arbitrários*: É obtida por meio da inicialização de uma matriz de covariância, utilizando os arrays da bibilioteca numpy;
 
 * *Verificação da matriz resultante*: É necessário verificar se a matriz gerada é não negativa definida, respeitando a limitação dada pela expressão $σ + iΩ ≥ 0$.

```python
 def check_condition(matrix):
    matrix_real = matrix.real
    eigenvalues = np.linalg.eigvals(matrix_real)
    return all(eig >= 0 for eig in eigenvalues)

    sigma = np.random.rand(4, 4) # Matriz de covariancia
    sigma_cov = 10 * sigma 
```

* *Inicializar um estado gaussiano*: Por meio de uma função integrada e o parâmetro associado ao estado, é possível inicializar um estado gaussiano. Para tal, define-se um número complexo $(alpha)$ e o estado coerente, o qual é inicializado com uma amplitudente complexa correspondente, definida por **qgt.coherent(alpha)** da biblioteca QuGit.

```python
 alpha = 1 - 2.0j  # Representacao de um numero complexo.

    # Definição dos estados:
    estado_0 = qgt.gaussian_state(R, sigma_cov)  # Estado Gaussiano Multimodo
    estado_1 = qgt.coherent(alpha)
```

* *Produto tensorial*: Por fim, calcula-se o produto tensorial do estado coerente iniciado, utilizando a função **qgt.tensor** product da biblioteca QuGIT.

#### ⚪ Citações

Este trabalho faz uso de QuGIT toolbox. [[QuGIT Toolbox]](https://arxiv.org/abs/2201.06368).

#### 🔵 Colabaradores 

Leonardo Antônio Mendes de Souza - Orientador. [[Perfil-Lattes]](http://lattes.cnpq.br/9817332779478274).

#### ⚪ Autor


Anna Luísa Ferreira. [[annafcosta]](https://github.com/annafcosta).


