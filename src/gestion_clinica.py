#Excepciones personalizadas para el sistema de gestión de clínicas
class PacienteYaRegistradoException(Exception):
    """Se lanza cuando se intenta registrar un paciente que ya existe."""
    pass

class PacienteNoEncontradoException(Exception):
    """Se lanza cuando no se encuentra un paciente buscado."""
    pass

class DniInvalidoException(Exception):
    """Se lanza cuando el DNI del paciente no es válido."""
    pass

class FechaNacimientoInvalidaException(Exception):
    """Se lanza cuando la fecha de nacimiento del paciente no es válida."""
    pass

class NombrePacienteInvalidoException(Exception):
    """Se lanza cuando el nombre del paciente no es válido."""
    pass

class EspecialidadYaRegistradaException(Exception):
    """Se lanza cuando se intenta registrar una especialidad que ya existe."""
    pass

class EspecialidadNoEncontradaException(Exception):
    """Se lanza cuando no se encuentra la especialidad buscada."""
    pass

class TipoEspecialidadInvalidoException(Exception):
    """Se lanza cuando el tipo de especialidad es inválido."""
    pass

class DiasEspecialidadInvalidosException(Exception):
    """Se lanza cuando los días de atención de la especialidad son inválidos."""
    pass

class MedicoYaRegistradoException(Exception):
    """Se lanza cuando se intenta registrar un médico que ya existe."""
    pass

class MedicoNoEncontradoException(Exception):
    """Se lanza cuando no se encuentra un médico buscado."""
    pass

class MatriculaInvalidaException(Exception):
    """Se lanza cuando la matrícula del médico no es válida."""
    pass

class NombreMedicoInvalidoException(Exception):
    """Se lanza cuando el nombre del médico no es válido."""
    pass

class EspecialidadInvalidaException(Exception):
    """Se lanza cuando la especialidad del médico no es válida."""
    pass
class MedicoNoDisponibleException(Exception):
    """Se lanza cuando se intenta acceder a un médico que no está disponible."""
    pass

class TurnoOcupadoException(Exception):
    """Se lanza cuando el turno solicitado ya está ocupado por otro paciente o médico."""
    pass

class TurnoNoEncontradoException(Exception):
    """Se lanza cuando no se encuentra el turno buscado."""
    pass

class FechaTurnoInvalidaException(Exception):
    """Se lanza cuando la fecha del turno no es válida."""
    pass

class HoraTurnoInvalidaException(Exception):
    """Se lanza cuando la hora del turno no es válida."""
    pass

class EspecialidadTurnoInvalidaException(Exception):
    """Se lanza cuando la especialidad del turno no es válida."""
    pass

class RecetaInvalidaException(Exception):
    """Se lanza cuando la receta es inválida (por ejemplo, sin medicamentos o con datos incorrectos)."""
    pass

class RecetaYaEmitidaException(Exception):
    """Se lanza cuando se intenta emitir una receta que ya existe para ese paciente, médico y fecha."""
    pass

class RecetaNoEncontradaException(Exception):
    """Se lanza cuando no se encuentra una receta buscada."""
    pass

class MedicamentoInvalidoException(Exception):
    """Se lanza cuando algún medicamento de la receta no es válido."""
    pass

class HistoriaClinicaNoEncontradaException(Exception):
    """Se lanza cuando no se encuentra la historia clínica del paciente."""
    pass

class HistoriaClinicaYaExisteException(Exception):
    """Se lanza cuando se intenta crear una historia clínica que ya existe para el paciente."""
    pass

class HistoriaClinicaInvalidaException(Exception):
    """Se lanza cuando los datos de la historia clínica son inválidos."""
    pass

class ClinicaNoEncontradaException(Exception):
    """Se lanza cuando no se encuentra la clínica solicitada."""
    pass

class ClinicaYaRegistradaException(Exception):
    """Se lanza cuando se intenta registrar una clínica que ya existe."""
    pass

class DatosClinicaInvalidosException(Exception):
    """Se lanza cuando los datos de la clínica son inválidos."""
    pass

class OpcionMenuInvalidaException(Exception):
    """Se lanza cuando el usuario ingresa una opción de menú no válida."""
    pass

class EntradaUsuarioInvalidaException(Exception):
    """Se lanza cuando la entrada del usuario no es válida o tiene caracteres no permitidos."""
    pass

class SalidaAnticipadaException(Exception):
    """Se lanza cuando el usuario decide salir del sistema de forma inesperada."""
    pass

# Clases del sistema de gestión de clínicas

class Paciente:
    def __init__ (self, nombre, dni, fecha_nacimiento):
        self.__nombre_paciente__ = nombre
        self.__dni__ = dni
        self.__fecha_nacimiento__ = fecha_nacimiento

    def obtener_dni(self):
        return self.__dni__

    def __str__(self):
        return f"Nombre: {self.__nombre_paciente__}, DNI: {self.__dni__}, Fecha de Nacimiento: {self.__fecha_nacimiento__}"
    
