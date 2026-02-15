# Python no Terminal e Sistemas

Esta seção foca na interação do Python diretamente com o Sistema Operacional, permitindo a automação de tarefas administrativas, auditoria de arquivos e execução de comandos externos para diagnósticos de rede. 
##  Bibliotecas Principais

- **`os`**: Utilizada para integração direta com o sistema operacional, como capturar o diretório atual (`os.getcwd()`) ou listar arquivos (`os.listdir()`).     
- **`subprocess`**: Biblioteca moderna e segura para executar comandos externos do sistema. Substitui o antigo `os.system` com maior controle sobre saídas e erros.  
- **`pathlib`**: Facilita o gerenciamento de diretórios e arquivos de forma organizada e multiplataforma.        
- **`datetime`**: Essencial para gerar _timestamps_ únicos, evitando que relatórios novos sobrescrevam execuções anteriores.
---
##  Automação de Comandos do Sistema

O uso de `subprocess.run` permite capturar a execução de ferramentas essenciais: 
### Comandos de Diagnóstico Comuns:

- **`whoami`**: Identifica o usuário logado no sistema. 
- **`ipconfig` / `ip addr`**: Exibe configurações de interfaces de rede.        
- **`tracert` / `traceroute`**: Mapeia o caminho dos pacotes até um destino (ex: 8.8.8.8).     
- **`netstat -an`**: Lista conexões de rede ativas e portas em escuta.    
### Parâmetros Críticos do `subprocess.run`:

- **`capture_output=True`**: Captura tanto o sucesso (`stdout`) quanto mensagens de erro (`stderr`).    
- **`text=True`**: Garante que o resultado retorne como texto (string) legível, em vez de bytes brutos. 
- **`shell=True`**: Necessário em ambientes Windows para interpretar comandos específicos do terminal.    
---
##  Manipulação de Logs e Auditoria

A automação permite monitorar a integridade do sistema através da verificação de arquivos e geração de relatórios. 
### Auditoria de Arquivos Modificados:

Um script pode percorrer diretórios e identificar arquivos alterados na data atual: 

1. Captura a data de hoje via `time.strftime`.     
2. Itera pelos arquivos com extensões específicas (ex: `.py`).     
3. Compara o tempo de modificação (`os.path.getmtime`) com a data atual.     
4. Registra as ocorrências em um arquivo `log.txt`.    

### Fluxo de Salvamento Seguro de Relatórios:

Python

``` bash
# Exemplo de lógica para salvar saídas com timestamp 
BASE_DIR = Path("relatorios")
BASE_DIR.mkdir(exist_ok=True) # [cite: 11, 36]
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # [cite: 12, 37]
caminho = BASE_DIR / f"{nome_arquivo}_{timestamp}.txt" # [cite: 21, 41]
```
---
## Boas Práticas e Segurança

- **Preferência pelo `subprocess`**: Mais seguro para evitar vulnerabilidades de injeção de comandos.     
- **Tratamento de Erros**: Utilizar blocos `try/except` para capturar falhas na execução de comandos externos sem interromper o script. 
- **Auditoria de Rede**: Automatizar o escaneamento de rede e salvar resultados em formatos estruturados (como JSON) para detectar dispositivos desconhecidos.    