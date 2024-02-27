import os

def CrearMenu():
    lstOpciones = [1, 2, 3, 4, 5, 6, 7]
    opciones = ['1. Registrar Equipo', '2. Registrar Fecha', '3. Reportes', '4.Eliminar Equipo', '5. Lista de Posiciones', '6. Lista Fechas(Fuera de servicio)', '7. Salir']
    os.system('cls')
    titulo = """
    ++++++++++++++++++++++++++++++++++++
    +   LIGA BETPLAY Reportes  +
    ++++++++++++++++++++++++++++++++++++
    """
    print(titulo)
    for item in opciones: 
        try:
            opciones = '1. Agregar equipo\n2. Registrar Fecha\n3. Reportes\n4. Eliminar Equipo\n5. Lista de Posiciones\n6. Lista Fechas(Fuera de servicio)\n7. Salir'
            print(opciones)
            op = int(input(':)_'))
            if (op not in lstOpciones):
                CrearMenu() 
        except ValueError:
            print('Dato invalido')
            os.system('pause')
            CrearMenu() 
        else:
            return op