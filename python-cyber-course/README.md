# Cybersecurity & Ethical Hacking with Python

Este repositório contém a documentação técnica consolidada e os scripts desenvolvidos durante o curso de **Python para Hackers Éticos e Cibersegurança**. O projeto abrange desde a automação de sistemas locais até a criação de ferramentas avançadas de varredura de rede e análise forense.

## Section 4: Automação de Sistemas e Terminal
Foco na integração do Python com o Sistema Operacional para auditoria e automação administrativa.

* **Bibliotecas Nucleares**: Uso estratégico de `os`, `subprocess`, `pathlib` e `datetime` para controle do host.
* **Diagnóstico Automatizado**: Execução segura de comandos como `whoami`, `ip addr`, `traceroute` e `netstat` via `subprocess.run`.
* **Auditoria de Arquivos**: Scripts para identificar arquivos modificados em tempo real e geração de logs estruturados.
* **Gestão de Relatórios**: Sistema de salvamento seguro utilizando `pathlib` para criar pastas e `datetime` para gerar timestamps únicos.

## Section 5: Redes e Programação de Sockets
Transição para a comunicação entre dispositivos e exploração de protocolos de rede.

* **Modelos de Camadas**: Estudo prático dos modelos **OSI (7 camadas)** e **TCP/IP (4 camadas)**.
* **Programação de Sockets**: Uso da biblioteca `socket` para criar conexões manuais TCP/IPv4 e interagir com servidores via verbos **HTTP (GET, POST, PUT, DELETE)**.
* **Port Scanner**: Desenvolvimento de ferramentas para identificar portas abertas e serviços alcançáveis em alvos remotos.

## Section 6: Ferramentas de Pentest e Defesa
Desenvolvimento de ferramentas profissionais e integração com frameworks de segurança.

* **Nmap Automation**: Scripts utilizando `python-nmap` para varreduras avançadas com detecção de versão de serviço (`-sV`).
* **Manipulação de Pacotes (Scapy)**: Técnicas de **Sniffing** (captura de tráfego) e **Spoofing** (falsificação de pacotes) para testes de rede.
* **Banner Grabbing**: Coleta de identificação de softwares remotos para determinar versões e possíveis vulnerabilidades.
* **Análise de Logs**: Script para detecção de invasores através de falhas de autenticação (Erro **401 Unauthorized**) utilizando `collections.Counter`.
* **Advanced Multi-IP Scanner**: Ferramenta de alta performance com suporte a múltiplos alvos e multithreading.

## Configuração do Ambiente (Arch Linux / Linux)

1. **Repositório**:
   ```bash
   git clone (https://github.com/taldoBorge/python-cyber-course/tree/master)
   cd python-cyber-course

2. **Ambiente Virtual (Venv)**:

python -m venv venv
source venv/bin/activate
pip install python-nmap scapy

3. **Execução**:
Certifique-se de ter o `nmap` instalado no sistema (`sudo pacman -S nmap`). Scripts que utilizam `Scapy` podem exigir privilégios de `sudo` para capturar pacotes de rede.

## Boas Práticas e Segurança

* **Variáveis de Ambiente**: Credenciais sensíveis nunca devem ser hardcoded no script.
* **Uso Ético**: Estas ferramentas foram desenvolvidas exclusivamente para fins educacionais e testes em ambientes controlados.
