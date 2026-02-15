from scapy.all import sniff, TCP

# Função chamada a cada pacote capturado
def mostrar_pacote(pacote):
    if pacote.haslayer(TCP):  # filtra apenas pacotes TCP
        print(f"[+] Pacote TCP capturado:")
        print(f"    IP Origem -> {pacote[0][1].src}")
        print(f"    IP Destino -> {pacote[0][1].dst}")
        print(f"    Porta Origem -> {pacote[TCP].sport}")
        print(f"    Porta Destino -> {pacote[TCP].dport}")
        print("-" * 40)

# Inicia o sniffing (CTRL+C para parar)
print("[*] Iniciando captura de pacotes TCP...")
sniff(prn=mostrar_pacote, filter="tcp", store=0)