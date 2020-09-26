import unittest
import os

from banco import BD


class TestesBanco(unittest.TestCase):

    def deleta_BD(self):
        if os.path.isfile(".//BDs//teste.db"):
            os.remove(".//BDs//teste.db")
            

    def test_1_abre_fecha_conexao(self):
        '''
        1 - Conecta com um banco de dados chamado teste.db,
        e depois encerra a conexão. Testa o construtor e os
        módulos "cria_tabela" e "encerra".
        '''
        bd = BD(".\\BDs\\teste.db")
        bd.encerra()

        self.deleta_BD()
        
        
    def test_2_tabela_vazia(self):
        '''
        2 - Espera-se que uma tabela recém criada tenha seis colunas
        e nenhuma linha. Testa o módulo "printa_tabela".
        '''
        bd = BD(".\\BDs\\teste.db")
        self.assertEqual(bd.tabela, "temporada_2020")
        itens, colunas = bd.printa_tabela()   
        bd.encerra()
        self.deleta_BD()       
        
        self.assertEqual(itens, [])
        self.assertEqual(len(colunas), 6)


    def test_3_add_placar_1(self):
        '''
        3 - Ao adicionar um jogo com placar de 12 pontos numa tabela vazia,
        a primeira linha deve ser igual à variável "valores". Testa o método
        "adicionar_placar" validando seu último bloco de expressões condicionais.
        '''
        bd = BD(".\\BDs\\teste.db")
        valores = (1, 12, 12, 12, 0, 0)
        bd.adiciona_placar(12, "primeiro jogo")
        itens = bd.printa_tabela()[0]     
        bd.encerra()
        self.deleta_BD()     
        
        self.assertEqual(itens[0], valores)

        
    def test_4_add_placar_2(self):
        '''
        4 - Ao adicionar um jogo com placar de 24 pontos numa tabela não vazia,
        a última linha deve ser igual à variável "valores". Testa os métodos
        "retorna_tabela" (usando parâmetro "última linha") e "adiciona_placar",
        validando o bloco "novo máximo" das expressões condicionais deste método.
        '''
        bd = BD(".\\BDs\\teste.db")
        valores = (2, 24, 12, 24, 0, 1)
        
        bd.adiciona_placar(12, "primeiro jogo")        
        bd.adiciona_placar([24, 12, 24, 0, 1], "novo máximo")        
        ultima_linha = bd.retorna_tabela("última linha")[0]    
        bd.encerra()
        self.deleta_BD()      
        
        self.assertEqual(ultima_linha, valores)


    def test_5_add_placar_3(self):
        '''
        5 - Ao adicionar três jogos com placares 30, 11 e 18, espera-se que
        a tabela inteira seja igual à variável "valores". Testa os métodos
        "retorna_tabela" (usando parâmetro "inteira") e "adiciona_placar",
        validando os blocos "novo mínimo" e "normal" das suas expressões
        condicionais.
        '''
        bd = BD(".\\BDs\\teste.db")
        valores = [(1, 30, 30, 30, 0, 0),
                   (2, 11, 11, 30, 1, 0),
                   (3, 18, 11, 30, 1, 0),
                   ]

        bd.adiciona_placar(30, "primeiro jogo")
        bd.adiciona_placar([11, 11, 30, 1, 0], "novo mínimo")
        bd.adiciona_placar([18, 11, 30, 1, 0], "normal")
        
        self.assertEqual(bd.retorna_tabela("inteira"), valores)
        
        bd.encerra()
        self.deleta_BD()  
        
        
    def test_6_add_placar_4(self):
        '''
        6 - Teste para adicionar placares com três digitos: 123 e 999.
        '''
        bd = BD(".\\BDs\\teste.db")        
        bd.adiciona_placar(123, "primeiro jogo")
      
        min_temp, max_temp, quebra_min, quebra_max = bd.retorna_tabela("última linha")[0][2:] 

        placar = 999
        valores = (2, placar, 123, placar, 0, 1)

        bd.adiciona_placar([placar, min_temp, placar, quebra_min, quebra_max + 1], "novo máximo")
        self.assertEqual(bd.retorna_tabela("última linha")[0], valores)
        
        bd.encerra()
        self.deleta_BD()   

        
    def test_7_add_placar_5(self):
        '''
        7 - Adiciona 11 jogos com um, dois e três dígitos, quebrando duas vezes o recorde mínimo
        e quatro vezes o recorde máximo. Ao final, espera-se que a tabela seja igual à variável "valores".
        '''
        bd = BD(".\\BDs\\teste.db")  
        valores = [(1, 5, 5, 5, 0, 0),
                   (2, 12, 5, 12, 0, 1),
                   (3, 7, 5, 12, 0, 1),
                   (4, 16, 5, 16, 0, 2),
                   (5, 4, 4, 16, 1, 2),
                   (6, 16, 4, 16, 1, 2),
                   (7, 8, 4, 16, 1, 2),
                   (8, 21, 4, 21, 1, 3),
                   (9, 17, 4, 21, 1, 3),
                   (10, 1, 1, 21, 2, 3),
                   (11, 386, 1, 386, 2, 4),
                   ]
        
        bd.adiciona_placar(5, "primeiro jogo")
        tmp = [[12, "novo máximo"],
               [7, "normal"],
               [16, "novo máximo"],
               [4, "novo mínimo"],
               [16, "normal"],
               [8, "normal"],
               [21, "novo máximo"],
               [17, "normal"],
               [1, "novo mínimo"],
               [386, "novo máximo"],
               ]

        for x in tmp:
            min_temp, max_temp, quebra_min, quebra_max = bd.retorna_tabela("última linha")[0][2:]        
            placar = x[0]
            if placar < min_temp:
                quebra_min += 1

            elif placar > max_temp:
                quebra_max += 1
                
            bd.adiciona_placar([placar, min_temp, max_temp, quebra_min, quebra_max], x[1])

        self.assertEqual(bd.retorna_tabela("inteira"), valores)
        
        bd.encerra()
        self.deleta_BD()



        




if __name__ == "__main__":
    unittest.main()
