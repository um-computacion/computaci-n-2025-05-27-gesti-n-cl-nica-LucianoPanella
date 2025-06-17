import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.gestion_clinica import Paciente, Especialidad, Medico, Receta

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.pac = Paciente("Juan Perez", "12345678", "01/01/2000")
        self.esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.med = Medico("Dra. Lopez", "M123", self.esp)
        self.rec = Receta(self.pac, self.med, ["Ibuprofeno", "Paracetamol"], "10/06/2025")

    def test_atributo_paciente(self):
        self.assertEqual(self.rec.__paciente__, self.pac)

    def test_atributo_medico(self):
        self.assertEqual(self.rec.__medico__, self.med)

    def test_atributo_medicamentos(self):
        self.assertEqual(self.rec.__medicamentos__, ["Ibuprofeno", "Paracetamol"])

    def test_atributo_fecha(self):
        self.assertEqual(self.rec.__fecha__, "10/06/2025")

    def test_obtener_paciente(self):
        self.assertEqual(self.rec.obtener_paciente(), self.pac)

    def test_obtener_medico(self):
        self.assertEqual(self.rec.obtener_medico(), self.med)

    def test_obtener_medicamentos(self):
        self.assertEqual(self.rec.obtener_medicamentos(), ["Ibuprofeno", "Paracetamol"])

    def test_obtener_fecha(self):
        self.assertEqual(self.rec.obtener_fecha(), "10/06/2025")

    def test_str(self):
        esperado = "Paciente: Juan Perez, Médico: Dra. Lopez, Medicamentos: Ibuprofeno, Paracetamol, Fecha: 10/06/2025"
        self.assertEqual(str(self.rec), esperado)

    def test_medicamentos_vacio(self):
        rec = Receta(self.pac, self.med, [], "11/06/2025")
        self.assertEqual(rec.__medicamentos__, [])
        esperado = "Paciente: Juan Perez, Médico: Dra. Lopez, Medicamentos: , Fecha: 11/06/2025"
        self.assertEqual(str(rec), esperado)

    def test_medicamentos_unico(self):
        rec = Receta(self.pac, self.med, ["Amoxicilina"], "12/06/2025")
        self.assertEqual(rec.obtener_medicamentos(), ["Amoxicilina"])
        esperado = "Paciente: Juan Perez, Médico: Dra. Lopez, Medicamentos: Amoxicilina, Fecha: 12/06/2025"
        self.assertEqual(str(rec), esperado)

    def test_fecha_vacia(self):
        rec = Receta(self.pac, self.med, ["Ibuprofeno"], "")
        self.assertEqual(rec.obtener_fecha(), "")

    def test_paciente_vacio(self):
        pac = Paciente("", "", "")
        rec = Receta(pac, self.med, ["Ibuprofeno"], "13/06/2025")
        self.assertEqual(rec.__paciente__.__nombre_paciente__, "")

    def test_medico_vacio(self):
        esp = Especialidad("Clínica", ["martes"])
        med = Medico("", "", esp)
        rec = Receta(self.pac, med, ["Ibuprofeno"], "14/06/2025")
        self.assertEqual(rec.__medico__.__nombre__, "")

    def test_modificar_medicamentos(self):
        self.rec.__medicamentos__ = ["Paracetamol"]
        self.assertEqual(self.rec.obtener_medicamentos(), ["Paracetamol"])

    def test_modificar_fecha(self):
        self.rec.__fecha__ = "20/06/2025"
        self.assertEqual(self.rec.obtener_fecha(), "20/06/2025")

    def test_str_con_campos_vacios(self):
        pac = Paciente("", "", "")
        esp = Especialidad("", [])
        med = Medico("", "", esp)
        rec = Receta(pac, med, [], "")
        esperado = "Paciente: , Médico: , Medicamentos: , Fecha: "
        self.assertEqual(str(rec), esperado)

    def test_medicamentos_numericos(self):
        rec = Receta(self.pac, self.med, [123, 456], "15/06/2025")
        self.assertEqual(rec.obtener_medicamentos(), [123, 456])
        esperado = "Paciente: Juan Perez, Médico: Dra. Lopez, Medicamentos: 123, 456, Fecha: 15/06/2025"
        self.assertEqual(str(rec), esperado)

if __name__ == '__main__':
    unittest.main()