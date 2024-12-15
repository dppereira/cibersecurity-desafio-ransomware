import os
import pyaes
import sys

def descriptografar_arquivo(file_name, key):
    try:
        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Remover o arquivo criptografado
        os.remove(file_name)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
        return
    except PermissionError:
        print(f"Erro: Permissão insuficiente para acessar '{file_name}'.")
        return

    # Descriptografar os dados do arquivo
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    # Salvar o arquivo descriptografado
    original_file_name = file_name.replace(".ransomwaretroll", "")
    try:
        with open(original_file_name, "wb") as new_file:
            new_file.write(decrypt_data)
    except PermissionError:
        print(f"Erro: Não foi possível salvar o arquivo '{original_file_name}'.")

def main():
    # Verificar se ao menos um arquivo foi passado como argumento
    if len(sys.argv) < 2:
        print("Uso: python decrypt.py <arquivo1> <arquivo2> ... <arquivoN>")
        exit(1)

    # Chave de descriptografia
    key = b"testeransomwares"  # Certifique-se de usar a mesma chave usada na criptografia

    # Processar cada arquivo passado como argumento
    for file_name in sys.argv[1:]:
        descriptografar_arquivo(file_name, key)

if __name__ == "__main__":
    main()

