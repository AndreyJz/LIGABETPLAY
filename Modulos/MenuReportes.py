import os

def crearMenu():
    lstOpciones = ['A', 'B', 'C', 'D', 'E','F']
    opciones = ['A. Equipo Goleador', 'B. Equipo con mas Puntos', 'C. Equipo que mas partidos gano','D. Total goles anotados', 'E. Promedio de goles en el torneo' 'F. Salir menu principal']
    os.system('clear')
    titulo = """
    ++++++++++++++++++++++++++++++++++++
    +       LIGA BETPLAY Reportes      +
    ++++++++++++++++++++++++++++++++++++
    """
    print(titulo)
    for item in opciones:
        opciones = 'A. Equipo Goleador\nB. Equipo Mas Puntos\nC. Equipo que mas partidos gano\nD. Total goles anotados\nE. Promedio de goles en el torneo\nF. Salir menu principal'
        print(opciones)
        try:
            opr = input('Escriba el apartado que quiere ver: ').upper()
        except:
            print('Error en la opcion')
            os.system('pause')
            crearMenu()  
        else:
            return opr
        
def TotalGoles(lstEquipos: dict):
    GolesTotales = 0
    for key,value in lstEquipos.items():
        GolesTotales += (value['GF'] + value['GC']) / 2
    return GolesTotales

def TotalPardidos(lstEquipos: dict):
    PartidosTotales = 0
    for key,value in lstEquipos.items():
        PartidosTotales += (value['PJ']) / 2
    return PartidosTotales

def EquipoMAXPuntos(lstEquipos: dict):
    MAXpuntos = 0
    EQMAXpuntos = None
    puntos = 0
    nombre = None

    for key,value in lstEquipos.items():
        MAXpuntos += value['TP']
        EQMAXpuntos = value['NombreEquipo']
        if value['TP'] > puntos:
            puntos += value['TP']
            nombre = EQMAXpuntos

    return puntos, nombre

def EquipoMAXGoles(lstEquipos: dict):
    MAXgoles = 0
    EQMAXgoles = None
    goles = 0
    nombre = None

    for key,value in lstEquipos.items():
        MAXgoles += value['GF']
        EQMAXgoles = value['NombreEquipo']
        if value['GF'] > goles:
            goles += value['GF']
            nombre = EQMAXgoles

    return goles, nombre

def EquipoMAXwins(lstEquipos: dict):
    MAXwins = 0
    EQMAXwins = None
    wins = 0
    nombre = None

    for key,value in lstEquipos.items():
        MAXwins += value['PG']
        EQMAXwins = value['NombreEquipo']
        if value['PG'] > wins:
            wins += value['PG']
            nombre = EQMAXwins

    return wins, nombre


def PromGoles(lstEquipos):
        GolesTotales = TotalGoles(lstEquipos)
        PartidosTotales = TotalPardidos(lstEquipos)

        return (GolesTotales / PartidosTotales)
