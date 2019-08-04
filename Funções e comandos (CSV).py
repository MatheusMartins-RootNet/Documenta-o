# Arquivos CSV
import csv

variavel = csv.reader(open('ARQUIVO'), delimiter=';')   # Abre o arquivo e insere ele dentro da variável
# A variável é uma lista, ou seja, precisa de um : for i in variavel : para ser lida, e o resultado sairá como outras listas menores
# Para ter cada item do CSV como um item unico use

for i in variavel:
    for j in i:
        return j    # No lugar do return, coloque a saida no modo que você desejar
