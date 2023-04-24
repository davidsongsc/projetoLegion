from cryptography.fernet import Fernet

# gera uma chave de criptografia
key = Fernet.generate_key()

# cria um objeto Fernet com a chave gerada
fernet = Fernet(key)

# texto a ser criptografado
texto = "lubia"

# criptografa o texto
texto_criptografado = fernet.encrypt(texto.encode())

# descriptografa o texto
texto_descriptografado = fernet.decrypt(texto_criptografado).decode()

# imprime o texto original, o texto criptografado e o texto descriptografado
print("Texto original:", texto)
print("Texto criptografado:", texto_criptografado)
print("Texto descriptografado:", texto_descriptografado)
