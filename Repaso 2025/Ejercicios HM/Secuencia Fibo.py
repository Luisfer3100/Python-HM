lista_fibo = [0,1]
while len(lista_fibo) < 20:
    nu_secu = lista_fibo[-2] + lista_fibo[-1]
    lista_fibo.append(nu_secu)

print(lista_fibo)