class Especialidad:
    def __init__ (self, tipo, dias):
        self.__tipo__ = tipo
        self.__dias__ = dias

    def obtener_especialidad(self):
        return self.__tipo__

    def verificar_dia(self, dia_a_verificar):
        return dia_a_verificar in self.__dias__

    def __str__(self):
        return f"Especialidad: {self.__tipo__}, Dias: {', '.join(self.__dias__)}"

class Medico:
    def __init__ (self, nombre, matricula, especialidad):
        self.__nombre__ = nombre
        self.__matricula__ = matricula
        self.__especialidad__ = especialidad

    def obtener_matricula(self):
        return self.__matricula__

    def obtener_especialidad_para_dia(self):
        return self.__especialidad__

    def __str__(self):
        return f"Nombre: {self.__nombre__}, Matricula: {self.__matricula__}, Especialidad: {self.__especialidad__.__tipo__}, Dias: {', '.join(self.__especialidad__.__dias__)}"  
    
class Turno:
    def __init__ (self, paciente, medico, fecha, hora, especialidad):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha__ = fecha
        self.__hora__ = hora
        self.__especialidad__ = especialidad

    def obtener_medico(self):
        return self.__medico__

    def obtener_fecha_hora(self):
        return self.__fecha__, self.__hora__

    def __str__(self):
        return f"Paciente: {self.__paciente__.__nombre_paciente__}, Medico: {self.__medico__.__nombre__}, Fecha: {self.__fecha__}, Hora: {self.__hora__}, Especialidad: {self.__especialidad__.__tipo__}"
    
class Receta:
    def __init__(self, paciente, medico, medicamentos, fecha):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self.__fecha__ = fecha

    def obtener_paciente(self):
        return self.__paciente__

    def obtener_medico(self):
        return self.__medico__

    def obtener_medicamentos(self):
        return self.__medicamentos__

    def obtener_fecha(self):
        return self.__fecha__

    def __str__(self):
        return (
            f"Paciente: {self.__paciente__.__nombre_paciente__}, "
            f"Médico: {self.__medico__.__nombre__}, "
            f"Medicamentos: {', '.join(str(m) for m in self.__medicamentos__)}, "
            f"Fecha: {self.__fecha__}"
        )
    
class HistoriaClinica:
    def __init__(self, paciente, turnos=None, recetas=None):
        self.__paciente__ = paciente
        self.__turnos__ = turnos if turnos is not None else []
        self.__recetas__ = recetas if recetas is not None else []

    def agregar_turno(self, turno):
        self.__turnos__.append(turno)

    def agregar_receta(self, receta):
        self.__recetas__.append(receta)

    def obtener_turnos(self):
        return self.__turnos__

    def obtener_receta(self):
        return self.__recetas__

    def __str__(self):
        return f"Historia Clínica de {self.__paciente__.__nombre_paciente__} (DNI: {self.__paciente__.__dni__})"
    
# Clase Clinica para gestionar pacientes, médicos, turnos y recetas

