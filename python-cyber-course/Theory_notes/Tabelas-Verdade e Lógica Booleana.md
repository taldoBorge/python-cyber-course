A lógica booleana é o que permite ao computador "tomar decisões". No Python, os operadores lógicos são escritos por extenso: `and`, `or`, e `not`.
## Operadores Básicos

### 1. AND (E) - "O Exigente"
Só retorna `True` se **todos** forem verdadeiros.
*Uso em Cyber:* `if usuario_valido and senha_correta and token_mfa:

| A | B | A and B |
| :--- | :--- | :--- |
| V | V | **V** |
| V | F | F |
| F | V | F |
| F | F | F |

### 2. OR (OU) - "O Flexível"
Retorna `True` se **pelo menos um** for verdadeiro.
*Uso em Cyber:* `if ip_bloqueado or pais_suspeito:`

| A | B | A or B |
| :--- | :--- | :--- |
| V | V | **V** |
| V | F | **V** |
| F | V | **V** |
| F | F | F |

### 3. NOT (NÃO) - "O Inversor"
Inverte o estado lógico.
*Uso em Cyber:* `if not is_admin:` (Se o usuário **não** for admin).

| A | NOT A |
| :--- | :--- |
| V | F |
| F | V |

## 🛠️ Exemplo de Expressão Complexa no Python

Para a expressão `(A or B) and not C`:

```python
A = True
B = False
C = True

# Passo 1: (True or False) -> True
# Passo 2: not True -> False
# Passo 3: True and False -> False
resultado = (A or B) and not C
print(f"O resultado da lógica é: {resultado}") 