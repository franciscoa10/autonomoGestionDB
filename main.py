import tareas
import backup
import generacionReporte

def menu_gestor():
    print("\nMenú de opciones")
    print("1. Añadir usuario")
    print("2. Actualizar usuario")
    print("3. Eliminar usuario")
    print("4. Añadir rol")
    print("5. Asignar rol a usuario")
    print("6. Obtener usuarios")
    print("7. Obetener roles")
    print("8. Respaldar base de datos")
    print("9. Restaurar base de datos")
    print("10. Generar reporte")
    print("11. Generar procedimientos almacenados")
    print("12. Salir")

def main():
    while True:
        menu_gestor()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            tareas.añadirUsuario()
        elif opcion == '2':
            tareas.actualizarUsuario()
        elif opcion == '3':
            tareas.eliminarUsuario()
        elif opcion == '4':
            tareas.añadirRol()
        elif opcion == '5':
            tareas.asignarRol()
        elif opcion == '6':
            tareas.obtenerUsuarios()
        elif opcion == '7':
            tareas.obtenerRoles()
        elif opcion == '8':
            backup.respaldo()
        elif opcion == '9':
            backup.restaurar()
        elif opcion == '10':
            generacionReporte.run()
        elif opcion == '11':
            tareas.procedimientosAlmacenados()
        elif opcion == '12':
            tareas.cerrarMenu()
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
