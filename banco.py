import sqlite3

class BD():
    def __init__(self, nome_banco, temporada = 2020):
        self.conexao = sqlite3.connect(f"BDs\\{nome_banco}")
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
        self.cursor.execute(f"SELECT rowid, * FROM {self.tabela}")
        itens = self.cursor.fetchall()
        colunas = ["JOGO", "PLACAR", "MÍNIMO DA TEMPORADA", "MÁXIMO DA TEMPORADA", "QUEBRA RECORDE MÍN.", "QUEBRA RECORDE MÁX."]

        return itens, colunas

    def retorna_tabela(self, tipo):
        if tipo == "última linha":
            self.cursor.execute(f"SELECT * FROM {self.tabela} ORDER BY rowid DESC LIMIT 1")
            itens = self.cursor.fetchall()[0]

        if tipo == "inteira":
            self.cursor.execute(f"SELECT rowid, * FROM {self.tabela}")
            itens = self.cursor.fetchall()

        return itens

    def add_placar_1(self, placar):
        self.cursor.execute(f"INSERT INTO {self.tabela} VALUES (?,?,?,?,?)", (placar, placar, placar, 0, 0))
        self.conexao.commit()

    def add_placar_2(self, lista, tipo):
        placar, placar_min, placar_max, quebra_min, quebra_max = lista[0], lista[1], lista[2], lista[3], lista[4]
        
        if tipo == "novo mínimo":
            self.cursor.execute(f"INSERT INTO {self.tabela} VALUES (?,?,?,?,?)", (placar, placar, placar_max, quebra_min, quebra_max))

        elif tipo == "novo máximo":
            self.cursor.execute(f"INSERT INTO {self.tabela} VALUES (?,?,?,?,?)", (placar, placar_min, placar, quebra_min, quebra_max))

        else:
            self.cursor.execute(f"INSERT INTO {self.tabela} VALUES (?,?,?,?,?)", (placar, placar_min, placar_max, quebra_min, quebra_max))

        self.conexao.commit()
