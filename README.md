# Descriptografador e Criptografador de Arquivos

Este projeto contém dois scripts Python: um para criptografar arquivos (`encrypt.py`) e outro para descriptografá-los (`decrypt.py`). Ambos os scripts utilizam o algoritmo AES (Advanced Encryption Standard) no modo CTR (Counter).

## Requisitos

Antes de executar os scripts, certifique-se de que você possui os seguintes itens instalados:

- **Python 3.6 ou superior**
- **Biblioteca `pyaes`**

## Como usar

### Criptografar Arquivos

1. Clone ou baixe o repositório para sua máquina local.
2. Execute o script `encrypt.py` passando os arquivos que deseja criptografar como argumentos na linha de comando:

#### Exemplo de uso

Se você deseja criptografar os arquivos `teste1.txt` e `teste2.txt`, use:

```python encrypt.py teste1.txt teste2.txt```

Após a execução, os arquivos criptografados serão salvos com a extensão `.ransomwaretroll`.

### Descriptografar Arquivos

1. Execute o script `decrypt.py` passando os arquivos criptografados como argumentos na linha de comando:

#### Exemplo de uso

Se você possui os arquivos `teste1.txt.ransomwaretroll` e `teste2.txt.ransomwaretroll`, use:

```python decrypt.py teste1.txt.ransomwaretroll teste2.txt.ransomwaretroll```

Após a execução, os arquivos originais serão restaurados, sem a extensão `.ransomwaretroll`.

## Detalhes Técnicos

### Algoritmo de Criptografia

- Ambos os scripts utilizam o algoritmo AES (Advanced Encryption Standard) no modo CTR (Counter).
- A criptografia e a descriptografia utilizam uma chave de 16 bytes, a qual deve ser mantida segura e ser a mesma nos dois scripts.

## Personalização

Se necessário, você pode alterar a chave de criptografia/descriptografia nos scripts:

```python
key = b"testeransomwares"  # Substitua pela chave usada na criptografia




