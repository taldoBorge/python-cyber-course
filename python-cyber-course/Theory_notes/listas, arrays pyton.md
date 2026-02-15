Listas são coleções ordenadas de itens. Elas são mutáveis, o que significa que podemos alterar seus valores após a criação.
## Fatiamento (Slicing)
A sintaxe é `lista[início : fim]`.
- **Início:** Inclusivo (começa exatamente aqui).
- **Fim:** Exclusivo (para um antes desse índice).
Exemplo : `frutas[1:4]` -> Pega os índices 1, 2 e 3.
## Métodos Úteis (Para adicionar ao seu script)
- `frutas.append("manga")`: Adiciona um item ao final.
- `len(frutas)`: Retorna o tamanho da lista (quantos itens tem).
- `frutas.sort()`: Organiza a lista em ordem alfabética.
##  Aplicação em Segurança
Usamos listas para armazenar:
1. **White Lists / Black Lists:** IPs permitidos ou bloqueados.
2. **Payloads:** Diferentes tipos de ataques para testar um campo de formulário.
3. **Dicionários:** Listas de palavras para ataques de força bruta.