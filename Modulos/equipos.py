import os
from tabulate import tabulate
Equipos={}
def AddTeam(lstEquipos:dict):
    NombreEquipo = input('Escriba el nombre del equipo : ')
    data = lstEquipos.get(NombreEquipo,False)
    if (type(data) == dict):
        print('Este equipo ya se encuentra registrado')
        os.system('pause')
    elif(type(data) == bool and data == False):
        Equipos={
        'NombreEquipo':NombreEquipo,
        'PJ':0,
        'PG':0,
        'PP':0,
        'PE':0,
        'GF':0,
        'GC':0,
        'TP':0   
        }
        lstEquipos.update({NombreEquipo:Equipos})
        print(lstEquipos)
    

def ValidateStudent(lstEquipos:dict,NombreEquipo)-> bool:
    return bool(lstEquipos.get(NombreEquipo,''))

def DelTeam(lstEquipos:dict):
    NombreEquipo = input('Ingrese el nombre al equipo a borrar: ')
    if (ValidateStudent(lstEquipos,NombreEquipo)):
        lstEquipos.pop(NombreEquipo)
    else:
        print(f'El equipo {NombreEquipo} no se encuentra registrado')
        os.system('pause')


def ViewTeams(lstEquipos : dict):
    os.system('cls')
    titulo = """
    +++++++++++++++++++++++++++++++++++++++
    + TABLA DE POSICIONES DE LIGA BETPLAY +
    +++++++++++++++++++++++++++++++++++++++
    """
    print(titulo)
    tabla = [[value, lstEquipos[value]['PJ'], lstEquipos[value]['PG'], lstEquipos[value]['PP'], lstEquipos[value]['PE'], lstEquipos[value]['GF'], lstEquipos[value]['GC'], lstEquipos[value]['TP']] for value in lstEquipos]
    tabla_ordenada = sorted(tabla, key=lambda x: x[7], reverse=True)
    print(tabulate(tabla_ordenada, headers=['Equipo', 'PJ', 'PG','PP','PE','GF','GC','TP']))
    os.system('pause')
    pausa = input('')

