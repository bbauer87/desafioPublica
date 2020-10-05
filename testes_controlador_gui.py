__author__ = "Bruno Silveira Bauer"
__version__ = "1.0.1"

import unittest
import os

from controlador_gui import ControladorGui
from datetime import datetime



CAMINHO = ".\\BD\\teste.db"


class TestesControlGUI(unittest.TestCase):
    '''
    Classe que testa os métodos do script controlador_gui.py
    '''

    def deleta_BD(self):
        '''
        Após cada teste, o BD criado será excluído.
        '''
        
        if os.path.isfile(CAMINHO):
            os.remove(CAMINHO)
    
    def test_1_abre_fecha_conexao(self):
        '''
        1 - Abrir e fechar uma conexão com BD.

        Conecta com um banco de dados chamado teste.db,
        e depois encerra a conexão. Testa o construtor e os
        métodos "busca_bds" e "encerra".
        '''

        try:
            with self.assertRaises(Exception):
                app = ControladorGui()
                app.conecta(CAMINHO)
                app.encerra()

        except AssertionError:
            pass            

        self.deleta_BD()

    def test_2_cria_deleta_bd(self):
        '''
        2 - Testes de criação, consulta e deleção de um BD.

        Testa os métodos "altera_cria_bd", "tabela" e "deletar",
        conforme se cria um BD chamado "teste2.db", depois se define
        uma tabela chamada "321" e por fim deleta-se esse BD.
        '''

        app = ControladorGui()
        app.conecta(CAMINHO)

        retorno = app.altera_cria_bd(["teste2.db", None])

        self.assertEqual(retorno, str(datetime.now().year))

        app.tabela("escolhe", "321")

        self.assertEqual(app.tabela("consulta"), [str(datetime.now().year), "321"])

        app.conecta(CAMINHO)
        app.deletar("deletar BD", "teste2.db")

        with self.assertRaises(Exception):
            os.remove(".\\BD\\teste2.db")
            
        app.encerra()
        self.deleta_BD()

    def test_3_add_retorna_dados(self):
        '''
        3 - Testes ao adicionar seis jogos, onde os dados retornados devem
        ser iguais aos discriminados abaixo.

        Testa os métodos "retorna_dados" e "add_placar".
        '''
        
        app = ControladorGui()
        app.conecta(CAMINHO)
        app.tabela("escolhe", "2020")

        retorno = app.add_placar(10)
        self.assertEqual(retorno, "normal")
        
        retorno = app.add_placar(15)
        self.assertEqual(retorno, "novo máximo")
        
        retorno = app.add_placar(5)
        self.assertEqual(retorno, "novo mínimo")

        for x in [20, 23, 25]:
            app.add_placar(x)

        tab_inteira, top_5, top_5_piores, soma_placares = app.retorna_dados()

        valor_tab_inteira = [(1, 10, 10, 10, 0 ,0),
                             (2, 15, 10, 15, 0, 1),
                             (3, 5, 5, 15, 1, 1),
                             (4, 20, 5, 20, 1, 2),
                             (5, 23, 5, 23, 1, 3),
                             (6, 25, 5, 25, 1, 4),
                             ]

        self.assertEqual(tab_inteira, valor_tab_inteira)
        self.assertEqual(top_5, [25, 23, 20, 15, 10])
        self.assertEqual(top_5_piores, [5, 10, 15, 20, 23])
        self.assertEqual(soma_placares, 98)
        
        app.encerra()
        self.deleta_BD()

    def test_4_add_temporada(self):
        '''
        4 - Teste de criação de temporada.

        Testa o método "altera_cria_temp".
        '''

        app = ControladorGui()
        app.conecta(CAMINHO)
        app.tabela("escolhe", "2020")

        retorno_tabelas, retorno_tab_atual = app.altera_cria_temp("inicial")

        self.assertEqual(retorno_tabelas, [])
        self.assertEqual(retorno_tab_atual, "temporada_2020")
        
        app.altera_cria_temp("criação", "1234")

        self.assertEqual(app.bd.tabela, "temporada_1234")

        
        app.encerra()
        self.deleta_BD()




if __name__ == "__main__":
    unittest.main()
