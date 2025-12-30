#Possível resposta do exercício ->


import subprocess
from pathlib import Path
from datetime import datetime

# Pasta onde os arquivos serão salvos
BASE_DIR = Path("relatorios")
BASE_DIR.mkdir(exist_ok=True)

# Timestamp para diferenciar os arquivos
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

def salvar_saida(comando, nome_arquivo):
    """Executa um comando e salva sua saída em arquivo"""
    try:
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            shell=True  # necessário no Windows para rodar ipconfig/tracert
        )
        caminho = BASE_DIR / f"{nome_arquivo}_{timestamp}.txt"
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(f"Comando: {' '.join(comando)}\n")
            f.write(f"Código de saída: {resultado.returncode}\n\n")
            f.write("Saída:\n")
            f.write(resultado.stdout)
            f.write("\nErros:\n")
            f.write(resultado.stderr)
        print(f"[+] Saída de {comando[0]} salva em {caminho}")
    except Exception as e:
        print(f"Erro ao executar {comando}: {e}")

# Executa e salva os três comandos
salvar_saida("whoami", "whoami")
salvar_saida("ip addr", "ip_info")
salvar_saida("ping -c 4 8.8.8.8", "ping_teste")




