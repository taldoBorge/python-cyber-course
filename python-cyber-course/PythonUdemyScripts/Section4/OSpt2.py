import os
import time


path = "."#current path
today = time.strftime("%Y-%m-%d")#capture today's date

with open("log.txt", "w") as log: #Creates or modifies/overwrites the log file.
    for archive in os.listdir(path):
        if archive.endswith(".py"):
            modified = time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(archive)))
            if modified == today:
                log.write(f"{archive} was modified today.\n")






#É muito importante preferir o uso da biblioteca subprocess pra coisas mais serias por ser mais segura e moderna, devemos evitar comandos dinamicos sem verificação pra evitar injeção de comandos
#Sempre preferir scripts que usem logs por facilitar a auditoria e investigações pq ja separa o que foi feito e quando
#Nunca execute os.system com dados diretamente do usuarios ou fontes não confiaveis sem validação ou sanitização adequada pq isso facilita o ataque de injeção de comandos e uso de exploits