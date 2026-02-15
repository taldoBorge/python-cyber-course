O pip é um gerenciador de pacotes, o gerenciador oficial do python. Ele serve para instalar bibliotecas feitas por outros programadores e desenvolvedores para poder reutilizar código e não precisar reinventar a roda toda vez que for fazer um projeto.

**pip install requests** -> Para instalar a biblioteca externa requests , para fazer requisições http
**pip install requests** -> Para desinstalar uma biblioteca, no caso a requests
**pip --version** -> parecida com a verificação de versão do próprio python, serve pra ver a versão do pip instalado
**pip list** -> lista todos os pacotes e dependências, basicamente tudo que foi instalado no seu ambiente virtual
**pip install requests== 2.25.1**  ->Instala a versão especifica da biblioteca escolhida, no caso a requests 
###  pip list vs. pip freeze
- **`pip list`**: Uso visual. Bom para conferir rápido o que tem no ambiente. 
  *(Não deve ser usado para gerar o requirements.txt)*.
- **`pip freeze`**: Uso técnico. Gera a lista no formato exato que o Python entende para reinstalar dependências.
### Operadores de Terminal usados:
- `>` : Redireciona a saída para um arquivo (sobrescrevendo o que já existe).
- `&&` : Executa o segundo comando apenas se o primeiro terminar sem erros.