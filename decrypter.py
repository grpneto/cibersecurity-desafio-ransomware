## Comando usado para importar a biblioteca de criptografia
import os
import pyaes

## Comando usado para abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Chave de 16 bytes usada para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## O arquivo criptografado é removido, mas o seu conteúdo permanece
os.remove(file_name)

"""
O arquivo descriptografado é criado. A descriptografia só será feita com o uso do comando
decrypter.py
"""
new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
