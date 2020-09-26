import sqlite3

class BD():
    def __init__(self, caminho_banco, temporada = 2020):
        self.conexao = sqlite3.connect(caminho_banco)
        self.cursor = self.conexao.cursor()
        self.tabela = f"temporada_{temporada}"

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
