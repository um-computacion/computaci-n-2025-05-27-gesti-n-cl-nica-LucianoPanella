import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.gestion_clinica import Paciente, Especialidad, Medico, Turno

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.pac = Paciente("Juan Perez", "12345678", "01/01/2000")
        self.esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.med = Medico("Dra. Lopez", "M123", self.esp)
        self.turno = Turno(self.pac, self.med, "10/06/2025", "10:00", self.esp)

    def test_atributo_paciente(self):
        self.assertEqual(self.turno.__paciente__, self.pac)

    def test_atributo_medico(self):
        self.assertEqual(self.turno.__medico__, self.med)

    def test_atributo_fecha(self):
        self.assertEqual(self.turno.__fecha__, "10/06/2025")

    def test_atributo_hora(self):
        self.assertEqual(self.turno.__hora__, "10:00")

    def test_atributo_especialidad(self):
        self.assertEqual(self.turno.__especialidad__, self.esp)

    def test_obtener_medico(self):
        self.assertEqual(self.turno.obtener_medico(), self.med)

    def test_obtener_fecha_hora(self):
        fecha, hora = self.turno.obtener_fecha_hora()
        self.assertEqual(fecha, "10/06/2025")
        self.assertEqual(hora, "10:00")

    def test_str(self):
        esperado = "Paciente: Juan Perez, Medico: Dra. Lopez, Fecha: 10/06/2025, Hora: 10:00, Especialidad: Cardiología"
        self.assertEqual(str(self.turno), esperado)

    def test_paciente_vacio(self):
        pac = Paciente("", "", "")
        turno_vacio = Turno(pac, self.med, "11/06/2025", "11:00", self.esp)
        self.assertEqual(turno_vacio.__paciente__.__nombre_paciente__, "")

    def test_medico_vacio(self):
        esp = Especialidad("Clínica", ["martes"])
        med = Medico("", "", esp)
        turno_vacio = Turno(self.pac, med, "12/06/2025", "12:00", esp)
        self.assertEqual(turno_vacio.__medico__.__nombre__, "")

    def test_especialidad_vacia(self):
        esp = Especialidad("", [])
        turno_vacio = Turno(self.pac, self.med, "13/06/2025", "13:00", esp)
        self.assertEqual(turno_vacio.__especialidad__.__tipo__, "")

    def test_fecha_vacia(self):
        turno_vacio = Turno(self.pac, self.med, "", "14:00", self.esp)
        self.assertEqual(turno_vacio.__fecha__, "")

    def test_hora_vacia(self):
        turno_vacio = Turno(self.pac, self.med, "14/06/2025", "", self.esp)
        self.assertEqual(turno_vacio.__hora__, "")

    def test_modificar_paciente(self):
        nuevo_pac = Paciente("Ana Torres", "87654321", "02/02/1990")
        self.turno.__paciente__ = nuevo_pac
        self.assertEqual(self.turno.__paciente__, nuevo_pac)

    def test_modificar_medico(self):
        nuevo_med = Medico("Dr. House", "M999", self.esp)
        self.turno.__medico__ = nuevo_med
        self.assertEqual(self.turno.__medico__, nuevo_med)

    def test_modificar_fecha(self):
        self.turno.__fecha__ = "20/06/2025"
        self.assertEqual(self.turno.__fecha__, "20/06/2025")

    def test_modificar_hora(self):
        self.turno.__hora__ = "15:30"
        self.assertEqual(self.turno.__hora__, "15:30")

    def test_modificar_especialidad(self):
        nueva_esp = Especialidad("Neurología", ["viernes"])
        self.turno.__especialidad__ = nueva_esp
        self.assertEqual(self.turno.__especialidad__, nueva_esp)

    def test_str_con_campos_vacios(self):
        pac = Paciente("", "", "")
        esp = Especialidad("", [])
        med = Medico("", "", esp)
        turno_vacio = Turno(pac, med, "", "", esp)
        esperado = "Paciente: , Medico: , Fecha: , Hora: , Especialidad: "
        self.assertEqual(str(turno_vacio), esperado)

if __name__ == '__main__':
    unittest.main()