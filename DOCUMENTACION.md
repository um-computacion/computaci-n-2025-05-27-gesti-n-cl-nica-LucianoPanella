# Documentación de Uso del Sistema de Gestión Clinica
# Descripción General
    El sistema fue desarrolado en Python, y este mismo permite gestionar de forma basica y eficiente una clínica medica. Se utiliza una interfaz atravez de consola(CLI), y en esta misma se puede registras pacientes y medicos, agendar turnos, emitir recetas y ver las historias clínicas. Consta de validaciones y control de errores
# Como ejecutar el sistema
    1- Debe tener python instalado(la version 3.10 o superior)
    2- Abrir la terminal o consola en la carpeta "src" donde se encuentra el archivo de "gestion_clinica.py"
    3- Ejecularlo con la scrip: "python src/gestion_clinica.py"
    4- El sistema motrará un menu para interactuar atraves de la consola
# Menu Principal del Sistema de Gestión Clinica
    Menu:
        1-Agregar Paciente
        2-Agregar Medico
        3-Agendar Turno
        4-Emitir Receta
        5-Ver Pacientes
        6-Ver Medicos
        7-Ver Turnos
        8-Ver Historia Clinica
        9-Salir
# Estructura del Sistema
    # Clases Principales
        - Paciente: Se utiliza para obtener informacion del paciente. Utilizando los  atributos nombre, dni y fecha_nacimiento

        - Medico:Se utiliza para obtener informacion del medico. Utilizando los atributos nombre, matricula y especialidad 

        - Especialidad:Se utiliza para obtener informacion de la especialidad. Utilizando los  atributos tipo y dias_atencion

        - Turno:Se utiliza para obtener informacion del turno. Utilizando los  atributos paciente, medico, fecha, hora y especialidad

        - Receta:Se utiliza para obtener informacion de la receta. Utilizando los  atributos paciente, medico, medicamentos y fecha

        - HistoriaClinica:Se utiliza para obtener informacion del paciente. Utilizando los  atributos paciente, lista_de_turnos y lista_de_recestas

        - Clinica: Se utiliza como "Clase Principal" Ya que sirve para gestionar pacientes, medicos, turnos y recetas. Proporcionando los metodos para agregar pacientes y medicos, agendar turnos, emitir recetas y mostrar las historias clinicas. Utilizando los  atributos listas_de_pacientes, medicos, turnos e historias_clinicas

        - Clinica_Cli: Es la clase, que se utiliza para por ejecutar la interfaz de la Clinica
# Validaciones y Errores
    Todas las validaciones importantes (DNI, matricula, fechas, especialidades, duplicados) estan implementadas dentro de las clases de modelo. Y tambien se utilizan excepciones personalizadas como:
        - PacienteYaRegistradoException
        - TurnoOcupadoException
        - RecetaInvalidaException
        - MedicoNoEncontradoException
        - etc
    Las excepciones son captudaras y transformadas en mensajes claros para el usuario
# Como ejecitar los Test del sistema
    1- Debe tener python instalado(la version 3.10 o superior)
    2- Abrir la terminal o consola en la carpeta "Test" donde se encuentran los distintos archivos con los test, para cada clase
    3- Ejecularlo con la scrip: "python -m unittest discover -s Test" Ejecutara todos los test de manera automatica
    4- Por consola o terminal deberia de figurar
     "Ran 135 tests in 0.029s"
     "OK"
    5- Si desea ejecutar un test en particular, es atraves del siguien comando: "python -m unittest Test/(nombre del archivo.py)
        Ej: "python -m unittest Test/test_cli.py"  
# Cobertura de los Test del sistema
    - test_paciente.py: Prueba la clase Paciente.
    - test_especialidad.py: Prueba la clase Especialidad.
    - test_medico.py: Prueba la clase Medico.
    - test_turno.py: Prueba la clase Turno.
    - test_receta.py: Prueba la clase Receta.
    - test_historiaclinica.py: Prueba la clase HistoriaClinica.
    - test_clinica.py: Prueba la lógica de la clase Clinica
    - test_cli.py: Prueba la interfaz de consola usando mocks.

    El sistema tiene test unitarios que cubren casos correctos e incorrectos de las clases, asegurando la covertura de funcional del sistema 

# Comentario
    Las  Clases y Excepciones estan junto al CLI en el mismo archivo de "gestion_clinica.py". Debido a que cuando intente ejecutar los test, fallaban siempre tirando el error de "ModuleNotFoundError: No module named" ya que cuando se realizaba el "From (Nombre_Archivo) import (Clase a llamar) figuraba que no existia.
    Corroboré mayusculas y minusculas, borre archivos y cambie nombres. No termine de entender el porque no me permitia los import 
# Archivo de gestion_clinica.py
    En la primera parte se encuentran todas las excepciones, luego les siguen las clases y para finalizar se encuentra la ultima clase del CLI. Donde se ejecuta la interfaz