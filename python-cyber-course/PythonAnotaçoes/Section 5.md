# Section 5: Redes com Python & Sockets

Esta seção marca a transição de scripts de automação local para a comunicação entre dispositivos, explorando como os dados viajam e como o Python pode interceptar e testar esses caminhos.
##  1. Arquitetura e Modelos de Camadas

Para a rede funcionar, a comunicação é dividida em blocos organizados.

- **Modelo OSI (7 camadas)**: Focado em teoria e estudo de protocolos.    
- **Modelo TCP/IP (4 camadas)**: O padrão real da Internet.
### Camadas Principais:

1. **Enlace**: Trabalha com o endereço **MAC** (identidade física da placa).    
2. **Rede**: Onde vive o endereço **IP** (endereço lógico) e o protocolo **ICMP** (Ping).    
3. **Transporte**: Define a confiabilidade da entrega.    
    - **TCP**: Confiável, garante a ordem dos dados (usado em HTTP, SSH).               
    - **UDP**: Rápido, mas sem garantia de entrega (usado em DNS e Vídeo).        
4. **Aplicação**: Protocolos de alto nível que usamos no navegador (**HTTP**, **HTTPS**, **DNS**, **FTP**).
## 2. Endereçamento: IP e Portas

- **IP (Internet Protocol)**: Identifica o dispositivo na rede.   
- **Portas**: Identificam o serviço específico rodando naquele IP9. Existem 65.535 portas disponíveis.    

### Portas Essenciais para Cibersegurança:

- **22 (SSH)**: Acesso remoto seguro.    
- **53 (DNS)**: Tradução de nomes para IPs.    
- **80 / 443**: Tráfego Web (HTTP / HTTPS).    
- **3306**: Banco de dados MySQL.   
## 3. Programação de Sockets (O Coração da Rede)

A biblioteca `socket` é a ponte que o Python usa para "discar" para outros computadores.
### Criando um Conexão Manual:

```Python
import socket

# AF_INET = IPv4 | SOCK_STREAM = TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Conectando ao alvo
client.connect(("google.com", 80)) 

# Enviando requisição HTTP bruta (em bytes)
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") 

# Recebendo a resposta do servidor
resposta = client.recv(4096)
print(resposta.decode()) 
```
## 4. Verbos HTTP e Comunicação Web

Toda requisição para um servidor web usa um "verbo" para dizer o que quer:

- **GET**: Busca dados (não altera nada no servidor).    
- **POST**: Envia dados (usado em logins e formulários).    
- **PUT/PATCH**: Atualiza dados existentes.    
- **DELETE**: Remove um recurso.
## 5. Ferramentas Criadas: Port Scanner & Validator

- **Port Scanner**: Varre uma lista de portas para verificar quais estão `open` (abertas) ou `closed` (fechadas)        
- **Service Validator**: Função que tenta conectar a um IP/Porta e retorna se o serviço está "Reachable" (alcançável) ou não.      