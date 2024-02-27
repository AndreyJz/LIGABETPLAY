import Modulos.MenuReportes as mr
import Modulos.menu as mp
import Modulos.equipos as e
import Modulos.fechas as f
if __name__ == '__main__' :
    equiposLiga = {}
    fechas = {}
    isAppRuning = True
    while isAppRuning:
        op=mp.CrearMenu()
        if(op ==1):
            isAddTeam = True
            while isAddTeam:
                e.os.system('cls')
                e.AddTeam(equiposLiga)
                isAddTeam = bool(input('Desea agregar otro equipo S(si) o Enter(no)'))
        elif(op == 2):
            isAddDate = True
            while isAddDate:
                    e.os.system('cls')
                    f.AddGame(equiposLiga,fechas)
                    isAddDate = bool(input('Quieres seguir agregando una fecha? S (si) Enter (No)\n'))
        elif(op == 3):
            isreport = True
            while isreport:
                opr= mr.crearMenu()
                if (opr == 'A'):
                    MAXgoles, EQMAXgoles  = mr.EquipoMAXGoles(equiposLiga)
                    print(f'El equipo con más goles es {EQMAXgoles} con {MAXgoles} goles')
                    print('Enter para ir al menu de reportes')
                    mr.os.system('pause')
                elif (opr == 'B'):
                    MAXpuntos, EQMAXpuntos  = mr.EquipoMAXPuntos(equiposLiga)
                    print(f'El equipo con más goles es {EQMAXpuntos} con {MAXpuntos} goles')
                    print('Enter para ir al menu de reportes')
                    mr.os.system('pause')
                elif (opr == 'C'):
                    MAXwins, EQMAXwins  = mr.EquipoMAXwins(equiposLiga)
                    print(f'El equipo con más goles es {EQMAXwins} con {MAXwins} goles')
                    print('Enter para ir al menu de reportes')
                    mr.os.system('pause')
                elif (opr == 'D'):
                    GolesTotales  = mr.TotalGoles(equiposLiga)
                    print(f'El total de goles que fueron anotados en el torneo es {GolesTotales}')
                    print('Enter para ir al menu de reportes')
                    mr.os.system('pause')
                elif (opr == 'E'):
                    PromGoles  = mr.PromGoles(equiposLiga)
                    print(f'El promedio de los goles anotados en el torneo es {PromGoles}')
                    print('Enter para ir al menu de reportes')
                    mr.os.system('pause')
                elif (opr == 'F'):
                    isreport=False
        elif(op == 4):
            isDelTeam = True
            while isDelTeam:
                e.os.system('cls')
                e.DelTeam(equiposLiga)
                isDelTeam = bool(input('Desea seguir borrando equipos? S(si) o Enter(no) '))
        elif(op == 5):
            isViewTeams = True
            while isViewTeams:
                e.os.system('cls')
                e.ViewTeams(equiposLiga)
                isViewTeams = bool(input('Desea seguir viendo la lista? S(si) o Enter(no) '))
        elif(op == 6):
            isViewDates = True
            print('Fuera de servicio')
            e.os.system('pause')
            while isViewDates:
                e.os.system('cls')
                f.ViewDates(fechas)
        elif(op == 7):
            isAppRuning=False
