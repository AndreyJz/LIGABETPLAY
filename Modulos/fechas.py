import os
from tabulate import tabulate
lstFechas = {}

def AddGame(lstEquipos:dict,lstFechas:dict):
    os.system('cls')
    titulo = """
        +++++++++++++++++++++++++++++++++++++
        +   REGISTRO DE FECHA LIGA BETPLAY  +
        +++++++++++++++++++++++++++++++++++++

        Estos son los Equipos Registrados:
    """
    print(titulo)
    for key,value in enumerate(lstEquipos):
        print(value)
    
    nroFecha = int(input('Ingrese el numero de fecha : '))
    if nroFecha in lstFechas:
        print(f'Ya existe una fecha con el número {nroFecha}.')
    else:
        fecha = {}
        local = input('Ingrese el equipo local ')
        visitante = input('Ingrese el equipo visitante ')
        dataL = lstEquipos.get(local,False)
        dataV = lstEquipos.get(visitante,False)
        if(type(dataL and dataV) == dict):
            golesL = int(input(f'Ingrese los goles marcador por {local} : '))
            golesV = int(input(f'Ingrese los goles marcador por {visitante} : '))
            if(type(golesL and golesV) == int):
                fecha[local] = {'nombre':local, 'goles':golesL, 'estado':'L'}
                fecha[visitante] = {'nombre':visitante, 'goles':golesV, 'estado':'V'}
                
                lstEquipos[local]['GF'] += fecha[local]['goles']
                lstEquipos[local]['GC'] += fecha[visitante]['goles']
                lstEquipos[visitante]['GF'] += fecha[visitante]['goles']
                lstEquipos[visitante]['GC'] += fecha[local]['goles']
                
                if fecha[local]['goles']>fecha[visitante]['goles']:
                    print(f'El equipo {local} le gano a {visitante}')
                    lstEquipos[local]['PJ'] += 1
                    lstEquipos[local]['PG'] += 1
                    lstEquipos[visitante]['PJ'] += 1
                    lstEquipos[visitante]['PP'] += 1
                    lstEquipos[local]['TP'] += 3
                elif fecha[visitante]['goles']>fecha[local]['goles']:
                    print(f'El equipo {visitante} le gano a {local}')
                    lstEquipos[local]['PJ'] += 1
                    lstEquipos[visitante]['PG'] += 1
                    lstEquipos[visitante]['PJ'] += 1
                    lstEquipos[local]['PP'] += 1
                    lstEquipos[visitante]['TP'] += 3
                else:
                    print(f'El equipo {visitante} empato con {local}')
                    lstEquipos[local]['PJ'] += 1
                    lstEquipos[local]['PE'] += 1
                    lstEquipos[visitante]['PJ'] += 1
                    lstEquipos[visitante]['PE'] += 1
                    lstEquipos[local]['TP'] += 1
                    lstEquipos[visitante]['TP'] += 1
                
                
                lstFechas.update({nroFecha:fecha})
            
            else:
                os.system('cls')
                print('Dato erroeno, solo puede ingresar numeros')
                os.system('pause')
            
        else:
            print('Alguno de los equipos no se encuentra registrado, registrelo primero')
            os.system('pause')

def ViewDates(lstFechas:dict):
    os.system('cls')
    titulo = """
    +++++++++++++++++++++++++++++++++++
    + TABLA DE FECHAS DE LIGA BETPLAY +
    +++++++++++++++++++++++++++++++++++
    """
    print(titulo)
    tabla=[]
    for llave,fecha in lstFechas.items():
        for key,partido in fecha.items():
            tabla.append([llave, lstFechas[llave][key]['nombre'], lstFechas[llave][key]['goles'], lstFechas[llave][key]['estado']])
    print(tabulate(tabla, headers=['NroFecha', 'nombre', 'goles','estado'], tablefmt='grind'))
    os.system('pause')
    pausa = input('')