As listas em Python são objetos que possuem métodos próprios para manipulação de dados.
##  Métodos Principais:
- `.append(valor)`: Adiciona ao final da lista (útil para logs de eventos).
- `.pop()`: Remove e retorna o último elemento (sistema LIFO - Last In, First Out).
- `del lista[indice]`: Remove permanentemente um item por sua posição.
## Iteração Automática
O comando `for x in lista:` é a forma mais eficiente de percorrer dados. 
O Python gerencia o índice automaticamente, evitando erros de "Index Out of Range".
#  Manipulação de Strings e Listas

##  .split(separador, maxsplit)
Transforma uma **String** em uma **Lista**.
- Se não passar nada, ele corta nos espaços em branco.
- O `maxsplit` limita quantos cortes serão feitos.
- **Uso:** Extrair informações de arquivos CSV ou Logs.
## .join(iterável)
Transforma uma **Lista** em uma **String**.
- A sintaxe é: `"separador".join(lista)`.
- **Uso:** Gerar arquivos formatados ou mensagens legíveis.
##  Exemplo Prático de Segurança:
`log = "192.168.1.1:8080"`
`ip, porta = log.split(":")`
`print(f"Alvo: {ip} na porta {porta}")`