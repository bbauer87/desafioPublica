__author__ = "Bruno Silveira Bauer"
__version__ = "1.0.1"

import sqlite3


class BD:
    '''
    Classe que modela o banco de dados.
    '''
    
    def __init__(self, caminho_banco):
        '''
        Parâmetro:
        ----------
        caminho_banco : str
            Indica o caminho do banco de dados a ser conectado ou criado.
        '''

        try:
            self.conexao = sqlite3.connect(caminho_banco)
            self.cursor = self.conexao.cursor()

            print(">>> Conexão realizada em ", caminho_banco)

        except Exception as e:
            print(f"\nErro fatal na conexão com o BD!\n\n")
            print(e)
            quit()


    def define_tabela(self, temporada):
        '''
        Parâmetro:
        ----------
        temporada : str
            Indica a tabela que será usada para querys no BD.
        '''
        
        self.tabela = f"temporada_{temporada}"

        print(f">>> Definida tabela {self.tabela}")

        try:
            self.cursor.execute(f"SELECT * FROM {self.tabela}")

        except sqlite3.OperationalError:
            self.cria_tabela()


    def cria_tabela(self):
        '''
        Método que cria uma tabela com cinco colunas, caso não exista no BD.
        '''
        
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.tabela} (
                          placar INTEGER NOT NULL,
                          min_temporada INTEGER NOT NULL,
                          max_temporada INTEGER NOT NULL,
                          quebra_min INTEGER NOT NULL,
                          quebra_max INTEGER NOT NULL)""")

        self.conexao.commit()

    def verifica_tabelas(self):
        '''
        Método que retorna uma lista com as tabelas que constam no BD.
        '''
        
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

        return self.cursor.fetchall()

    def deleta_tabela(self, tabela):  
        '''
        Parâmetro:
        ----------
        tabela : str
            Indica a tabela que será deletada no BD.
        '''
        
        self.cursor.execute(f"DROP TABLE {tabela}")
        self.conexao.commit()

    def encerra(self):
        '''
        Método que encerra o cursor e a conexão com o BD.
        '''
        
        self.cursor.close()
        self.conexao.close()

    def printa_tabela(self): 
        '''
        Método que retorna a tabela inteira bem como uma lista de colunas, para
        que a visão CLI efetue print.
        '''
               
        colunas = ["JOGO", "PLACAR", "MÍNIMO DA TEMPORADA", "MÁXIMO DA TEMPORADA", "QUEBRA RECORDE MÍN.", "QUEBRA RECORDE MÁX."]

        return self.retorna_tabela("inteira"), colunas

    def retorna_tabela(self, tipo):
        '''
        Parâmetro:
        ----------
        tipo : str
            Indica que tipo de dado sobre a tabela que será retornado:
            ou a tabela inteira, ou apenas a última linha.
        '''
        
        if tipo == "última linha":
            self.cursor.execute(f"SELECT rowid, * FROM {self.tabela} ORDER BY rowid DESC LIMIT 1")

        if tipo == "inteira":
            self.cursor.execute(f"SELECT rowid, * FROM {self.tabela}")

        return self.cursor.fetchall()

    def adiciona_placar(self, lista_ou_int, tipo):
        '''
        Parâmetros:
        ----------
        lista_ou_int : list ou int
            Indica qual placar será adicionado na tabela. Caso seja o primeiro jogo,
            o valor é int; caso contrário, será uma lista com os cinco valores a serem
            adicionados na nova linha da tabela.
            
        tipo : str
            Indica que tipo de inserção será feita na tabela: se houve um novo placar
            máximo ou mínimo, se é um placar normal ou se é o primeiro jogo.
        '''
        
        if type(lista_ou_int) == list:
            placar, placar_min, placar_max, quebra_min, quebra_max = lista_ou_int
        
        if tipo == "novo mínimo":
            valores = (placar, placar, placar_max, quebra_min, quebra_max)

        elif tipo == "novo máximo":
            valores = (placar, placar_min, placar, quebra_min, quebra_max)

        elif tipo == "normal":
            valores = (placar, placar_min, placar_max, quebra_min, quebra_max)
            
        else:
            valores = (lista_ou_int, lista_ou_int, lista_ou_int, 0, 0)

        self.cursor.execute(f"INSERT INTO {self.tabela} VALUES (?,?,?,?,?)", valores)
        self.conexao.commit()


    def soma_placares(self):
        '''
        Método que retorna a soma dos placares da tabela usando o método SUM do SQLite.
        '''
            
        self.cursor.execute(f"SELECT SUM(placar) FROM {self.tabela}")

        return self.cursor.fetchall()[0][0]


    def media_placares(self):
        '''
        Método que retorna a média dos placares da tabela usando o método AVG do SQLite.
        '''
            
        self.cursor.execute(f"SELECT AVG(placar) FROM {self.tabela}")

        return self.cursor.fetchall()[0][0]
        

    def top_5(self, tipo):
        '''
        Método que retorna os cinco melhores placares da tabela.
        
        Parâmetro:
        ----------
        tipo : str
            Indica se o retorno deve ser em forma de lista ou de soma dos valores.
        '''
            
        self.cursor.execute(f"SELECT placar FROM {self.tabela} ORDER BY placar DESC LIMIT 5")
        
        if tipo == "soma":
            return sum([x[0] for x in self.cursor.fetchall()])            

        else:
            return [x[0] for x in self.cursor.fetchall()]
        

    def top_5_piores(self, tipo):
        '''
        Método que retorna os cinco piores placares da tabela.
        
        Parâmetro:
        ----------
        tipo : str
            Indica se o retorno deve ser em forma de lista ou de soma dos valores.
        '''
            
        self.cursor.execute(f"SELECT placar FROM {self.tabela} ORDER BY placar LIMIT 5")

        if tipo == "soma":
            return sum([x[0] for x in self.cursor.fetchall()])            

        else:
            return [x[0] for x in self.cursor.fetchall()]


    def printa_tabela_2(self):
        '''
        Método que retorna quatro listas.

        A primeira contém a média dos placares e as somas dos placares gerais, dos
        cinco melhores e dos cinco piores; a segunda lista contém listas dos melhores
        e piores placares; as duas últimas listas são compostas dos nomes das colunas,
        para que a visão CLI efetue print.
        '''
            
        estatisticas_1 = [[self.soma_placares(),
                          self.media_placares(),
                          self.top_5("soma"),
                          self.top_5_piores("soma")]]

        estatisticas_2 = []
        t5 = self.top_5("lista")
        t5_piores = self.top_5_piores("lista")

        for x in range(len(t5)):
            estatisticas_2.append([t5[x], t5_piores[x]])
        
        colunas_1 = ["SOMA DOS PLACARES", "MÉDIA DOS PLACARES", "SOMA DO TOP 5 PLACARES", "SOMA DO TOP 5 PIORES PLACARES"]
        colunas_2 = ["TOP 5 PLACARES", "TOP 5 PIORES PLACARES"]

        return estatisticas_1, estatisticas_2, colunas_1, colunas_2
