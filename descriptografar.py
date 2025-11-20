from cryptography.fernet import Fernet
import os

# 1 - Carrega a chave
with open("chave.key", "rb") as arquivo_chave:
    chave = arquivo_chave.read()

fernet = Fernet(chave)

# 2 - Ler o arquivo criptografado
arquivo_alvo = "senhas.txt"

with open(arquivo_alvo, "rb") as arquivo:
    dados_criptografados = arquivo.read()

# 3 - Descriptografa os dados do arquivo
dados_originais = fernet.decrypt(dados_criptografados)

# 4 - Salva os dados descriptografados no arquivo
with open(arquivo_alvo, "wb") as arquivo:
    arquivo.write(dados_originais)

print(f"O arquivo '{arquivo_alvo}' foi recuperado com sucesso!")