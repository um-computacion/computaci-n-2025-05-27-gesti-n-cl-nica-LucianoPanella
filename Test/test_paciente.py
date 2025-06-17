import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.gestion_clinica import Paciente

class TestPaciente(unittest.TestCase):
    def setUp(self):
        self.pac = Paciente("Juan Perez", "12345678", "01/01/2000")

    def test_atributo_nombre(self):
        self.assertEqual(self.pac.__nombre_paciente__, "Juan Perez")

    def test_atributo_dni(self):
        self.assertEqual(self.pac.__dni__, "12345678")

    def test_atributo_fecha_nacimiento(self):
        self.assertEqual(self.pac.__fecha_nacimiento__, "01/01/2000")

    def test_obtener_dni(self):
        self.assertEqual(self.pac.obtener_dni(), "12345678")

    def test_str(self):
        esperado = "Nombre: Juan Perez, DNI: 12345678, Fecha de Nacimiento: 01/01/2000"
        self.assertEqual(str(self.pac), esperado)

    def test_nombre_vacio(self):
        pac = Paciente("", "87654321", "02/02/1990")
        self.assertEqual(pac.__nombre_paciente__, "")

    def test_dni_vacio(self):
        pac = Paciente("Ana Torres", "", "02/02/1990")
        self.assertEqual(pac.__dni__, "")

    def test_fecha_nacimiento_vacia(self):
        pac = Paciente("Ana Torres", "87654321", "")
        self.assertEqual(pac.__fecha_nacimiento__, "")

    def test_nombre_numerico(self):
        pac = Paciente(123, "87654321", "02/02/1990")
        self.assertEqual(pac.__nombre_paciente__, 123)

    def test_dni_numerico(self):
        pac = Paciente("Ana Torres", 87654321, "02/02/1990")
        self.assertEqual(pac.__dni__, 87654321)

    def test_fecha_nacimiento_numerica(self):
        pac = Paciente("Ana Torres", "87654321", 20200101)
        self.assertEqual(pac.__fecha_nacimiento__, 20200101)

    def test_modificar_nombre(self):
        self.pac.__nombre_paciente__ = "Carlos Ruiz"
        self.assertEqual(self.pac.__nombre_paciente__, "Carlos Ruiz")

    def test_modificar_dni(self):
        self.pac.__dni__ = "99999999"
        self.assertEqual(self.pac.obtener_dni(), "99999999")

    def test_modificar_fecha_nacimiento(self):
        self.pac.__fecha_nacimiento__ = "31/12/1999"
        self.assertEqual(self.pac.__fecha_nacimiento__, "31/12/1999")

    def test_str_con_campos_vacios(self):
        pac = Paciente("", "", "")
        esperado = "Nombre: , DNI: , Fecha de Nacimiento: "
        self.assertEqual(str(pac), esperado)

if __name__ == '__main__':
    unittest.main()