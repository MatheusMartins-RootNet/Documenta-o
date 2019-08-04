# Python Base
string = banana
lista = [1, '2', 3.4]
item = oi
num = 96

round(float, Quant)		# Arredonda as casas decimais de um número decimal em uma quantidade determinada

Dict  = {"Item1": "sig", "Item2": "Sig"}	# Pode ser usado para características
Lista = [Item1, Item2]				# Pode ser modficado
Tuple = (Item1, Item2)				# Pode ser usado para listar itens, porém não modificável

string.lower()						# Coloca tudo em minúsculo
string.upper()						# Coloca tudo em maiúsculo
string.captalize()					# Coloca a primeira letra da palavra maiúscula
string.count('Entrada')				# Conta quantas vezes a entrada aparece na string
string.endwith('Entrada')			# Verifica se a string termina com tal entrada (True or False)
string.replace('Entrada', 'Saida')	# Substitui a palavra de entrada (à ser substituida) pela palavra de saída (Substituição)
string.split('Entrada')				# Separa a string usando a entrada como repartição
string.startwith('Entrada')			# Verifica se a string começa com tal entrada (True or False)
string.isalpha()					# Retorna True se existir somente letras, e false se tiver qualquer outro caractere
string.strip()						# Retira os espaços da frase
string.strip(', .')					# Define o que retirar dentro da frase


lista.append('Entrada')		# Insere tal entrada em uma lista
del lista['Entrada']		# Apaga os itens de uma lista (pode ser usado como [item1 : item2])
lista.count('Entrada')		# Exibe quantas vezes tal item foi achado na lista
lista.extend('Lista 2')		# Adiciona ao final da lista 1, os itens da lista 2
lista.insert(Pos, 'Entrada')	# Insere em tal posição, a entrada na lista
lista.index('entrada')
lista.remove('Entrada')		# Remove tal entrada de uma lista
lista.reverse()		        # Inverte a ordem de uma lista
lista.sort()			# Ordena em alfanumérico a lista

chr(num)		# Trás o valor real do número ASCII
','.join(lista)	# Irá transformar a lista em uma string usando o ', ' como junção entre os itens da lista
max('Lista')	# Soma todos os itens da lista
min('Lista')	# Subtrai todos os itens da lista
ord(item)		# Trás o valor ASCII do item
sorted(lista)           # Ordena uma lista em alfanumérico
