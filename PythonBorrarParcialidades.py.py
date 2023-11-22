#PythonBorrarParcialidades.py

import pandas as pd
import os
import time
#*****
#***** Estructura completa
#*****
#├───ESTRUCTURA DE CARPETAS DE CADA PARCIALIDAD
#│   ├───DOCUMENTOS APROBADOS
#│   │   ├───REV LETRA
#│   │   │   ├───01 PDF
#│   │   │   └───02 EDITABLE
#│   │   └───REV NUMERO
#│   │       ├───01 PDF
#│   │       └───02 EDITABLE
#│   └───DOCUMENTOS VIGENTES
#│       ├───01 PDF
#│       │   ├───CON OBSERVACIONES
#│       │   └───SIN OBSERVACIONES
#│       └───02 EDITABLE
#│           ├───CON OBSERVACIONES
#│           └───SIN OBSERVACIONES



# Ruta base donde se deben verificar los subdirectorios
#ruta_base = 'C:\\Users\\hjorquera\\Desktop\\PLANIMETRIA\\01 PARCIALIDADES\\'
ruta_base = 'R:\\01 PARCIALIDADES\\'  

# Nombre del archivo de log
#archivo_log = 'C:\\Users\\hjorquera\\Desktop\\PLANIMETRIA\\01 PARCIALIDADES\\log_Borrar_Documentos.txt'
archivo_log = 'R:\\01 PARCIALIDADES\\0000-00 ADMINISTRACION\\LOG\\log_Borrar_Documentos.txt'

# Planilla con la lista de parcialidades
#archivo_excel = 'C:\\Users\\hjorquera\\Desktop\\PLANIMETRIA\\01 PARCIALIDADES\\Listado de Parcialidades.xlsx'
archivo_excel = 'R:\\01 PARCIALIDADES\\Listado de Parcialidades.xlsx'

# Lista de carpetas y subcarpetas
estructura = [
            'DOCUMENTOS APROBADOS\\REV LETRA\\01 PDF',
            'DOCUMENTOS APROBADOS\\REV LETRA\\02 EDITABLE',
            'DOCUMENTOS APROBADOS\\REV NUMERO\\01 PDF',
            'DOCUMENTOS APROBADOS\\REV NUMERO\\02 EDITABLE',
            'DOCUMENTOS VIGENTES\\01 PDF\\CON OBSERVACIONES',
            'DOCUMENTOS VIGENTES\\01 PDF\\SIN OBSERVACIONES',
            'DOCUMENTOS VIGENTES\\02 EDITABLE\\CON OBSERVACIONES',
            'DOCUMENTOS VIGENTES\\02 EDITABLE\\SIN OBSERVACIONES',
             ]

# Carga el archivo Excel en un DataFrame Hoja de Parcialidades.
df = pd.read_excel(archivo_excel, sheet_name='PARCIALIDADES')

# Filtra el DataFrame para considerar solo parcialidades a 'PROCESAR' igual a 'S'
df_parcialidades = df[df['PROCESAR'] == 'S']

# Abre el archivo de log en modo de escritura
with open(archivo_log, 'w') as log_file:
    # Itera a través de cada parcialidad y la procesa
    for parcialidad in df_parcialidades['PARCIALIDAD']:
        ruta_subdirectorio = os.path.join(ruta_base, parcialidad)
        log_file.write(f'Parcialidad: {parcialidad}\n')
        # Iterar a través de la estructura y crear carpetas si no existen
        for carpeta in estructura:
            ruta_carpeta = os.path.join(ruta_subdirectorio, carpeta)
            if os.path.exists(ruta_carpeta):
                for f in os.listdir(ruta_carpeta):
                    try:
                        os.remove(os.path.join(ruta_carpeta, f))
                        log_file.write(f"Borrado: '{os.path.join(ruta_carpeta, f)}'\n")
                        print(f"Los archivos de la carpeta '{ruta_carpeta}' han sido borrados.")
                    except PermissionError:
                        print(f"                                                                                                         Cuidado archivos de la carpeta '{ruta_carpeta}'")
                        print(f"                                                                                                         El archivo {f} está en uso y no se pudo borrar.")
                    #time.sleep(1)  # Puedes agregar un retraso para evitar borrar demasiado rápido
                log_file.write(f"Los archivos de la carpeta '{ruta_carpeta}' han sido borrados.\n")
            else:
                log_file.write(f"No existe la carpeta '{ruta_carpeta}'\n")

print("Proceso finalizado. Los resultados se han guardado en el archivo de log.")





