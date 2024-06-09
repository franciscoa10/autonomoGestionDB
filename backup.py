import mysql.connector
import subprocess

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)

def respaldo():
    try:
        usuario = input("Ingresa el nombre del usuario: ")
        contrasena = input("Ingresa la contraseña: ")
        nombre_db = input("Ingrese el nombre de la base de datos a respaldar. ")
        archivo_respaldo = input("Ingrese el nombre para el archivo.sql(ubique el '.sql' al final): ")
        
        with open(f'C:/bibliotecaRespaldo/{archivo_respaldo}', 'w') as out:
            subprocess.Popen(f'"C:/Program Files/MySQL/MySQL Workbench 8.0 CE/"mysqldump --user={usuario} --password={contrasena} --databases {nombre_db}', shell=True, stdout=out)
    
    except subprocess.CalledProcessError as error:
        print(f"Error al ejecutar el comando: {error}")
    finally:
        print("Respaldo generado satisfactoriamente.")
        print("Presione enter para regresar al menú..")
        input()




def restaurar():
    try:
        usuario = input("Ingresa el nombre del usuario: ")
        contrasena = input("Ingresa la contraseña: ")
        archivo_respaldo = input("Ingrese el nombre para el archivo.sql(ubique el '.sql' al final): ")
        subprocess.Popen(f'"C:/Program Files/MySQL/MySQL Workbench 8.0 CE/mysql" --user={usuario} --password={contrasena} < C:/bibliotecaRespaldo/{archivo_respaldo}', shell=True)
        
        
    except subprocess.CalledProcessError as error:
        print(f"Error al ejecutar el comando: {error}")
    finally:
        print("Restauración generada satisfactoriamente.")
        print("Presione enter para regresar al menú..")
        input()