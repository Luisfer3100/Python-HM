import math

# El metodo ceil, retorna el numero entero mas cercano hacia arriba
numero = math.ceil(7.1)
print(numero)

# El metodo floor al igual que ceil retorna el numero entero mas cercano pero hacia abajo
numero = math.floor(7.9)
print(numero)

# isnan, retorna un booleano
booleano = math.isnan(23)
print(booleano)

# Para poder sacar la potencia de algun número ya vimos que se puede hacer con **, pero math tiene un metodo para esto:
numero = math.pow(5, 3)
print(numero)

# Para la raiz cuadrada tenemos sqrt
numero = math.sqrt(25)
print(numero)
