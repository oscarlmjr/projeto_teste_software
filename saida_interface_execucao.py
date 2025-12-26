caminho_arquivo = 'teste.txt'

with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
	# print(arquivo.read())
	print(arquivo.readline())
	# print(arquivo.readlines())

	cont = 1
	for linha in arquivo.readline():
		print(linha)
		if cont == 6:   # linha(6)
			arquivo.write('step:	|execution_track:					|input:							|output:							|')
			arquivo.write('|---------------------------------------------------------------------------------------------------------------|')
			...
		if linha.isnumeric:   # linha(8)
			...
		# if len(linha) != 113:   # "Olá".ljust(10, '*') -> 'Olá*******'
		# 	...
	# 	if linha == '|-':   # linha(7)
	# 		...
	# 	if linha == '|':   # linha(9)
	# 		...
		cont += 1
		
# print(len('|---------------------------------------------------------------------------------------------------------------|'))
# print(len('|		|...								|(1)							|									|'))

