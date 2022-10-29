cidade = str(input('Nome da cidade: '))

cid = cidade.split()
ci = bool(cid[0] == 'Santo')

print('A cidade em questão {}, apresenta o palavra Santo? {}'.format(cidade, ci))
