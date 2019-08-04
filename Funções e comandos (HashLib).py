# HashLib
import hashlib

# hashlib.md5(texto.encode())	 Define que a criptografia será MD5
# hashlib.sha(texto.encode())	 Define que a criptografia será SHA

resultado = hashlib.md5(texto.encode())	# Criptografa o texto
resultado.hexdigest()	# Saida do texto criptografado
