Em Python, quando não sabemos quantos dados uma função receberá, utilizamos o empacotamento de argumentos. Isso permite criar scripts genéricos e ferramentas de automação robustas.
##  1. *args (Positional Arguments)
O `*args` captura argumentos extras passados por posição e os armazena em uma **Tupla**.

- **Sintaxe:** `def func(*args):`
- **Tipo de Dado:** `tuple` (imutável).
- **Uso Comum:** Listas de alvos, números para cálculos, nomes de arquivos.

### Exemplo Prático:
```python
def listar_alvos(*ips):
    for ip in ips:
        print(f"Alvo configurado: {ip}")

listar_alvos("192.168.1.1", "10.0.0.5", "172.16.0.2")
````

---

##  2. **kwargs (Keyword Arguments)

O `**kwargs` captura argumentos extras passados com nome (chave=valor) e os armazena em um **Dicionário**.

- **Sintaxe:** `def func(**kwargs):    
- **Tipo de Dado:** `dict` (mutável).    
- **Uso Comum:** Configurações de sistema, flags de segurança, parâmetros de conexão.   
### Exemplo Prático:

Python

```
def config_server(**opcoes):
    porta = opcoes.get("port", 80)
    print(f"Servidor rodando na porta: {porta}")

config_server(port=443, protocol="HTTPS", verbose=True)
```

##  3. A Ordem de Precedência (Regra de Ouro)

Para evitar erros de sintaxe, o Python exige uma ordem específica na definição da função:

1. **Parâmetros Fixos** (Obrigatórios)   
2. **`*args`** (Extras posicionais)    
3. **`**kwargs`** (Extras nomeados)    

##  Aplicação em Cibersegurança

### Automação de Scanner (Exemplo Real)

Imagine um script que precisa disparar um ataque ou scan contra múltiplos IPs, mas as configurações de timeout ou proxy podem variar:

Python

```
def pentest_tool(scan_type, *targets, **settings):
    print(f"Executando {scan_type}...")
    for target in targets:
        timeout = settings.get("timeout", 5)
        print(f" -> Escaneando {target} com timeout de {timeout}s")

pentest_tool("PortScan", "192.168.0.1", "192.168.0.10", timeout=2, verbose=True)
```

##  Dicas Rápidas

- `args` e `kwargs` são nomes convencionais. O que define a função é o `*` e o `**`.    
- Use `kwargs.get('chave', 'valor_padrao')` para evitar erros caso o usuário esqueça de passar uma configuração.    
- Use `type(args)` para debugar e ver a Tupla, ou `type(kwargs)` para ver o Dicionário.

