import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.gestion_clinica import Especialidad

class TestEspecialidad(unittest.TestCase):
    def setUp(self):
        self.esp = Especialidad("Cardiología", ["lunes", "miércoles", "viernes"])

    def test_atributo_tipo(self):
        self.assertEqual(self.esp.__tipo__, "Cardiología")

    def test_atributo_dias(self):
        self.assertEqual(self.esp.__dias__, ["lunes", "miércoles", "viernes"])

    def test_obtener_especialidad(self):
        self.assertEqual(self.esp.obtener_especialidad(), "Cardiología")

    def test_verificar_dia_true(self):
        self.assertTrue(self.esp.verificar_dia("lunes"))
        self.assertTrue(self.esp.verificar_dia("miércoles"))
        self.assertTrue(self.esp.verificar_dia("viernes"))

    def test_verificar_dia_false(self):
        self.assertFalse(self.esp.verificar_dia("martes"))
        self.assertFalse(self.esp.verificar_dia("jueves"))
        self.assertFalse(self.esp.verificar_dia("domingo"))

    def test_str(self):
        esperado = "Especialidad: Cardiología, Dias: lunes, miércoles, viernes"
        self.assertEqual(str(self.esp), esperado)

    def test_tipo_vacio(self):
        esp = Especialidad("", ["lunes"])
        self.assertEqual(esp.obtener_especialidad(), "")

    def test_dias_vacio(self):
        esp = Especialidad("Dermatología", [])
        self.assertEqual(esp.__dias__, [])
        self.assertFalse(esp.verificar_dia("lunes"))
        self.assertEqual(str(esp), "Especialidad: Dermatología, Dias: ")

    def test_tipo_numerico(self):
        esp = Especialidad(123, ["lunes"])
        self.assertEqual(esp.obtener_especialidad(), 123)

    def test_dias_con_repetidos(self):
        esp = Especialidad("Pediatría", ["lunes", "lunes", "martes"])
        self.assertTrue(esp.verificar_dia("lunes"))
        self.assertTrue(esp.verificar_dia("martes"))
        self.assertFalse(esp.verificar_dia("miércoles"))

    def test_dias_con_mayusculas(self):
        esp = Especialidad("Traumatología", ["Lunes", "Miércoles"])
        self.assertFalse(esp.verificar_dia("lunes"))  # Sensible a mayúsculas/minúsculas
        self.assertTrue(esp.verificar_dia("Lunes"))

    def test_str_con_un_dia(self):
        esp = Especialidad("Oftalmología", ["jueves"])
        self.assertEqual(str(esp), "Especialidad: Oftalmología, Dias: jueves")

    def test_str_con_dias_vacios(self):
        esp = Especialidad("Neurología", [])
        self.assertEqual(str(esp), "Especialidad: Neurología, Dias: ")

    def test_modificar_tipo(self):
        self.esp.__tipo__ = "Clínica"
        self.assertEqual(self.esp.obtener_especialidad(), "Clínica")

    def test_modificar_dias(self):
        self.esp.__dias__ = ["martes"]
        self.assertTrue(self.esp.verificar_dia("martes"))
        self.assertFalse(self.esp.verificar_dia("lunes"))

if __name__ == '__main__':
    unittest.main()