import mysql.connector
from datetime import datetime

conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="parqueo"
)     

def menu():
    while True:
        print("\n--- PARKCONTROL ---")
        print("1. Registrar ingreso")
        print("2. Consultar vehiculos")
        print("3. Registrar salida")
        print("4. Eliminar registro")
        print("5. Salir")

        desi = input("Seleccione una opcion: ")

        if desi == "1":
            registro()
        elif desi == "2":
            consultar()
        elif desi == "3":
            actualizar()
        elif desi == "4":
            eliminar()
        elif desi == "5":
            print("Programa finalizado")
            break
        else:
            print("Opcion no valida")

menu()

def agregar():
    ownerName=input("Nombre del propietario: ")
    licensePlate=input("Numero de placa: ")

    print("1. Car")
    print("2. Motorcycle")
    print("3. Truck")

    desi = input("Seleccione el tipo de vehículo: ")

    if desi == "1":
        vehicleType = "Car"
    elif desi == "2":
        vehicleType = "Motorcycle"
    elif desi == "3":
        vehicleType = "Truck"
    else:
        print("Tipo de vehículo no válido")
        return

    entryTime = datetime.now()
    status = "Inside"
    cursor = conexion.cursor()
    query = "INSERT INTO vehiculo(ownerName, licensePlate, vehicleType, entryTime, status) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query,(ownerName, licensePlate, vehicleType, entryTime, status))
    conexion.commit()
    print("Vehículo registrado correctamente")

agregar()
 
def consultar():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM vehiculo")
    registro = cursor.fetchall()
    if registro:
        for vehiculo in registro:
            print(vehiculo)
    else:
        print("No hay vehiculos registrados")

consultar()

def actualizar():
    id = int(input("Ingrese el ID del vehiculo: "))
    cursor = conexion.cursor()
    cursor.execute("SELECT status FROM vehiculo WHERE id = %s",(id,))
    vehiculo = cursor.fetchall()
    if vehiculo is None:
        print("Vehiculo no encontrado")
    elif vehiculo (0) == "Exited":
        print("El vehiculo ya registro su salida")
    else:
        exitTime = datetime.now()
        query="UPDATE vehiculo SET exitTime = %s, status = %s WHERE id = %s"
        valores = (exitTime, "Exited", id)
        cursor.execute(query, valores)
        conexion.commit()
print("Salida registrada correctamente")

actualizar()


def eliminar():
    id = int(input("Ingrese el ID del vehiculo a eliminar: "))
    cursor = conexion.cursor()
    query="DELETE FROM vehiculo WHERE id = %s"
    cursor.execute(query, (id,))
    conexion.commit()
    if cursor.rowcount > 0:
        print("Registro eliminado correctamente")
    else:
        print("No se encontro el vehiculo")

eliminar()

cursor.close()