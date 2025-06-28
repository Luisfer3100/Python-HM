# Se pide que el usuario ingrese su tweet.
tweet = str(input('Escribe aqui: ')).rstrip() # Esto me puede ayudar a que si el ususario ingresa solo un espacio en blanco, se borre y se tome como que
# es un tweet vacio

# Control de flujo para imprimir si es valido o no el tweet (recordar que el maximo de caracteres para un tweet es de 20).
if 0 < len(tweet) <= 20: # En las primeras pruebas que le hice a mi codigo, al pasar un tweet vacio, me tomaba por bueno esta condicion, pero me di cuenta que solo
    # le indique a esta condicion que se aplicara si el largo es menor al 20, lo cual incluye si es igual a 0. Entonces recorde que puedo usar operadores logicos.
    # Para esto indique que si 0 es menor a el largo del tweet y menor o igual a 20, se lleve a cabo esta condicon.
    print('Su tweet de ha publicado.')
elif len(tweet) > 20:
    print('Ha sobrepasado el limite de su publicación.')
elif tweet == '':
    print('No se puede publicar un tweet vacio.')

