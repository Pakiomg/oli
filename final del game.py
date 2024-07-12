
import random
import os
import csv

nombres_de_trabajadores=["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel","Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"

sueldos_de_trabajadores=[]

with open("sueldos.csv, 'w' , newline ==","utf-8")as archivo:
    archivo.write("nombre,sueldo,descuento,afp,sueldo_liquito\n")
    
    
def asignar_sueldos_aleatorios=[]
    sueldos={empleado: random.randint(300000,25000000)for empleado in empleados}
    return sueldos
    


def clasificacion_de_sueldos=[]
menores_300000=[]
intermedio_
mayores_25000000=[]

def ver_estadisticas(sueldos):
    total= sum(sueldos.values)
    promedio= total/ len(sueldos)
    max_sueldo = max(sueldos.values)
    min_sueldo = max(sueldos.values)
    return {
        'total':total,
        'promedio': promedio,
        'maximo': max_sueldo,
        'minimo': min_sueldo
    }

def report_sueldos(sueldos):
    for empleado, sueldo in sueldos.items():
        print(f"{empleado}: ${sueldo}")
        

for empleado in empleados:
if empleados=["sueldo"]<300000:
    menores_300k.append(empleado)
elif 300000<=empleado["sueldo"]<=25000000:
    entre_300000


def menu():
sueldos={}
while True:
print("\n,menu")
print(1. "Asignar sueldos aleatorios")
print(2. "Clasificar sueldos")
print(3. "Ver estadísticas")
print(4. "Reporte de sueldos")
print(5. "Salir del programa")
opcion = input("selecione una opcion:")

if opcion=="1":
    sueldos= asignar_sueldos()
    print("sueldos asignados.")
elif opcion =="2":
    if sueldos:
        clasificacion=
        clasificar_sueldos=(sueldos)
        for categoria,empleados in
        clasificacion.items():
                            print(f"\n{categoria}:")
                            for empleo, sueldo in
empleados.items():
    print(f"{empleado}:$ {sueldo}")
    else:
        print("primero debe asignar suledos.")
    elif opcion=="3":
        if sueldos:
            estadisticas=
            ver_estadisticas(sueldos)




   
