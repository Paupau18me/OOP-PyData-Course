class CamaraDigital:

    '''
    Esta clase describe una camara digital y sus funciones
    '''

    def __init__(self, marca, modelo, precio, peso, enfoque_auto, resolucion):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.peso = peso
        self.enfoque_auto = enfoque_auto
        self.resolucion = resolucion

    def __str__(self):
        return ('Marca: {}, Modelo: {}, Precio: {}$, Peso: {}g, Enfoque automatico: {}, Resolucion: {}Mpx').format(self.marca, self.modelo, self.precio, self.peso, self.enfoque_auto, self.resolucion)

    def enfocar(self):
        if self.enfoque_auto == 'Si':
            print('Ya cuenta con enfoque automaticamatico')
        else:
            print('Enfocando...')
            print('Enfocado correctamente!')

camara1 = CamaraDigital('Sony', 'D500', 2000, 760, 'No', 20.6)
print(camara1.__str__())
camara1.enfocar()


print('_________________________________________________________\n')

class HacedorPanes():

    '''
    Esta clase describe a las perosnas que hacen pancito y sus funciones
    '''

    def elaborar_masa(self):
        print('Masa elaborada')

    def hornear(self):
        print('Horneando...')

    def contar_chiste_panadores(self):
        print('''    - ¡Mamá! ¡Mamá! ¿Cuando comeremos pan de hoy?
    - Mañana, hijo, mañana.
        ''')

baker = HacedorPanes()
baker.elaborar_masa()
baker.hornear()
baker.contar_chiste_panadores()