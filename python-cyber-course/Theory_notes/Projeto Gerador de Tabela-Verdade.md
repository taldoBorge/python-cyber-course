# Gerador Universal de Tabela-Verdade

Este projeto consiste em um script Python que lê uma expressão lógica do usuário, identifica as variáveis dinamicamente e gera todas as combinações possíveis para determinar o resultado lógico de cada cenário.
## Explicação das Funções e Ferramentas

| Ferramenta / Função | O que faz neste projeto?                                                                                           |
| :------------------ | :----------------------------------------------------------------------------------------------------------------- |
| `itertools.product` | Gera o "Produto Cartesiano". Aqui, cria todas as combinações de `True/False` baseadas no número de variáveis.      |
| `filter()`          | Filtra a string da expressão para extrair apenas o que é letra, ajudando a isolar as variáveis.                    |
| `set()`             | Remove duplicatas. Se a variável 'A' aparece 3 vezes, o `set` garante que ela seja contada apenas uma vez.         |
| `sorted()`          | Organiza as variáveis em ordem alfabética (A, B, C...) para uma tabela organizada.                                 |
| `dict(zip(...))`    | Une os nomes das variáveis com os valores (T/F) gerados pelo `product`, criando um "mapa" para o Python consultar. |
| `eval()`            | A "alma" do script. Ela pega a string da expressão e a executa como código real, calculando o resultado booleano.  |

---

## Análise Linha por Linha

```python
import itertools  # Importa a biblioteca de ferramentas de iteração eficiente.

# 1. Entrada do Usuário
expression = input("Digite a expressão...") 

# 2. Identificação de Variáveis
# Criamos um conjunto de palavras que o Python usa como operadores para não confundir com variáveis.
operadores = {'and', 'or', 'not'}

# Transformamos tudo que não é letra em espaço, depois dividimos (split) em palavras.
palavras = "".join(c if c.isalpha() else " " for c in expression).split()

# Guardamos apenas o que é palavra E não está na lista de operadores.
variables = sorted(set(v for v in palavras if v.lower() not in operadores))

# 3. Cabeçalho da Tabela
# O join une os nomes das variáveis com uma barra " | ".
print(" | ".join(variables) + " | Resultado")
print("-" * (len(variables) * 4 + 12)) # Cria uma linha divisória proporcional ao tamanho da tabela.

# 4. O Coração do Script: Loop de Combinações
# O repeat=len(variables) diz: "Se tenho 3 variáveis, preciso de 3 colunas de T/F".
for values in itertools.product([False, True], repeat=len(variables)):
    
    # Associa cada letra ao seu valor atual (Ex: {'A': True, 'B': False})
    context = dict(zip(variables, values))
    
    # Calcula o resultado da string usando os valores do dicionário 'context'
    # O {"__builtins__": None} é uma trava de segurança para o eval não acessar funções do sistema.
    result = eval(expression, {"__builtins__": None}, context)
    
    # 5. Formatação da Saída
    # Para cada variável, exibe 'T' se for True e 'F' se for False.
    row = " | ".join(['T' if context[var] else 'F' for var in variables])
    row += " | " + ('T' if result else 'F')
    print(row)
````
## Raciocínio Lógico do Fluxo

1. **Captura:** O programa recebe uma string bruta (texto).    
2. **Sanitização:** O código precisa limpar a string para saber quem são os "atores" (variáveis) e quem são as "ações" (operadores).    
3. **Explosão Combinatória:** Através do `product`, o script testa todas as realidades possíveis ($2^n$).    
4. **Mapeamento:** O `zip` cria uma ponte entre o nome abstrato ('A') e o valor real (True).    
5. **Processamento:** O `eval` faz o papel do cérebro humano, resolvendo os parênteses e precedências lógicas.    
6. **Exibição:** O resultado é traduzido de booleano puro para 'T/F' para facilitar a leitura.
## Visão de Cibersegurança

Este script simula o funcionamento de um **Decision Engine** (Motor de Decisão). Em sistemas de firewall ou permissões de nuvem (AWS/Azure), a lógica é exatamente esta: avaliar múltiplas condições para chegar a um `True` (Allow) ou `False` (Deny).