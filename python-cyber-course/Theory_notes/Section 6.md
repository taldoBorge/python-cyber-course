
Nesta seção, o foco foi a integração do Python com ferramentas consagradas da cibersegurança e o desenvolvimento de ferramentas customizadas para auditoria de redes e análise de eventos.

##  1. Automação com Nmap (`python-nmap`)

O uso da biblioteca `python-nmap` permitiu criar scripts que automatizam a varredura de múltiplos hosts e salvam relatórios estruturados

- **Funcionalidade**: O script utiliza a classe `PortScanner()` para mapear portas abertas e identificar o estado do host (UP/DOWN).    
- **Relatórios**: Foram implementados loops para iterar sobre protocolos (TCP/UDP) e portas, extraindo informações de serviços e versões através do argumento `-sV`.    
- **Timestamp**: O uso de `datetime` garante a criação de arquivos de log únicos, facilitando a organização histórica das varreduras.   
## 2. Manipulação de Pacotes com Scapy

O **Scapy** foi introduzido como uma ferramenta pika das galáxias para manipular o tráfego de rede em baixo nível.
- **Sniffing**: Captura de pacotes em tempo real para extrair IPs de origem/destino e portas de comunicação.    
- **Spoofing**: Criação de pacotes forjados (falsificação de IP de origem) para testes de segurança e simulação de ataques de rede.   
## 3. Coleta de Banners e Fingerprinting

A técnica de **Banner Grabbing** é o primeiro passo do reconhecimento para identificar o software e a versão de um serviço remoto.
- **Processo**: O script realiza uma conexão via `socket` e aguarda o recebimento da string de identificação (banner) enviada pelo servidor.    
- **Identificação**: Através da análise do banner, é possível realizar o _fingerprinting_ para determinar se um serviço é SSH, HTTP, FTP, entre outros

##  4. Análise de Logs e Identificação de Suspeitos

Logs são registros automáticos de eventos essenciais para a cibersegurança, servindo como a "caixa-preta" dos sistemas.
- **Automação de Análise**: Foi desenvolvido um script que lê arquivos de log e utiliza a biblioteca `Counter` para identificar endereços IP com excesso de falhas de autenticação (Erro **401 Unauthorized**).    
- **Filtros**: O script limpa e separa as partes do log (timestamp, IP, request, status) para focar apenas em eventos suspeitos e gerar relatórios de IPs bloqueáveis.    

## 5. Mini Ferramenta Própria: Advanced Port Scanner

Consolidando todo o aprendizado, foi criada uma ferramenta avançada de varredura multithreaded.
- **Threading**: Uso de `threading` e `Queue` para realizar varreduras simultâneas, aumentando drasticamente a velocidade do scan.    
- **Heurística**: Integração de banner grabbing com lógica de identificação de serviços para gerar relatórios detalhados em formatos `.txt` e `.csv`.  