from unittest.mock import MagicMock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import unittest
from unittest.mock import patch
from view.Menu import LogicIA, LogicJugador, MenuScreen
from view.Tablero import TableroJugador, TableroMaquina


class TestLogicIA(unittest.TestCase):

    def setUp(self):
        self.tablero_maquina = TableroMaquina()
        self.tablero_jugador = TableroJugador()
        self.logic_ia = LogicIA(self.tablero_maquina, self.tablero_jugador)

    def test_colocar_barcos_maquina(self):
        # Comprueba que se colocan 10 barcos en el tablero de la máquina
        self.logic_ia.colocar_barcos_maquina()
        self.assertEqual(len(self.logic_ia.barcos_maquina), 10)

    
class TestLogicJugador(unittest.TestCase):

    def setUp(self):
        self.tablero_maquina = TableroMaquina()
        self.tablero_jugador = TableroJugador()
        self.logic_jugador = LogicJugador(self.tablero_jugador, self.tablero_maquina)

    def test_colocar_barco_jugador(self):
        # Simula la colocación de barcos por parte del jugador
        for btn in self.tablero_jugador.buttons[:10]:
            self.logic_jugador.colocar_barco_jugador(btn)
        self.assertEqual(len(self.logic_jugador.barcos_jugador), 10)

    @patch('random.random', return_value=0.1)  # Mock para controlar random.random
    def test_realizar_ataque_jugador(self, mock_random):
        # Prueba que se realiza un ataque de manera adecuada
        self.logic_jugador.realizar_ataque_jugador(self.tablero_maquina.buttons[0])
        self.assertTrue(self.tablero_maquina.buttons[0].text in ['X', '-'])
        
class TestMenuScreen(unittest.TestCase):

    def setUp(self):
        self.menu_screen = MenuScreen()

    def test_initialization(self):
        # Prueba que los widgets se inicializan correctamente
        self.assertIsInstance(self.menu_screen.btn_jugar, Button)
        self.assertIsInstance(self.menu_screen.btn_nosotros, Button)
        self.assertIsInstance(self.menu_screen.btn_salir, Button)
        self.assertIsInstance(self.menu_screen.chess_layout, BoxLayout)
        self.assertIsInstance(self.menu_screen.tablero_jugador, TableroJugador)
        self.assertIsInstance(self.menu_screen.tablero_maquina, TableroMaquina)


if __name__ == '__main__':
    unittest.main()

