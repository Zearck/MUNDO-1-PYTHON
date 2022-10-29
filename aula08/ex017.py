cat_op = float(input('Insira o valor do cateto oposto: '))
cat_adj = float(input('Insira o valor do cateto adjacente: '))

hip = (cat_op ** 2 + cat_adj ** 2) ** (1/2)

print("O valor da hipotenusa será de {}".format(hip))