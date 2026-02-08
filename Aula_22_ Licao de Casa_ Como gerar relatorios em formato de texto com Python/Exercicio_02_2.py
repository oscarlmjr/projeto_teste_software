with open('sample_data/usuarios_.txt', 'r') as arquivo:
    def mega(bytes):
        return (f'{(int(usuario[c]) / (1024 ** 2)):8.2f}')

    def tamanho(uso):
        return (f'{((float(n[2]) / espaco) * 100):10.2f}')

    usuario_relatorio = []
    for linha in arquivo:
        usuario = []
        c = 0
        for u in linha.split():
            usuario.append(u)
            if c == 0:
                usuario[c] = (f'{(usuario[c]):12}')
                c += 1
                continue
            if c == 1:
                usuario[c] = mega(bytes)
        usuario_relatorio.append(usuario)

relatorio = []
c = 1
espaco = 0
for r in usuario_relatorio:
    usuario = []
    usuario = r
    usuario.insert(0, f'{(str(c)):3}')
    c += 1
    relatorio.append(usuario)
    espaco += float(usuario[2])
espaco_medio = (f'{(espaco / int(usuario[0])):.2f}')
usuario = relatorio

relatorio = []
for n in usuario:
    relatorio_usuario = n
    uso = tamanho(uso=n[2])
    n[2] = (f"{(n[2] + ' MB'):16}")

    relatorio_usuario.append(uso + ' %')
    relatorio.append(relatorio_usuario)
print(f'relatorio = \n{relatorio}')
with open('sample_data/relatorio_.txt', 'w') as arquivo:
    arquivo.writelines('ACME Inc.               Uso do espaco em disco pelos usuarios\n' \
'------------------------------------------------------------------------\n' \
'Nr.  Usuario        Espaco utilizado     % do uso\n')
    arquivo.writelines('\n')

    for r in relatorio:
        for n in r:
            arquivo.writelines(f'{n}  ')
        arquivo.writelines('\n')

    arquivo.writelines('\n')

    arquivo.writelines(f'Espaco total ocupado: {espaco} MB\n')
    arquivo.writelines(f'Espaco medio ocupado: {espaco_medio} MB\n')
