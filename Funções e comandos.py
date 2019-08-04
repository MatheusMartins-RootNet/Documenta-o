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



# Math
import math

math.sqrt(Num)		# Irá dar a raiz quadrada de um número
math.sin(Num)		# Irá dar o seno de um número
math.cos(Num)		# Irá dar o cosseno de um número
math.tan(Num)		# Irá dar a tangente de um número
math.pi			# Irá dar o valor de PI para calcular
math.hypot(X, Y)	# Retorna a hipotenusa dos catetos fornecidos


# Random
import random

random.randint(min, max)	# Irá dar um número entre o intervalo definido com o max -1
random.random()			# Irá retornar um número decimal entre 0 e 1
random.choice(list)		# Irá retornar um item aleatório da lista
random.sample(list, Quant)	# Irá retornar uma quantidade definida de itens aleatórios em uma lista
random.shuffle(list)		# Embaralha uma lista
random.uniform(min, max)	# Irá retornar um número decimal entre este intervalo


# Sqlite3
import sqlite3

banco = sqlite3.connect('Nome.db')	#Se conecta a um banco de dados desejado
cursor = banco.cursor()		# Cria um cursor (Meio de comandar o banco)
banco.commit()	# Salva o banco de dados
banco.close()	# Fecha o banco de dados

cursor.execute('CREATE TABLE Nome (Nome1 Tipo1, Nome2 Tipo2, Nome3 Tipo3)')	# Cria uma tabela com tais atributos
cursor.execute('CREATE TABLE IF NOT EXISTS Nome (Nome1 Tipo1, Nome2 Tipo2, Nome3 Tipo3)')	#Cria uma tabela se ela nao existir
cursor.execute('CREATE TABLE Nome (Inteiro  Integer, Float Real, Texto Text, Booleano Boolean)')
# Tipos de valores
# Integer = Número Inteiro
# Real    = Número Decimal
# Text    = Texto
# Boolean = Booleano

# Tipo de atributos
# NOT NULL = Não nulo (tem que ter algo)
# IF NOT EXISTS = Se não existir
# VARCHAR() = Tamanho do valor
# PRIMARY KEY AUTOINCREMENT = Criar Id dos itens

cursor.execute('INSERT INTO Tabela (Nome1, Nome2, Nome3) VALUES (Valor1, Valor2, Valor3)')	# Irá inserir na tabela tais valores exatos
cursor.execute('INSERT INTO Tabela (Nome1, Nome2, Nome3) VALUES (?, ?, ?)', (Valor1, Valor2, Valor3))	# Irá inserir na tabela a partir de valores externos (variáveis)

cursor.executemany('INSERT INTO Nome (Tipo1, Tipo2, Tipo3) VALUES (?, ?, ?)', Lista)	# Insere valores de uma lista completa no banco de dados

cursor.execute('SELECT * FROM Tabela')	# Irá selecionar tudo da tabela desejada
cursor.execute('SELECT Filtro FROM Tabela')	# Irá selecionar tudo que estiver no Nome1
cursor.fetchall()	# Irá trazer o resultado do comando anterior
cursor.execute('ALTER TABLE Tabela ADD COLUMN Nome Tipo')	# Adiciona uma nova coluna na tabela Nome
cursor.execute('UPDATE Tabela SET Filtro = ?, Filtro2 = ? WHERE Item = ?', (Filtro, Filtro2, Item))	# Irá atualizar o item tal, dentro da tabela, para um novo valor
cursor.execute('DELETE FROM Tabela WHERE Filtro = ?, Filtro2 = ?', (Filtro, Filtro2,))	# Irá apagar um item de tal tabela, com filtro tal


# DateTime
import datetime
from time import strftime

datetime.datetime.now().strftime('%d|%m|%Y') # Jeito completo

strftime('%d|%m|%Y')  # Jeito mais simples

# %d = Dia  |  %m = Mês  |  %Y = Ano

# %H = Hora 24H
# %I = Hora 12H
# %p = AM / PM
# %M = Minuto
# %S = Segundo

# %w = Dia da semana (em número)
# %D = Dia abreviado
# %b = Mês abreviado
# %y = Ano abreviado
# %j = Dia no ano


# HashLib
import hashlib

# hashlib.md5(texto.encode())	 Define que a criptografia será MD5
# hashlib.sha(texto.encode())	 Define que a criptografia será SHA

resultado = hashlib.md5(texto.encode())	# Criptografa o texto
resultado.hexdigest()	# Saida do texto criptografado


# Operational Sistem
import os

os.system('Comando')	# Executa comandos através do python
os.dir()	# Exibe o diretório atual
os.name		# Exibe o tipo de sistemas (nt = windows)
os.mkdir()	


# Arquivos CSV
import csv

variavel = csv.reader(open('ARQUIVO'), delimiter=';')   # Abre o arquivo e insere ele dentro da variável
# A variável é uma lista, ou seja, precisa de um : for i in variavel : para ser lida, e o resultado sairá como outras listas menores
# Para ter cada item do CSV como um item unico use

for i in variavel:
    for j in i:
        return j    # No lugar do return, coloque a saida no modo que você desejar


# Sys (Passagem de argumentos)
import sys

sys.argv  # Irá pegar os argumentos passados (igual uma lista, tudo que vem depois do comando python/python3) como string
