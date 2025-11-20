# 🔐 Simulador de Ransomware em Python

Este projeto foi desenvolvido como parte do Bootcamp do **Santander - Cibersegurança 2025**.
O objetivo é simular o funcionamento básico de um malware do tipo **Ransomware** em um ambiente controlado, para entender os conceitos de criptografia e a importância de medidas defensivas.

## 🛠️ Ferramentas Utilizadas

- **Linguagem:** Python 3
- **Biblioteca:** `cryptography` (Módulo Fernet)
- **IDE:** VS Code

## ⚙️ Como Funciona

O projeto é dividido em três scripts para demonstrar o ciclo de ataque:

1. **`gerar_chave.py`**: Cria uma chave de criptografia e a salva no arquivo `chave.key`. 
2. **`criptografar.py`**: Lê o arquivo alvo (`senhas.txt`), utiliza a chave para criptografar seu conteúdo e sobrescreve o arquivo original,  tornando o arquivo ilegível.
3. **`descriptografar.py`**: Lê o arquivo criptografado e a chave correta. Reverte o processo, trazendo o conteúdo original de volta.

## 🧪 Como Executar o Teste

1. É necessário ter o Python instalado e a biblioteca necessária:
    
    ```bash
    pip install cryptography
    
    ```
    
2. Crie um arquivo: ex.  `senhas.txt` com texto aleatório dentro.
3.  Execute os scripts na ordem:
    
    ```bash
    python gerar_chave.py  # Gera a chave.key
    python criptografar.py    # O arquivo senhas.txt ficará ilegível
    python descriptografar.py # O arquivo senhas.txt voltará ao normal
    ```
    

---

## 🛡️ Minhas Reflexões sobre Segurança

Com este desafio, percebi que a criptografia pode ser usada tanto para o bem quanto para o mal. Para evitar ser vítima de um ataque assim, os pontos principais são:

1. **Backup Offline:** Ter os dados salvos em um lugar desconectado da internet. É a única garantia de recuperar tudo sem pagar resgate.
2. **Atualizações:** Nunca ignorar os pedidos de atualização do sistema, pois eles corrigem brechas de segurança.
3. **Atenção aos Downloads:** Não baixar arquivos suspeitos, pois é assim que o Ransomware geralmente entra.
4. **Antivírus Ativo:** Manter o antivírus ligado ajuda a identificar comportamentos suspeitos antes que seja tarde.
