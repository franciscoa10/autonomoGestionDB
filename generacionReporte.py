import mysql.connector
from fpdf import FPDF

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)

def run(): 
    try: 
        cursor = conexion.cursor()
        consulta = f"""SELECT table_name 
                        FROM information_schema.tables 
                        WHERE table_schema='biblioteca_db' 
                        AND table_type='BASE TABLE'; """
                    
        cursor.execute(consulta)
        
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
        table = input("Ingresa la entidad con la quiere generar un reporte: ")
        atributos(table)
    except mysql.connector.Error as error:
        print("Error al listar entidades:", error)

def atributos(table):
    try: 
        cursor = conexion.cursor()
        consulta = f"""SELECT column_name                  
                        FROM information_schema.columns     
                        WHERE table_schema = 'biblioteca_db'       
                        AND table_name   = '{table}'"""
        
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
        reporte(table)

    except mysql.connector.Error as error:
        print("Error al listar atributos:", error)            

def reporte(table):
    try: 
        cursor = conexion.cursor()
        columnas = input('Ingrese las columnas con las que quiere generar un reporte(separe los atributos con una ","): ')

        consulta = f"""SELECT {columnas}
                        FROM biblioteca_db.{table}"""
        cursor.execute(consulta)
        
        resultados = cursor.fetchall()
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        reporteNombre = input("Ingrese el nombre de su reporte: ")

        pdf.cell(180, 10, txt="Reporte", border=1, ln=True, align='C')
        header = columnas.split(',')
        for col in header:
            pdf.cell(40, 10, col, border=1)
        pdf.ln()


        for fila in resultados:
            for dato in fila:
                pdf.cell(40, 10, str(dato), border=1)
            pdf.ln()

        pdf.output(f"{reporteNombre}.pdf")
        print("Reporte generado correctamente.")
        print("Presione enter para regresar al menú..")
        input()
        
    except mysql.connector.Error as error:
        print("Error al generar reporte:", error)

    finally:
        cursor.close()
        print("Cursor cerrado.")