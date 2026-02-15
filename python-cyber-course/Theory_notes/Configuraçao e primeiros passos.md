### Comandos linux essenciais:
 - **sudo dpkg --configure -a** -> Esse comando de emergência é usado para destravar o instalador do Debian quando um processo é interrompido como apertar CNTRL + Z
 - **apt update** -> Atualiza a lista de repositórios do sistema 
 -  **apt install python3** -> realiza a instalação do interpretador Python
 - **ls -l** -> Lista os arquivos do diretório atual com detalhes (permissões, dono, tamanho)
 - **mkdir -p Caminho/da/pasta** -> Cria pastas e subpastas de uma unica vez (-p é de parent)
 - **mv AntigoNome NovoNome** -> renomeia pastas ou move arquivos 
 - **touch arquivo.xx** -> esse comando cria um novo arquivo vazio
 - **code .**  -> abre o vscode na pasta onde voce rodou o comando

---
###  Explicação dos Comandos Python

1. **`sys.version`**: Retorna a versão exata do interpretador. Importante para scripts que usam bibliotecas modernas (como o Python 3.13).    
2. **`os.getlogin()`**: Retorna o nome do usuário logado. Em scripts de automação, ajuda a validar se o script tem permissões de administrador.    
3. **`os.getcwd()`**: (_Get Current Working Directory_) Mostra o caminho absoluto de onde o script está rodando. 

##  Lições Aprendidas (Troubleshooting)

- **Case Sensitivity:** O Linux diferencia `Segurança` de `segurança`. Sempre respeite as maiúsculas.    
- **Python Syntax:** O comando `printf` (comum em C/C++) não existe no Python básico; o correto é `print`.    
- **Gerenciamento de Processos:** - `Ctrl + C`: Interrompe e encerra o processo (Kill).    
    - `Ctrl + Z`: Apenas pausa o processo (Suspend), mantendo arquivos e travas de sistema bloqueados.
## 2. Primeiro Script: 

Este script realiza uma **Enumeração Local**, técnica básica de reconhecimento em cibersegurança para entender sob quais condições um código está sendo executado.

```python

# Importação de bibliotecas (caixas de ferramentas extras)

import sys  # Interage com o interpretador (ex: versão do Python)
import os   # Interage com o Sistema Operacional (ex: pastas, usuário, arquivos)

print("--- Ambiente de Cibersegurança Pronto ---")

# Uso de f-strings (f"") para inserir variáveis dentro de textos
print(f"Versão do Python: {sys.version}")
print(f"Usuário atual: {os.getlogin()}")
print(f"Pasta atual: {os.getcwd()}")

print("-----------------------------------------")

```python    