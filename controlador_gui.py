import os
from sys import argv
from datetime import datetime


from banco import BD







class ControladorGui:    
    def __init__(self):
        self.busca_bds()


    def busca_bds(self):
        self.diretorio = os.path.dirname(__file__) + "\\BD\\"        
        self.bancos = [file for file in os.listdir(self.diretorio) if file.endswith(".db")]


    def conecta(self, nome_bd, tabela = ""):
        self.bd = BD(nome_bd)

    def encerra(self):
        self.bd.encerra()

    def altera_cria_bd(self, param):#nome_bd, temporada
        self.encerra()

        print("param -> ", param)#deletar
        
##        if ".db" not in param[0]:
##            param[0] = param[0] + ".db"
            
        self.conecta(f".\\BD\\{param[0]}")
        if param[1] != None:
            
            print("bitchlili")#deletar!
            
            self.tabela("escolhe", param[1])
            return param[1]
##            self.bd.define_tabela(param[1])

        else:
            try:
                print("blimbert")#deletar!
                self.tabela("escolhe", self.tabela("consulta")[0])
                return self.tabela("consulta")[0]

            except:
                print("cacarymert!!!")#deletar!
                self.tabela("escolhe", str(datetime.now().year))
                return str(datetime.now().year)
                
            

    def tabela(self, tipo, param = ""):
        if tipo == "consulta":
            return [x[0].replace("temporada_", "") for x in self.bd.verifica_tabelas()]

        if tipo == "escolhe":
            self.bd.define_tabela(param)

    def retorna_dados(self):#, tabela):
##        try:
##            self.bd.tabela
##        except AttributeError:
##            self.bd.define_tabela(tabela)
            
        return self.bd.retorna_tabela("inteira"), self.bd.top_5("lista"), self.bd.top_5_piores("lista"), self.bd.soma_placares()

    def altera_cria_temp(self, etapa, param = ""):
        if etapa == "inicial":
            tabelas = self.bd.verifica_tabelas()
            print("altera_cria_temp -> ", tabelas)#deletar
            tabelas = [x[0] for x in tabelas] 
            tabelas.remove(self.bd.tabela)

            return tabelas, self.bd.tabela

        if etapa == "criação":            
            self.bd.tabela = f"temporada_{param}"
            self.bd.cria_tabela()

        if etapa == "alterar":    
            self.bd.tabela = param
            


    def deletar(self, etapa, param = ""):
##        if etapa == "verificação":
##            return self.altera_cria_temp("inicial")

        if etapa == "deletar temporada":
            print("param delet temp-> ", param)#deletar
            self.bd.deleta_tabela(param)

            
        if etapa == "deletar BD":
            print("param delet bd-> ", param)#deletar
            
            if os.path.isfile(self.diretorio + param):
                os.remove(self.diretorio + param)
            
            
        

    def add_placar(self, placar):
##        placar = int(placar)
        tipo = "normal"

        if len(self.bd.retorna_tabela("inteira")) > 0:                 
            ultima_linha = self.bd.retorna_tabela("última linha")[0][2:]
            placar_min, placar_max, quebra_min, quebra_max = ultima_linha            

            if placar < placar_min:
                tipo = "novo mínimo"
                quebra_min += 1
                
            elif placar > placar_max:
                tipo = "novo máximo"
                quebra_max += 1

            self.bd.adiciona_placar([placar, placar_min, placar_max, quebra_min, quebra_max], tipo)

        else:          
            self.bd.adiciona_placar(placar, "primeiro jogo")

        return tipo

