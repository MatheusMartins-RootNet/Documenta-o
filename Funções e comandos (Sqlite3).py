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