class Clinica:
    def __init__ (self, pacientes, medicos, turnos, historias_clinicas):
        self.__pacientes__ = pacientes
        self.__medicos__ = medicos
        self.__turnos__ = turnos
        self.__historias_clinicas__ = historias_clinicas


    def agregar_paciente(self, paciente_nuevo):
        if any(paciente_actual.__dni__ == paciente_nuevo.__dni__ for paciente_actual in self.__pacientes__):
            raise PacienteYaRegistradoException("El paciente ya está registrado.")
        self.__pacientes__.append(paciente_nuevo)

    def agregar_medico(self, medico_nuevo):
        if any(medico_actual.__matricula__ == medico_nuevo.__matricula__ for medico_actual in self.__medicos__):
            raise MedicoYaRegistradoException("El médico ya está registrado.")
        self.__medicos__.append(medico_nuevo)

    def obtener_pacientes(self):
        return self.__pacientes__

    def obtener_medicos(self):
        return self.__medicos__

    def obtener_medico_por_matricula(self, matricula):
        return next((medico_actual for medico_actual in self.__medicos__ if medico_actual.__matricula__ == matricula), None)

    def agendar_turno(self, dni_paciente, matricula_medico, fecha, hora, especialidad):
        paciente_encontrado = next((paciente_actual for paciente_actual in self.__pacientes__ if paciente_actual.__dni__ == dni_paciente), None)
        medico_encontrado = next((medico_actual for medico_actual in self.__medicos__ if medico_actual.__matricula__ == matricula_medico), None)
        if not paciente_encontrado and not medico_encontrado:
            raise PacienteNoEncontradoException("Paciente y médico no encontrados")
        elif not paciente_encontrado:
            raise PacienteNoEncontradoException("Paciente no encontrado")
        elif not medico_encontrado:
            raise MedicoNoEncontradoException("Médico no encontrado")
        for turno_existente in self.__turnos__:
            if (turno_existente.__medico__.__matricula__ == matricula_medico and
                turno_existente.__fecha__ == fecha and
                turno_existente.__hora__ == hora):
                raise TurnoOcupadoException("El médico ya tiene un turno en ese horario.")
        turno_nuevo = Turno(paciente_encontrado, medico_encontrado, fecha, hora, especialidad)
        self.__turnos__.append(turno_nuevo)
        historia = self.obtener_historia_clinica(dni_paciente)
        if historia:
            historia.agregar_turno(turno_nuevo)
        return turno_nuevo

    def obtener_turnos(self):
        return self.__turnos__

    def emitir_receta(self, dni_paciente, matricula_medico, medicamentos, fecha):
        paciente_encontrado = next((paciente_actual for paciente_actual in self.__pacientes__ if paciente_actual.__dni__ == dni_paciente), None)
        medico_encontrado = next((medico_actual for medico_actual in self.__medicos__ if medico_actual.__matricula__ == matricula_medico), None)
        if not paciente_encontrado:
            raise PacienteNoEncontradoException("Paciente no encontrado")
        if not medico_encontrado:
            raise MedicoNoEncontradoException("Médico no encontrado")
        if not medicamentos or not isinstance(medicamentos, list) or not all(medicamento.strip() for medicamento in medicamentos):
            raise RecetaInvalidaException("La receta debe contener al menos un medicamento válido.")
        receta_nueva = Receta(paciente_encontrado, medico_encontrado, medicamentos, fecha)
        if hasattr(self, '__recetas__'):
            self.__recetas__.append(receta_nueva)
        historia_clinica_encontrada = self.obtener_historia_clinica(dni_paciente)
        if historia_clinica_encontrada:
            historia_clinica_encontrada.agregar_receta(receta_nueva)
            return receta_nueva
        else:
            raise PacienteNoEncontradoException("Historia clínica no encontrada para el paciente.")

    def obtener_historia_clinica(self, dni_paciente):
        return next((historia_clinica_actual for historia_clinica_actual in self.__historias_clinicas__ if historia_clinica_actual.__paciente__.__dni__ == dni_paciente), None)
    
# Clase Clinica_Cli para interactuar con el usuario

