import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.gestion_clinica import Paciente, Especialidad, Medico, Receta, Turno, HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.pac = Paciente("Juan Perez", "12345678", "01/01/2000")
        self.esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.med = Medico("Dra. Lopez", "M123", self.esp)
        self.turno1 = Turno(self.pac, self.med, "10/06/2025", "10:00", self.esp)
        self.turno2 = Turno(self.pac, self.med, "11/06/2025", "11:00", self.esp)
        self.receta1 = Receta(self.pac, self.med, ["Ibuprofeno"], "10/06/2025")
        self.receta2 = Receta(self.pac, self.med, ["Paracetamol"], "11/06/2025")
        self.hist = HistoriaClinica(self.pac)

    def test_atributo_paciente(self):
        self.assertEqual(self.hist.__paciente__, self.pac)

    def test_turnos_inicial_vacio(self):
        self.assertEqual(self.hist.obtener_turnos(), [])

    def test_recetas_inicial_vacio(self):
        self.assertEqual(self.hist.obtener_receta(), [])

    def test_agregar_turno(self):
        self.hist.agregar_turno(self.turno1)
        self.assertIn(self.turno1, self.hist.obtener_turnos())

    def test_agregar_varios_turnos(self):
        self.hist.agregar_turno(self.turno1)
        self.hist.agregar_turno(self.turno2)
        self.assertIn(self.turno1, self.hist.obtener_turnos())
        self.assertIn(self.turno2, self.hist.obtener_turnos())
        self.assertEqual(len(self.hist.obtener_turnos()), 2)

    def test_agregar_receta(self):
        self.hist.agregar_receta(self.receta1)
        self.assertIn(self.receta1, self.hist.obtener_receta())

    def test_agregar_varias_recetas(self):
        self.hist.agregar_receta(self.receta1)
        self.hist.agregar_receta(self.receta2)
        self.assertIn(self.receta1, self.hist.obtener_receta())
        self.assertIn(self.receta2, self.hist.obtener_receta())
        self.assertEqual(len(self.hist.obtener_receta()), 2)

    def test_str(self):
        esperado = "Historia Clínica de Juan Perez (DNI: 12345678)"
        self.assertEqual(str(self.hist), esperado)

    def test_turnos_y_recetas_separados(self):
        self.hist.agregar_turno(self.turno1)
        self.hist.agregar_receta(self.receta1)
        self.assertIn(self.turno1, self.hist.obtener_turnos())
        self.assertIn(self.receta1, self.hist.obtener_receta())
        self.assertNotIn(self.receta1, self.hist.obtener_turnos())
        self.assertNotIn(self.turno1, self.hist.obtener_receta())

    def test_inicializacion_con_listas(self):
        hist2 =HistoriaClinica(self.pac, [self.turno1], [self.receta1])
        self.assertIn(self.turno1, hist2.obtener_turnos())
        self.assertIn(self.receta1, hist2.obtener_receta())

    def test_agregar_turno_objeto_distinto(self):
        otro_pac = Paciente("Ana Torres", "87654321", "02/02/1990")
        otro_esp = Especialidad("Clínica", ["martes"])
        otro_med = Medico("Dr. House", "M999", otro_esp)
        otro_turno = Turno(otro_pac, otro_med, "12/06/2025", "12:00", otro_esp)
        self.hist.agregar_turno(otro_turno)
        self.assertIn(otro_turno, self.hist.obtener_turnos())

    def test_agregar_receta_objeto_distinto(self):
        otro_pac = Paciente("Ana Torres", "87654321", "02/02/1990")
        otro_esp = Especialidad("Clínica", ["martes"])
        otro_med = Medico("Dr. House", "M999", otro_esp)
        otra_receta = Receta(otro_pac, otro_med, ["Amoxicilina"], "12/06/2025")
        self.hist.agregar_receta(otra_receta)
        self.assertIn(otra_receta, self.hist.obtener_receta())

    def test_modificar_turnos(self):
        self.hist.__turnos__ = [self.turno1]
        self.assertIn(self.turno1, self.hist.obtener_turnos())

    def test_modificar_recetas(self):
        self.hist.__recetas__ = [self.receta1]
        self.assertIn(self.receta1, self.hist.obtener_receta())

    def test_turnos_y_recetas_independientes(self):
        self.hist.agregar_turno(self.turno1)
        self.hist.agregar_receta(self.receta1)
        self.hist.agregar_turno(self.turno2)
        self.hist.agregar_receta(self.receta2)
        self.assertEqual(self.hist.obtener_turnos(), [self.turno1, self.turno2])
        self.assertEqual(self.hist.obtener_receta(), [self.receta1, self.receta2])

if __name__ == '__main__':
    unittest.main()