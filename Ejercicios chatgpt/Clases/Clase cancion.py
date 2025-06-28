class Cancion:
    def __init__(self, titulo, artista):
        self.__artista = artista
        self.__titulo = titulo

    def __str__(self):
        return f'{self.__titulo} - {self.__artista}'

    def __eq__(self, other):
        if (self.__titulo == other.__titulo) and (self.__artista == other.__artista):
            return 'Es la misma canción.'
        else:
            return 'Las canciones son diferentes.'

    def __len__(self):
        return f'El titulo de la canción tiene {len(self.__titulo)} caracteres.'

cancion1 = Cancion('No me sueltes', 'Rauw Alejandro')
print(cancion1.__str__())
print(cancion1.__len__())

cancion2 = Cancion('Desenfocao', 'Rauw Alejandro')
print(cancion1.__eq__(cancion2))