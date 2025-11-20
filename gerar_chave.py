from cryptography.fernet import Fernet

# 1 - Gera a chave
chave = Fernet.generate_key()

# 2 - Salva a chave em um arquivo
with open("chave.key", "wb") as arquivo_chave:
    arquivo_chave.write(chave)

print("Chave gerada e salva como 'chave.key'!")