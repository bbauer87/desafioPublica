__author__ = "Bruno Silveira Bauer"
__version__ = "1.0.1"

import unittest
import os

from banco import BD

CAMINHO = ".\\BD\\teste.db"

class TestesBanco(unittest.TestCase):
    '''
    Classe que testa os métodos do script banco.py
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
        métodos "cria_tabela" e "encerra".
        '''
        bd = BD(CAMINHO)
        bd.encerra()

        self.deleta_BD()
        
        
    def test_2_tabela_vazia(self):
        '''
        2 - Testar uma tabela vazia.

        Espera-se que uma tabela recém criada tenha seis colunas
        e nenhuma linha. Testa os métodos "printa_tabela" e
        "define_tabela".
        '''
        bd = BD(CAMINHO)
        bd.define_tabela("2020")
        self.assertEqual(bd.tabela, "temporada_2020")
        itens, colunas = bd.printa_tabela()   
        bd.encerra()
        self.deleta_BD()       
        
        self.assertEqual(itens, [])
        self.assertEqual(len(colunas), 6)


    def test_3_add_placar_1(self):
        '''
        3 - Teste de adicionar placar 1.

        Ao adicionar um jogo com placar de 12 pontos numa tabela vazia,
        a primeira linha deve ser igual à variável "valores". Testa o método
        "adicionar_placar" validando seu último bloco de expressões condicionais.
        '''
        bd = BD(CAMINHO)
        bd.define_tabela("51")
        valores = (1, 12, 12, 12, 0, 0)
        bd.adiciona_placar(12, "primeiro jogo")
        itens = bd.printa_tabela()[0]     
        bd.encerra()
        self.deleta_BD()     
        
        self.assertEqual(itens[0], valores)

        
    def test_4_add_placar_2(self):
        '''
        4 - Teste de adicionar placar 2.

        Ao adicionar um jogo com placar de 24 pontos numa tabela não vazia,
        a última linha deve ser igual à variável "valores". Testa os métodos
        "retorna_tabela" (usando parâmetro "última linha") e "adiciona_placar",
        validando o bloco "novo máximo" das expressões condicionais deste método.
        '''
        bd = BD(CAMINHO)
        bd.define_tabela("1234")
        valores = (2, 24, 12, 24, 0, 1)
        
        bd.adiciona_placar(12, "primeiro jogo")        
        bd.adiciona_placar([24, 12, 24, 0, 1], "novo máximo")        
        ultima_linha = bd.retorna_tabela("última linha")[0]    
        bd.encerra()
        self.deleta_BD()      
        
        self.assertEqual(ultima_linha, valores)


    def test_5_add_placar_3(self):
        '''
        5 - Teste de adicionar placar 3.

        Ao adicionar três jogos com placares 30, 11 e 18, espera-se que
        a tabela inteira seja igual à variável "valores". Testa os métodos
        "retorna_tabela" (usando parâmetro "inteira") e "adiciona_placar",
        validando os blocos "novo mínimo" e "normal" das suas expressões
        condicionais.
        '''
        bd = BD(CAMINHO)
        bd.define_tabela("10000")
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
        6 - Teste de adicionar placar 4.

        Teste para adicionar placares com três digitos: 123 e 999.
        '''
        bd = BD(CAMINHO)     
        bd.define_tabela("3")   
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
        7 - Teste de adicionar placar 5.

        Adiciona 11 jogos com um, dois e três dígitos, quebrando duas vezes o recorde mínimo
        e quatro vezes o recorde máximo. Ao final, espera-se que a tabela seja igual à variável "valores".
        '''
        bd = BD(CAMINHO)     
        bd.define_tabela("8219")   
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


    def test_8_define_deleta_tabelas(self):
        '''
        8 - Definir e deletar tabelas.

        Ao adicionar as respectivas temporadas no BD, espera-se que a lista
        das temporadas seja igual à variável "valores". Em seguida, verifica-se
        a igualdade de ambas perante a remoção de uma temporada. Testa os métodos
        "define_tabela" e "deleta_tabela".
        '''
        bd = BD(CAMINHO)    
        bd.define_tabela("2020")    
        bd.define_tabela("2021")    
        bd.define_tabela("2022")

        valores = ["temporada_2020", "temporada_2021", "temporada_2022"]

        self.assertEqual([x[0] for x in bd.verifica_tabelas()], valores)

        valores.remove("temporada_2021")
        bd.deleta_tabela("temporada_2021")

        self.assertEqual([x[0] for x in bd.verifica_tabelas()], valores)
        
        bd.encerra()
        self.deleta_BD()

    
    def test_9_soma_media_placares(self):
        '''
        9 - Calcular soma e média dos placares.

        Ao popular uma temporada com sete jogos, espera-se que a soma e a média
        dos placares sejam iguais às variáveis "valor_soma" e "valor_média",
        respectivamente. Testa os métodos "soma_placares" e "media_placares".
        '''
        bd = BD(CAMINHO)    
        bd.define_tabela("1497")
        
        bd.adiciona_placar(5, "primeiro jogo")
        tmp = [[12, "novo máximo"],
               [7, "normal"],
               [16, "novo máximo"],
               [4, "novo mínimo"],
               [16, "normal"],
               [8, "normal"],
               ]

        for x in tmp:
            min_temp, max_temp, quebra_min, quebra_max = bd.retorna_tabela("última linha")[0][2:]        
            placar = x[0]
            if placar < min_temp:
                quebra_min += 1

            elif placar > max_temp:
                quebra_max += 1
                
            bd.adiciona_placar([placar, min_temp, max_temp, quebra_min, quebra_max], x[1])

        valor_soma = 5 + sum([x[0] for x in tmp])
        valor_media = valor_soma / (len(tmp) + 1)

        self.assertEqual(bd.soma_placares(), valor_soma)
        self.assertEqual(bd.media_placares(), valor_media)
        
        bd.encerra()
        self.deleta_BD()

        
    def test_10_top_5_print(self):
        '''
        11 - Teste dos melhores e dos piores top 5.

        Ao popular uma temporada com sete jogos, espera-se que os melhores
        e os piores top 5 sejam iguais às variáveis "valor_top_5" e "valor_piores_top_5".
        Em seguida, verifica se as somas de ambos valores são iguais às variáveis
        "valor_soma_top_5" e "valor_soma_piores_top_5".

        Testa os métodos "top_5" e "top_5_piores" com os dois blocos condicionais de cada um.
        Também é testado o método "printa_tabela_2", cujos dois primeiros valores retornados
        devem ser iguais às variáveis "valor_estats_1" e "valor_estats_2", respectivamente.
        '''
        bd = BD(CAMINHO)    
        bd.define_tabela("404")

        bd.adiciona_placar(5, "primeiro jogo")
        tmp = [[12, "novo máximo"],
               [7, "normal"],
               [16, "novo máximo"],
               [4, "novo mínimo"],
               [16, "normal"],
               [8, "normal"],
               ]

        for x in tmp:
            min_temp, max_temp, quebra_min, quebra_max = bd.retorna_tabela("última linha")[0][2:]        
            placar = x[0]
            if placar < min_temp:
                quebra_min += 1

            elif placar > max_temp:
                quebra_max += 1
                
            bd.adiciona_placar([placar, min_temp, max_temp, quebra_min, quebra_max], x[1])


        valor_top_5 = [16, 16, 12, 8, 7]
        valor_piores_top_5 = [4, 5, 7, 8, 12]

        self.assertEqual(bd.top_5("lista"), valor_top_5)
        self.assertEqual(bd.top_5_piores("lista"), valor_piores_top_5)
        
        valor_soma_top_5 = sum(valor_top_5)
        valor_soma_piores_top_5 = sum(valor_piores_top_5)

        self.assertEqual(bd.top_5("soma"), valor_soma_top_5)
        self.assertEqual(bd.top_5_piores("soma"), valor_soma_piores_top_5)

        
        valor_estats_1 = [[bd.soma_placares(),
                           bd.media_placares(),
                           valor_soma_top_5,
                           valor_soma_piores_top_5,
                           ]]

        valor_estats_2 = [[valor_top_5[x], valor_piores_top_5[x]] for x in range(len(valor_top_5))]

        resultado = bd.printa_tabela_2()

        self.assertEqual(resultado[0], valor_estats_1)
        self.assertEqual(resultado[1], valor_estats_2)        
        
        bd.encerra()
        self.deleta_BD()



if __name__ == "__main__":
    unittest.main()
