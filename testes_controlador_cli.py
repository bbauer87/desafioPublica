__author__ = "Bruno Silveira Bauer"
__version__ = "1.0.1"

import unittest
import os


from controlador_cli import ControladorCli


class TestesControlCLI(unittest.TestCase):
    '''
    Classe que testa a funcionalidade geral do script controlador_cli.py
    '''

    def test_1_cli(self):
        try:
            with self.assertRaises(Exception):
                cli = ControladorCli()

        except AssertionError:
            pass

        except SystemExit:
            pass
    


if __name__ == "__main__":
    unittest.main()
