import mysql.connector


conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)

HOST = 'localhost'


def añadirUsuario():
    try:
        usuario = input("Ingresa el nombre del usuario: ")
        contraseña = input("Ingresa la contraseña: ")
        cursor = conexion.cursor()
        sentencia = f"CREATE USER '{usuario}'@'{HOST}' IDENTIFIED BY '{contraseña}'"
        cursor.execute(sentencia)

        conexion.commit()
        print("Usuario añadido correctamente.")
    
    except mysql.connector.Error as error:
        print("Error al añadir usuario:", error)

    finally:
        cursor.close()
        print("Cursor cerrado.")



def actualizarUsuario():
    try:
        usuario = input("Ingresa el nombre del usuario que quiere actualizar: ")
        nuevoUsuario = input("Ingresa el nuevo nombre del usuario: ")
        contraseña = input("Ingresa la nueva contraseña: ")
        cursor = conexion.cursor()
        
        sentencia = f"RENAME USER '{usuario}'@'{HOST}' TO '{nuevoUsuario}'@'{HOST}'"
        cursor.execute(sentencia)
        conexion.commit()
        
        sentencia2 = f"ALTER USER '{nuevoUsuario}'@'{HOST}' IDENTIFIED BY '{contraseña}'"
        cursor.execute(sentencia2)
        conexion.commit()
        
        print("Usuario actualizado correctamente.")
    
    except mysql.connector.Error as error:
        print("Error al actualizar usuario:", error)

    finally:
        cursor.close()
        print("Cursor cerrado.")


def eliminarUsuario():
    try: 
        usuario = input("Ingresa el nombre del usuario a ser eliminado: ")
        cursor = conexion.cursor()
        sentencia = f"DROP USER '{usuario}'@'{HOST}'"
        cursor.execute(sentencia)
        
        conexion.commit()
        print("Usuario eliminado correctamente.")
    
    except mysql.connector.Error as error:
        print("Error al eliminar usuario:", error)

    finally:
        cursor.close()
        print("Cursor cerrado.")


def añadirRol():
    try:
        rol = input("Ingresa el nombre del nuevo rol: ")
        cursor = conexion.cursor()
        sentencia = f"CREATE ROLE '{rol}'"
        cursor.execute(sentencia)

        conexion.commit()
        print("Rol creado correctamente.")
    
    except mysql.connector.Error as error:
        print("Error al crear rol:", error)

    finally:
        cursor.close()
        print("Cursor cerrado.")
        
        
def asignarRol():
    try:
        rol = input("Ingresa el nombre del rol: ")
        usuario = input("Ingresa el nombre del usuario: ")
        cursor = conexion.cursor()
        sentencia = f"GRANT '{rol}' TO '{usuario}'@localhost"
        cursor.execute(sentencia)

        conexion.commit()
        print("Rol asignado correctamente.")
    
    except mysql.connector.Error as error:
        print("Error al asignar rol:", error)

    finally:
        cursor.close()
        print("Cursor cerrado.")
        





def obtenerUsuarios():
    try:
        cursor = conexion.cursor()
        sentencia = f"SELECT User FROM mysql.user WHERE account_locked = 'N';"
        cursor.execute(sentencia)
        resultados = cursor.fetchall()

        for fila in resultados:
            print(fila)
        print("Presione enter para continuar")
        input()

    
    except mysql.connector.Error as error:
        print("Error al mostrar usuarios:", error)

    finally:
        cursor.close()
        print("Cursor cerrado.")



def obtenerRoles():
    try:
        cursor = conexion.cursor()
        sentencia = f"""SELECT User
                    FROM mysql.user
                    WHERE account_locked = 'Y'
                    AND User NOT IN ('mysql.infoschema', 'mysql.session', 'mysql.sys');"""

        cursor.execute(sentencia)
        resultados = cursor.fetchall()

        for fila in resultados:
            print(fila)
        print("Presione enter para continuar")
        input()
    
    except mysql.connector.Error as error:
        print("Error al obtener roles:", error)

    finally:
        cursor.close()
        print("Cursor cerrado.")


def procedimientosAlmacenados():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='biblioteca_db'
    )
    try:
        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES FROM biblioteca_db")
        tablas = cursor.fetchall()

        with open('crudProcedimientos.sql', 'w') as archivo:
            archivo.write(f"DELIMITER $$\n\n")
            
            for tabla in tablas:
                nombre_tabla = tabla[0]
                cursor.execute(f"DESCRIBE {nombre_tabla}")
                columnas = cursor.fetchall()
                
                primary_key = None
                columnas_nombres = []
                columnas_parametros = []
                columnas_update = []
                
                for columna in columnas:
                    col_name = columna[0]
                    col_type = columna[1]
                    if columna[3] == 'PRI' and columna[5] == 'auto_increment':
                        primary_key = col_name
                    else:
                        columnas_nombres.append(col_name)
                        columnas_parametros.append(f"IN p_{col_name} {col_type}")
                        columnas_update.append(f"{col_name} = p_{col_name}")

                columnas_insert = ", ".join(columnas_nombres)
                columnas_parametros = ", ".join(columnas_parametros)
                
                archivo.write(f"CREATE PROCEDURE Insertar_{nombre_tabla} ({columnas_parametros}) \n")
                archivo.write(f"BEGIN\n")
                archivo.write(f"    INSERT INTO {nombre_tabla} ({columnas_insert}) VALUES ({', '.join([f'p_{col}' for col in columnas_nombres])});\n")
                archivo.write(f"END $$\n\n")
                
                if primary_key:
                    archivo.write(f"CREATE PROCEDURE Actualizar_{nombre_tabla} (IN p_{primary_key} {columnas[0][1]}, {columnas_parametros}) \n")
                    archivo.write(f"BEGIN\n")
                    archivo.write(f"    UPDATE {nombre_tabla} SET {', '.join(columnas_update)} WHERE {primary_key} = p_{primary_key};\n")
                    archivo.write(f"END $$\n\n")
                
                if primary_key:
                    archivo.write(f"CREATE PROCEDURE Eliminar_{nombre_tabla} (IN p_{primary_key} {columnas[0][1]}) \n")
                    archivo.write(f"BEGIN\n")
                    archivo.write(f"    DELETE FROM {nombre_tabla} WHERE {primary_key} = p_{primary_key};\n")
                    archivo.write(f"END $$\n\n")
                
                archivo.write(f"CREATE PROCEDURE ObtenerTodos_{nombre_tabla} () \n")
                archivo.write(f"BEGIN\n")
                archivo.write(f"    SELECT * FROM {nombre_tabla};\n")
                archivo.write(f"END $$\n\n")
            
            archivo.write(f"DELIMITER ;\n")
    
        print("Scripts de procedimientos almacenados generados correctamente.")
    
    except mysql.connector.Error as error:
        print("Error al generar script: ", error)

    finally:
        cursor.close()
        print("Cursor cerrado.")
        print("Presione enter para regresar al menú..")
        input()


def cerrarMenu():
    print(conexion.is_connected())
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada.")
    else: 
        print("Saliendo del gestor.")