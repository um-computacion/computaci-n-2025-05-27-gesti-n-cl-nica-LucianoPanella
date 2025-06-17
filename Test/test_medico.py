import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.gestion_clinica import Medico, Especialidad

class TestMedico(unittest.TestCase):
    def setUp(self):
        self.esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.med = Medico("Dra. Lopez", "M123", self.esp)

    def test_atributo_nombre(self):
        self.assertEqual(self.med.__nombre__, "Dra. Lopez")

    def test_atributo_matricula(self):
        self.assertEqual(self.med.__matricula__, "M123")

    def test_atributo_especialidad(self):
        self.assertEqual(self.med.__especialidad__, self.esp)

    def test_obtener_matricula(self):
        self.assertEqual(self.med.obtener_matricula(), "M123")

    def test_obtener_especialidad_para_dia(self):
        self.assertEqual(self.med.obtener_especialidad_para_dia(), self.esp)

    def test_str(self):
        esperado = "Nombre: Dra. Lopez, Matricula: M123, Especialidad: Cardiología, Dias: lunes, miércoles"
        self.assertEqual(str(self.med), esperado)

    def test_nombre_vacio(self):
        med = Medico("", "M124", self.esp)
        self.assertEqual(med.__nombre__, "")

    def test_matricula_vacia(self):
        med = Medico("Dr. House", "", self.esp)
        self.assertEqual(med.__matricula__, "")

    def test_especialidad_nula(self):
        med = Medico("Dr. House", "M125", None)
        self.assertIsNone(med.__especialidad__)

    def test_str_con_especialidad_nula(self):
        med = Medico("Dr. House", "M125", None)
        with self.assertRaises(AttributeError):
            str(med)

    def test_modificar_nombre(self):
        self.med.__nombre__ = "Dr. Strange"
        self.assertEqual(self.med.__nombre__, "Dr. Strange")

    def test_modificar_matricula(self):
        self.med.__matricula__ = "M999"
        self.assertEqual(self.med.obtener_matricula(), "M999")

    def test_modificar_especialidad(self):
        nueva_esp = Especialidad("Neurología", ["viernes"])
        self.med.__especialidad__ = nueva_esp
        self.assertEqual(self.med.obtener_especialidad_para_dia(), nueva_esp)

    def test_str_con_dias_vacios(self):
        esp = Especialidad("Dermatología", [])
        med = Medico("Dr. Skin", "M200", esp)
        esperado = "Nombre: Dr. Skin, Matricula: M200, Especialidad: Dermatología, Dias: "
        self.assertEqual(str(med), esperado)

    def test_str_con_tipo_especialidad_numerico(self):
        esp = Especialidad(123, ["lunes"])
        med = Medico("Dr. Num", "M201", esp)
        esperado = "Nombre: Dr. Num, Matricula: M201, Especialidad: 123, Dias: lunes"
        self.assertEqual(str(med), esperado)

if __name__ == '__main__':
    unittest.main()