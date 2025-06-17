import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from src.gestion_clinica import Paciente, Especialidad, Medico, HistoriaClinica, Clinica
from src.gestion_clinica import PacienteYaRegistradoException, MedicoYaRegistradoException
from src.gestion_clinica import PacienteNoEncontradoException, MedicoNoEncontradoException   
from src.gestion_clinica import TurnoOcupadoException, RecetaInvalidaException

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.pac1 = Paciente("Juan Perez", "12345678", "01/01/2000")
        self.pac2 = Paciente("Ana Torres", "87654321", "02/02/1990")
        self.esp1 = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.esp2 = Especialidad("Clínica", ["martes"])
        self.med1 = Medico("Dra. Lopez", "M123", self.esp1)
        self.med2 = Medico("Dr. House", "M456", self.esp2)
        self.hist1 = HistoriaClinica(self.pac1)
        self.hist2 = HistoriaClinica(self.pac2)
        self.clinica = Clinica(
            pacientes=[self.pac1, self.pac2],
            medicos=[self.med1, self.med2],
            turnos=[],
            historias_clinicas=[self.hist1, self.hist2]
        )

    def test_agregar_paciente(self):
        nuevo_pac = Paciente("Carlos Ruiz", "11223344", "03/03/1985")
        self.clinica.agregar_paciente(nuevo_pac)
        self.assertIn(nuevo_pac, self.clinica.obtener_pacientes())

    def test_agregar_paciente_duplicado(self):
        with self.assertRaises(PacienteYaRegistradoException):
            self.clinica.agregar_paciente(self.pac1)

    def test_agregar_medico(self):
        nuevo_med = Medico("Dra. Smith", "M789", self.esp1)
        self.clinica.agregar_medico(nuevo_med)
        self.assertIn(nuevo_med, self.clinica.obtener_medicos())

    def test_agregar_medico_duplicado(self):
        with self.assertRaises(MedicoYaRegistradoException):
            self.clinica.agregar_medico(self.med1)

    def test_agendar_turno(self):
        turno_nuevo = self.clinica.agendar_turno("12345678", "M123", "10/06/2025", "10:00", self.esp1)
        self.assertIn(turno_nuevo, self.clinica.obtener_turnos())
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertIn(turno_nuevo, historia.obtener_turnos())

    def test_agendar_turno_paciente_no_encontrado(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("99999999", "M123", "10/06/2025", "10:00", self.esp1)

    def test_agendar_turno_medico_no_encontrado(self):
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.agendar_turno("12345678", "M999", "10/06/2025", "10:00", self.esp1)

    def test_agendar_turno_duplicado(self):
        self.clinica.agendar_turno("12345678", "M123", "10/06/2025", "10:00", self.esp1)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "M123", "10/06/2025", "10:00", self.esp1)

    def test_emitir_receta(self):
        medicamentos = ["Aspirina", "Paracetamol"]
        receta_nueva = self.clinica.emitir_receta("12345678", "M123", medicamentos, "15/06/2025")
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertIn(receta_nueva, historia.obtener_receta())

    def test_emitir_receta_paciente_no_encontrado(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("99999999", "M123", ["Aspirina"], "15/06/2025")

    def test_emitir_receta_medico_no_encontrado(self):
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.emitir_receta("12345678", "M999", ["Aspirina"], "15/06/2025")

    def test_emitir_receta_invalida(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "M123", [], "15/06/2025")

    def test_obtener_pacientes(self):
        pacientes = self.clinica.obtener_pacientes()
        self.assertIn(self.pac1, pacientes)
        self.assertIn(self.pac2, pacientes)

    def test_obtener_medicos(self):
        medicos = self.clinica.obtener_medicos()
        self.assertIn(self.med1, medicos)
        self.assertIn(self.med2, medicos)

    def test_obtener_turnos_vacio(self):
        self.assertEqual(self.clinica.obtener_turnos(), [])

    def test_obtener_historia_clinica(self):
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(historia, self.hist1)

    def test_obtener_historia_clinica_no_encontrada(self):
        historia = self.clinica.obtener_historia_clinica("99999999")
        self.assertIsNone(historia)

if __name__ == '__main__':
    unittest.main()