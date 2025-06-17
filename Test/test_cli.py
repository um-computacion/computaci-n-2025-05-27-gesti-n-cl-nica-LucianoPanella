import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from io import StringIO
from src.gestion_clinica import Clinica_Cli

class TestClinicaCLI(unittest.TestCase):
    def setUp(self):
        self.cli = Clinica_Cli()

    @patch('builtins.input', side_effect=[
        "1", "Juan Perez", "12345678", "01/01/2000", "9"
    ])
    def test_agregar_paciente(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Paciente agregado correctamente.", output)

    @patch('builtins.input', side_effect=[
        "1", "Juan Perez", "12345678", "01/01/2000",
        "1", "Juan Perez", "12345678", "01/01/2000", "9"
    ])
    def test_agregar_paciente_duplicado(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("El paciente ya está registrado.", output)

    @patch('builtins.input', side_effect=[
        "1", "", "12345678", "01/01/2000", "9"
    ])
    def test_agregar_paciente_nombre_vacio(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("El nombre no puede estar vacío.", output)

    @patch('builtins.input', side_effect=[
        "1", "Juan Perez", "abc", "01/01/2000", "9"
    ])
    def test_agregar_paciente_dni_invalido(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("El DNI debe ser numérico.", output)

    @patch('builtins.input', side_effect=[
        "2", "Dra. Lopez", "M123", "Pediatría", "lunes,martes", "9"
    ])
    def test_agregar_medico(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Médico agregado correctamente.", output)

    @patch('builtins.input', side_effect=[
        "2", "Dra. Lopez", "M123", "Pediatría", "lunes,martes",
        "2", "Dra. Lopez", "M123", "Pediatría", "lunes,martes", "9"
    ])
    def test_agregar_medico_duplicado(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("El médico ya está registrado.", output)

    @patch('builtins.input', side_effect=[
        "2", "", "M123", "Pediatría", "lunes,martes", "9"
    ])
    def test_agregar_medico_nombre_vacio(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("El nombre no puede estar vacío.", output)

    @patch('builtins.input', side_effect=[
        "2", "Dra. Lopez", "", "Pediatría", "lunes,martes", "9"
    ])
    def test_agregar_medico_matricula_vacia(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("La matrícula no puede estar vacía.", output)

    @patch('builtins.input', side_effect=[
        "1", "Ana Torres", "87654321", "02/02/1990",
        "2", "Dr. House", "M456", "Clínica", "miércoles",
        "3", "87654321", "M456", "10/06/2025", "10:00", "Clínica", "9"
    ])
    def test_agendar_turno(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Turno agendado correctamente.", output)

    @patch('builtins.input', side_effect=[
        "2", "Dra. Lopez", "M123", "Cardiología", "lunes,miércoles",
        "3", "99999999", "M123", "10/06/2025", "10:00", "Cardiología", "9"
    ])
    def test_agendar_turno_paciente_no_encontrado(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Paciente no encontrado", output)

    @patch('builtins.input', side_effect=[
        "3", "99999999", "M999", "10/06/2025", "10:00", "Clínica", "9"
    ])
    def test_agendar_turno_paciente_y_medico_no_encontrados(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Paciente y médico no encontrados", output)

    @patch('builtins.input', side_effect=[
        "2", "Dra. Lopez", "M123", "Cardiología", "lunes,miércoles",
        "3", "99999999", "M123", "10/06/2025", "10:00", "Cardiología", "9"
    ])
    def test_agendar_turno_solo_paciente_no_encontrado(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Paciente no encontrado", output)

    @patch('builtins.input', side_effect=[
        "1", "Juan Perez", "12345678", "01/01/2000",
        "2", "Dra. Lopez", "M123", "Cardiología", "lunes,miércoles",
        "3", "12345678", "M123", "10/06/2025", "10:00", "Cardiología",
        "4", "12345678", "M123", "Aspirina,Paracetamol", "15/06/2025", "9"
    ])
    def test_emitir_receta(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Receta emitida correctamente.", output)

    @patch('builtins.input', side_effect=[
        "4", "99999999", "M789", "Aspirina,Paracetamol", "15/06/2025", "9"
    ])
    def test_emitir_receta_paciente_no_encontrado(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Paciente no encontrado", output)

    @patch('builtins.input', side_effect=[
        "1", "Lucia Gomez", "99887766", "04/04/1995",
        "5", "9"
    ])
    def test_ver_pacientes(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Lucia Gomez", output)
            self.assertIn("99887766", output)

    @patch('builtins.input', side_effect=[
        "2", "Dr. Strange", "M321", "Neurología", "viernes",
        "6", "9"
    ])
    def test_ver_medicos(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Dr. Strange", output)
            self.assertIn("M321", output)
            self.assertIn("Neurología", output)

    @patch('builtins.input', side_effect=[
        "1", "Mario Rossi", "55667788", "05/05/1980",
        "2", "Dr. Who", "M654", "General", "lunes",
        "3", "55667788", "M654", "20/06/2025", "09:00", "General",
        "7", "9"
    ])
    def test_ver_turnos(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Mario Rossi", output)
            self.assertIn("Dr. Who", output)
            self.assertIn("20/06/2025", output)

    @patch('builtins.input', side_effect=[
        "1", "Laura Diaz", "33445566", "06/06/1992",
        "8", "33445566", "9"
    ])
    def test_ver_historia_clinica(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Historia Clínica de Laura Diaz", output)
            self.assertIn("Turnos:", output)
            self.assertIn("Recetas:", output)

    @patch('builtins.input', side_effect=[
        "8", "99999999", "9"
    ])
    def test_ver_historia_clinica_no_encontrada(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Historia clínica no encontrada.", output)

    @patch('builtins.input', side_effect=[
        "9"
    ])
    def test_salir(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Gracias por usar el sistema de gestión clínica", output)

    @patch('builtins.input', side_effect=[
        "10", "9"
    ])
    def test_opcion_invalida(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.ejecutar()
            output = fake_out.getvalue()
            self.assertIn("Opción no válida, intente nuevamente.", output)

if __name__ == '__main__':
    unittest.main()