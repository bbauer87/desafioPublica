import sqlite3
##from datetime import datetime

class BD:
    def __init__(self, caminho_banco):#, temporada = datetime.now().year):

        try:
            self.conexao = sqlite3.connect(caminho_banco)
            self.cursor = self.conexao.cursor()

            print("Conexão realizada em ", caminho_banco)

        except Exception as e:
            print(f"\nErro fatal na conexão com o BD '{nome_bd}'!\n\n")
            print(e)
            quit()


    def define_tabela(self, temporada):#criar test unit
        self.tabela = f"temporada_{temporada}"

        print(f"definida tabela {self.tabela}")

        try:
            self.cursor.execute(f"SELECT * FROM {self.tabela}")

        except sqlite3.OperationalError:
            self.cria_tabela()


    def cria_tabela(self):        
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.tabela} (
                          placar INTEGER NOT NULL,
                          min_temporada INTEGER NOT NULL,
                          max_temporada INTEGER NOT NULL,
                          quebra_min INTEGER NOT NULL,
                          quebra_max INTEGER NOT NULL)""")

        self.conexao.commit()

    def verifica_tabelas(self):#tem q fazer test unit
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

        return self.cursor.fetchall()

    def deleta_tabela(self, tabela):   #tem q fazer test unit     
        self.cursor.execute(f"DROP TABLE {tabela}")
        self.conexao.commit()

    def encerra(self):
        self.cursor.close()
        self.conexao.close()

    def printa_tabela(self):        
        colunas = ["JOGO", "PLACAR", "MÍNIMO DA TEMPORADA", "MÁXIMO DA TEMPORADA", "QUEBRA RECORDE MÍN.", "QUEBRA RECORDE MÁX."]

        return self.retorna_tabela("inteira"), colunas

    def retorna_tabela(self, tipo):
        if tipo == "última linha":
            self.cursor.execute(f"SELECT rowid, * FROM {self.tabela} ORDER BY rowid DESC LIMIT 1")

        if tipo == "inteira":
            self.cursor.execute(f"SELECT rowid, * FROM {self.tabela}")

        return self.cursor.fetchall()

    def adiciona_placar(self, lista_ou_int, tipo):
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


    def soma_placares(self):#fazer td test unit
        self.cursor.execute(f"SELECT SUM(placar) FROM {self.tabela}")

        return self.cursor.fetchall()[0][0]


    def media_placares(self):#fazer td test unit
        self.cursor.execute(f"SELECT AVG(placar) FROM {self.tabela}")

        return self.cursor.fetchall()[0][0]
        

    def top_5(self, tipo):#fazer td test unit
        self.cursor.execute(f"SELECT placar FROM {self.tabela} ORDER BY placar DESC LIMIT 5")
        
        if tipo == "soma":
            return sum([x[0] for x in self.cursor.fetchall()])            

        else:
            return [x[0] for x in self.cursor.fetchall()]
        

    def top_5_piores(self, tipo):#fazer td test unit
        self.cursor.execute(f"SELECT placar FROM {self.tabela} ORDER BY placar LIMIT 5")

        if tipo == "soma":
            return sum([x[0] for x in self.cursor.fetchall()])            

        else:
            return [x[0] for x in self.cursor.fetchall()]


    def printa_tabela_2(self):
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
