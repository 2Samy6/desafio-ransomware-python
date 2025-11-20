from cryptography.fernet import Fernet
import os

# 1 - Carrega a chave que foi gerada
with open("chave.key", "rb") as arquivo_chave:
    chave = arquivo_chave.read()

fernet = Fernet(chave)

# 2 - Seleciona o arquivo a ser criptografado
arquivo_alvo = "senhas.txt"

with open(arquivo_alvo, "rb") as arquivo:
    dados_arquivo = arquivo.read()

# 3 - Criptografa os dados do arquivo
dados_criptografados = fernet.encrypt(dados_arquivo)

# 4 - Salva os dados criptografados no arquivo
with open(arquivo_alvo, "wb") as arquivo:
    arquivo.write(dados_criptografados)

print(f"O arquivo '{arquivo_alvo}' foi criptografado!")