class Clinica_Cli:
    def __init__(self, pacientes=None, medicos=None, turnos=None, historias_clinicas=None):
        if pacientes is None:
            pacientes = []
        if medicos is None:
            medicos = []
        if turnos is None:
            turnos = []
        if historias_clinicas is None:
            historias_clinicas = []
        self.clinica = Clinica(pacientes, medicos, turnos, historias_clinicas)

    def ejecutar(self):
        while True:
            print("Menu:")
            print("1. Agregar Paciente")
            print("2. Agregar Medico")
            print("3. Agendar Turno")
            print("4. Emitir Receta")
            print("5. Ver Pacientes")
            print("6. Ver Medicos")
            print("7. Ver Turnos")
            print("8. Ver Historia Clinica")
            print("9. Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del paciente: ")
                dni = input("Ingrese el DNI del paciente: ")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (DD/MM/AAAA): ").strip()
                try:
                    if not dni.isdigit():
                        raise DniInvalidoException("El DNI debe ser numérico.")
                    if not nombre or nombre.isspace():
                        raise NombrePacienteInvalidoException("El nombre no puede estar vacío.")
                    # Aquí podrías agregar más validaciones de fecha si lo deseas
                    nuevo_paciente = Paciente(nombre, dni, fecha_nacimiento)
                    self.clinica.agregar_paciente(nuevo_paciente)
                    nueva_historia = HistoriaClinica(nuevo_paciente, [], [])
                    self.clinica.__historias_clinicas__.append(nueva_historia)
                    print("Paciente agregado correctamente.")
                except PacienteYaRegistradoException as e:
                    print(str(e))
                except DniInvalidoException as e:
                    print(str(e))
                except NombrePacienteInvalidoException as e:
                    print(str(e))
                except Exception as e:
                    print("Error inesperado:", str(e))
            elif opcion == "2":
                nombre = input("Ingrese el nombre del médico: ")
                matricula = input("Ingrese la matrícula del médico: ")
                tipo_especialidad = input("Ingrese la especialidad del médico: ")
                dias_disponibles = input("Ingrese los días disponibles del médico (separados por comas): ").strip().split(',')
                try:
                    if not matricula:
                        raise MatriculaInvalidaException("La matrícula no puede estar vacía.")
                    if not nombre or nombre.isspace():
                        raise NombreMedicoInvalidoException("El nombre no puede estar vacío.")
                    if not tipo_especialidad or tipo_especialidad.isspace():
                        raise EspecialidadInvalidaException("La especialidad no puede estar vacía.")
                    esp = Especialidad(tipo_especialidad, dias_disponibles)
                    nuevo_medico = Medico(nombre, matricula, esp)
                    self.clinica.agregar_medico(nuevo_medico)
                    print("Médico agregado correctamente.")
                except MedicoYaRegistradoException as e:
                    print(str(e))
                except MatriculaInvalidaException as e:
                    print(str(e))
                except NombreMedicoInvalidoException as e:
                    print(str(e))
                except EspecialidadInvalidaException as e:
                    print(str(e))
                except Exception as e:
                    print("Error inesperado:", str(e))
            elif opcion == "3":
                dni_paciente = input("Ingrese el DNI del paciente: ")
                matricula_medico = input("Ingrese la matrícula del médico: ")
                fecha = input("Ingrese la fecha del turno (DD/MM/AAAA): ").strip()
                hora = input("Ingrese la hora del turno (HH:MM): ").strip()
                tipo_especialidad = input("Ingrese la especialidad del turno: ").strip()
                esp = Especialidad(tipo_especialidad, [])
                try:
                    self.clinica.agendar_turno(dni_paciente, matricula_medico, fecha, hora, especialidad=esp)
                    print("Turno agendado correctamente.")
                except PacienteNoEncontradoException as e:
                    print(str(e))
                except MedicoNoEncontradoException as e:
                    print(str(e))
                except TurnoOcupadoException as e:
                    print(str(e))
                except Exception as e:
                    print("Error inesperado:", str(e))
            elif opcion == "4":
                dni_paciente = input("Ingrese el DNI del paciente: ")
                matricula_medico = input("Ingrese la matrícula del médico: ")
                medicamentos = input("Ingrese los medicamentos (separados por comas): ").strip().split(',')
                fecha = input("Ingrese la fecha de emisión de la receta (DD/MM/AAAA): ").strip()
                try:
                    self.clinica.emitir_receta(dni_paciente, matricula_medico, medicamentos, fecha)
                    print("Receta emitida correctamente.")
                except PacienteNoEncontradoException as e:
                    print(str(e))
                except MedicoNoEncontradoException as e:
                    print(str(e))
                except RecetaInvalidaException as e:
                    print(str(e))
                except HistoriaClinicaNoEncontradaException as e:
                    print(str(e))
                except Exception as e:
                    print("Error inesperado:", str(e))
            elif opcion == "5":
                for paciente_existente in self.clinica.obtener_pacientes():
                    print(f"Nombre: {paciente_existente.__nombre_paciente__}, DNI: {paciente_existente.__dni__}, Fecha de Nacimiento: {paciente_existente.__fecha_nacimiento__}")
            elif opcion == "6":
                for medico_existente in self.clinica.obtener_medicos():
                    print(f"Nombre: {medico_existente.__nombre__}, Matrícula: {medico_existente.__matricula__}, Especialidad: {medico_existente.__especialidad__.__tipo__}, Días Disponibles: {', '.join(medico_existente.__especialidad__.__dias__)}")
            elif opcion == "7":
                for turno_existente in self.clinica.obtener_turnos():
                    print(f"Paciente: {turno_existente.__paciente__.__nombre_paciente__}, Médico: {turno_existente.__medico__.__nombre__}, Fecha: {turno_existente.__fecha__}, Hora: {turno_existente.__hora__}, Especialidad: {turno_existente.__especialidad__.__tipo__}")
            elif opcion == "8":
                dni_paciente = input("Ingrese el DNI del paciente: ")
                historia = self.clinica.obtener_historia_clinica(dni_paciente)
                if historia:
                    print(f"Historia Clínica de {historia.__paciente__.__nombre_paciente__} (DNI: {historia.__paciente__.__dni__})")
                    print("Turnos:")
                    for turno_existente in historia.obtener_turnos():
                        print(f"- {turno_existente.__fecha__} a las {turno_existente.__hora__} con Dr. {turno_existente.__medico__.__nombre__}")
                    print("Recetas:")
                    for receta_existente in historia.obtener_receta():
                        print(f"- {receta_existente.__fecha__}: {', '.join(receta_existente.__medicamentos__)}")
                else:
                    print("Historia clínica no encontrada.")
            elif opcion == "9":
                print("Gracias por usar el sistema de gestión clínica. ¡Hasta luego!")
                break
            else:
                print("Opción no válida, intente nuevamente.")

if __name__ == '__main__':
    cli = Clinica_Cli()
    cli.ejecutar()