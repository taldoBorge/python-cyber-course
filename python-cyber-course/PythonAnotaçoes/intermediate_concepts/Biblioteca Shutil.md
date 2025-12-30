Enquanto a biblioteca `os` foca na interação direta com o Sistema Operacional, a `shutil` foca na manipulação de arquivos e pastas como "objetos" de alto nível.

## Comandos Principais:
- **`shutil.move(src, dst)`**: Move arquivos/pastas de forma segura entre partições.
- **`shutil.copy2(src, dst)`**: Copia arquivos preservando metadados (data de criação, permissões). Essencial para forense digital.
- **`shutil.rmtree(path)`**: Remove um diretório e **todo** o seu conteúdo (recursivo). ⚠️ Use com cautela.
- **`shutil.make_archive(nome, 'zip', pasta)`**: Cria arquivos compactados (.zip, .tar) de uma pasta inteira.

## Uso em Cyber:
- **Exfiltração:** Compactar uma pasta de documentos sensíveis em um `.zip` e movê-la para uma pasta temporária.
- **Backup de Evidências:** Copiar logs preservando os registros de data original (`copy2`) para análise posterior.