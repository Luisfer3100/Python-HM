tweet = input('Ingresa el tweet: ')

if 0 < len(tweet) <= 20:
    print('Su tweet se ha publicado.')
elif len(tweet) > 20:
    print('Su tweet es demasiado largo.')
else:
    print('No se publican tweets vacios.')