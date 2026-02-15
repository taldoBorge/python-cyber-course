### 1. Para que serve e o que ele faz?

Imagine que você está testando uma ferramenta de ataque que precisa da biblioteca `Requests` na versão 2.0, mas o seu sistema Debian usa a versão 3.0 para rodar scripts internos. Se você atualizar, o sistema quebra. Se você não atualizar, a ferramenta não funciona.

O **venv** cria uma **cópia isolada** do Python dentro da pasta do seu projeto.

- **Isolamento:** Tudo o que você instalar ali dentro (bibliotecas, ferramentas) fica preso naquela pasta.    
- **Segurança:** Você não corre o risco de corromper o Python do seu sistema operacional (Debian). No Linux, isso é vital, pois o Debian usa o Python para muitas funções do próprio sistema.    
- **Limpeza:** Quando você cansar do projeto, basta deletar a pasta e o sistema continua limpo.

### Por que usar em Cibersegurança? 
- **Sandboxing:** Se uma biblioteca de terceiros for maliciosa ou instável, ela está limitada ao diretório do ambiente virtual.
- **Reproduzibilidade:** Permite criar um arquivo `requirements.txt` com as versões exatas das ferramentas de exploit para que funcionem em qualquer máquina.

### Como usar?
 Para usar o venv, precisamos criar o ambiente, ativar, usar e desativar. Para isso vamos ao terminal do linux ou do próprio vs-code e usamos os seguintes comandos:
 - **python3 -m venv venv** -> Aqui criamos nosso ambiente, o primeiro venv é o comando e o segundo é o nome da pasta que ele vai criar
 - **source venv/bin/activate** -> Nesse comando nos ativamos o ambiente, se funcionar o terminal vai mudar, vai aparecer um (venv) antes do nome
 - agora qualquer coisa que voce rodar como **pip install**, fica so nesse projeto.
 - **deactive** -> Você sai do ambiente do venv e volta pro sistema normal

### Erro: ensurepip is not available
**Causa:** O Debian não instala o módulo `venv` por padrão para economizar espaço e manter o sistema estável.
**Solução:** 1. Instalar o pacote específico da versão: `sudo apt install python3.13-venv`.
2. Remover a pasta `venv` incompleta: `rm -rf venv`.
3. Criar o ambiente novamente sem usar SUDO. (nunca crie ambientes virtuais assim como superusuário) 
##  Congelando Dependências (requirements.txt)

Para que outras pessoas (ou servidores) consigam rodar meu script com as mesmas versões de bibliotecas, usamos o arquivo de requisitos.
### Comandos:
- `pip freeze` : Exibe todas as bibliotecas e versões exatas instaladas no ambiente atual.
- `pip freeze > requirements.txt` : Salva essa lista em um arquivo.
- `pip install -r requirements.txt` : Instala todas as bibliotecas listadas no arquivo de uma só vez (muito usado em servidores e pipelines de CI/CD).

###  Visão de Segurança:
Manter versões fixas (ex: `requests==2.32.5`) evita que uma atualização futura de uma biblioteca quebre seu script de automação ou introduza uma vulnerabilidade não testada.

