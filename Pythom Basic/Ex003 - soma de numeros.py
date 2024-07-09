n1 = int(input("digite um numero:"))
n2 = int(input("digite outro numero:"))
s = n1 + n2
# pode ser esse: print("A soma de", n1, "e", n2, "o resultado é:", s)
# o codigo que está em baixo é mais recomendado
print("A soma de {} com {} o resultaado é {}".format(n1,n2,s))
