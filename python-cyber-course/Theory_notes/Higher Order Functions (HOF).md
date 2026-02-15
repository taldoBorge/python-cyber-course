Uma **Higher Order Function** (Função de Ordem Superior) é uma função que cumpre pelo menos um dos dois requisitos:
1. Recebe uma ou mais funções como argumento.
2. Retorna uma função como resultado.
Este conceito é a base do paradigma de **Programação Funcional** no Python.
## 1. Funções como Argumentos
Em Python, funções são "objetos de primeira classe", o que significa que podem ser passadas para variáveis como qualquer outro dado.

```python
def aplicar_operacao(func, valor):
    return func(valor)

def dobro(x): return x * 2

# Passando a função 'dobro' como argumento
print(aplicar_operacao(dobro, 5)) # Output: 10
````

## 2. O Trio de Ferro: Map, Filter e Reduce

### Map (Transformação)

Aplica uma função a cada item de um iterável (como uma lista) e retorna um novo objeto mapeado.

- **Sintaxe:** `map(função, lista)`    
- **Uso:** Transformar dados em lote (ex: converter todas as strings de uma lista para int).  
### Filter (Seleção)

Filtra os elementos de uma lista baseado em uma função que retorna `True` ou `False`.

- **Sintaxe:** `filter(função_booleana, lista)`    
- **Uso:** Limpar logs, filtrar portas abertas ou usuários ativos.    
### Reduce (Agregação)

Reduz uma lista a um único valor, aplicando uma função cumulativa.

- **Importação:** `from functools import reduce`    
- **Uso:** Somatórios complexos ou encontrar o maior valor em uma sequência.   
## 3. Funções Lambda (Anônimas)

São funções de uma única linha, sem nome, definidas com a palavra-chave `lambda`. Muito úteis dentro de HOFs para evitar a criação de funções simples com `def`.

**Exemplo com Filter:**

Python

```
portas = [21, 22, 80, 443, 8080]
# Filtrar apenas portas acima de 100
altas = list(filter(lambda p: p > 100, portas))
```

## 4. Closures (Funções Fábrica)

Ocorre quando uma função interna "lembra" do ambiente em que foi criada, mesmo após a função externa ter terminado a execução.

Python

```
def multiplicador(fator):
    def operacao(n):
        return n * fator
    return operacao

dobrar = multiplicador(2) # O '2' fica guardado no "escopo" da função
print(dobrar(10)) # Output: 20
```

## Aplicação em Cibersegurança

- **Processamento de Logs:** Usar `filter` para extrair apenas linhas de erro de um arquivo de log gigante.    
- **Análise de Redes:** Usar `map` para normalizar endereços IP ou formatar saídas de scanners.    
- **Scripts de Automação:** Criar Closures que geram "configuradores de carga" específicos para diferentes tipos de alvos.   
## Performance

- `map` e `filter` em Python são "lazy" (preguiçosos). Eles retornam iteradores. Use `list()` para ver o resultado final se necessário.    
- Lambdas são ótimas para legibilidade em funções curtas, mas para lógicas complexas, prefira o `def` tradicional.   