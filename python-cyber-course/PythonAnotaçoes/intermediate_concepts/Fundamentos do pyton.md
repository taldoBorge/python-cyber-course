Variáveis são espaços na memória onde guardamos informações. No Python, a tipagem é **dinâmica** e **forte**.
##  Tipos Básicos
| Tipo  | Nome     | Exemplo              |
| :---- | :------- | :------------------- |
| str   | String   | `ip = "192.168.0.1"` |
| int   | Inteiro  | `tentativas = 3`     |
| float | Decimal  | `latencia = 0.05`    |
| bool  | Booleano | `is_admin = True`    |
##  Comandos de Inspeção
- `type(variavel)` : Retorna qual é o tipo daquele dado.
- `input("Texto")` : Recebe um dado digitado pelo usuário (sempre retorna como **String**!).
## Pulo do Gato (Segurança)
Ao usar o `input()` para receber uma porta de rede, é necessário converter para inteiro, senão o Python não consegue fazer cálculos:
`porta = int(input("Digite a porta: "))`
# Manipulação de Arquivos (I/O)

## Modos de Abertura
- `'w'` (Write): Escreve/Sobrescreve. Se o arquivo existe, ele limpa o conteúdo.
- `'r'` (Read): Apenas leitura.
- `'a'` (Append): Adiciona conteúdo ao final do arquivo sem apagar o que já existe.
## Conversão de Tipos (Casting)
Essencial para converter a entrada do `input()` ou a leitura de arquivos (`str`) em dados processáveis.

- `int("80")` -> Transforma o texto "80" no número 80.
- `str(192)`  -> Transforma o número 192 no texto "192".
- `float("0.5")` -> Transforma o texto em decimal.

> [!CAUTION]
> Se você tentar converter uma string que contém letras (ex: `int("admin")`), o Python retornará um `ValueError`. Em scripts reais, tratamos isso para o programa não "morrer".
---

#  Módulos e Bibliotecas (A "Mochila" do Hacker)

Módulos são arquivos `.py` reutilizáveis. Bibliotecas são conjuntos desses módulos.
## Formas de Importação

1. **Importação Total:**
   `import math` -> Usa-se: `math.sqrt(25)`
2. **Importação Específica:** (Economiza memória e digitação)
   `from math import sqrt, pi` -> Usa-se direto: `sqrt(25)`
3. **Uso de Alias (Apelidos):**
   `import random as rd` -> Usa-se: `rd.randint(1, 10)`
## Bibliotecas Nativas para Segurança
- `hashlib` : Para criar e verificar Hashes (MD5, SHA256) de arquivos.
- `socket` : Para conexões de rede de baixo nível.
- `re` : (Regular Expressions) Para buscar padrões em textos (ex: achar CPFs ou IPs dentro de um log).
- `json` : Para ler configurações de ferramentas.

##  Exemplo Prático: Gerador de ID de Incidente
```python
import random
import datetime

id_caso = random.randint(1000, 9999)
data = datetime.date.today()
print(f"INCIDENTE #{id_caso} registrado em: {data}")

## Processamento de Linhas
O método mais eficiente para ler arquivos grandes no Python:
```python
with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip()) # Remove \n e espaços 
extras



## 📝 Exemplo Prático de Log de Segurança
```python
with open("acessos.log", "a") as log:
    log.write("Tentativa de login detectada - IP: 192.168.1.50\n")
         