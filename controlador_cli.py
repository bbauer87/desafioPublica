import os

from datetime import datetime

from banco import BD
from cli import Cli


        
    


class ControladorCli:
    def __init__(self):
        self.busca_bds()
        self.cli()


    def busca_bds(self):
        self.diretorio = os.path.dirname(__file__) + "\\BD\\"        
        self.bancos = [file for file in os.listdir(self.diretorio) if file.endswith(".db")]


    def cli(self):
        self.visao = Cli(self.bancos)
        nome_bd, temporada = self.visao.escolhe_banco()

        try:##verif de excessao em conexao com banco tem q ser na classe do banco, nao?
            if nome_bd in self.bancos:
                bd = BD(self.diretorio + nome_bd)## aki tem q descobrir nome da tabela do bd.. ex, se tenho bd bruno com uma unica tabela chamada vitiligo, qndo for pro construtor do jeito q ta vai criar uma tab vazia chamada 2020, pois eh parametro do construtor!!!!!!! dai vitiliga neh cumpadi
            else:
                bd = BD(self.diretorio + nome_bd, temporada)
                
        except Exception as e:
            print(f"\nErro fatal na conexão com o BD '{nome_bd}'!\n\n")
            print(e)
            quit()

        while True:
            escolha_menu, parametro = self.visao.menu(nome_bd, bd.tabela)
            if "Sair" in escolha_menu:
                quit()

            elif "Consultar outras estatísticas" in escolha_menu:
                estats_1, estats_2, colunas_1, colunas_2 = bd.printa_tabela_2()               
                self.visao.consultar_tabela(estats_1, colunas_1)
                self.visao.consultar_tabela(estats_2, colunas_2)

            elif "Alterar BD" in escolha_menu:
                self.busca_bds()
                self.bancos.remove(nome_bd)#remove da lista de bancos possiveis de alterar o q esteja em uso ;)
                if len(self.bancos) < 1:
                    escolha = self.visao.opcoes_BD("abortar", escolha_menu)

                else:                    
                    escolha = self.visao.opcoes_BD(self.bancos, escolha_menu)
                
                if "Sair" not in escolha:
                    bd.encerra()
                    bd = BD(self.diretorio + escolha)
                    nome_bd = escolha
                    temporada = datetime.now().year
                
            elif "Deletar BD" in escolha_menu:
                self.busca_bds()
                self.bancos.remove(nome_bd)#remove da lista de bancos possiveis de deletar o q esteja em uso ;)
                
                if len(self.bancos) < 1:
                    escolha = self.visao.opcoes_BD("abortar", escolha_menu)
                    
                else:                    
                    escolha = self.visao.opcoes_BD(self.bancos, escolha_menu)
                    
                    if "Sair" not in escolha:                        
                        if os.path.isfile(self.diretorio + escolha):
                            os.remove(self.diretorio + escolha)

            elif "Deletar temporada" in escolha_menu:
                escolha = self.visao.deletar_temporada(bd.verifica_tabelas(), parametro)
                if "Sair" not in escolha:
                    bd.deleta_tabela(escolha)                    

            elif "Alterar/Criar temporada" in escolha_menu:
                escolha, temporada = self.visao.alterar_temporada(bd.verifica_tabelas(), bd.tabela)

                if "Criar nova temporada" in escolha:
                    bd.tabela = f"temporada_{temporada}"
                    bd.cria_tabela()

                elif "temporada_" in escolha:
                    bd.tabela = escolha
                
            elif "Consultar estatísticas" in escolha_menu:
                dados = bd.printa_tabela()
                self.visao.consultar_tabela(dados[0], dados[1])

            elif "Adicionar um jogo" in escolha_menu:
                itens_serie = bd.retorna_tabela("inteira")
                
                if len(itens_serie) > 0:                 
                    ultima_linha = bd.retorna_tabela("última linha")[0][2:]
                    placar_min, placar_max, quebra_min, quebra_max = ultima_linha
                    
                    tipo = "normal"

                    if parametro < placar_min:
                        tipo = "novo mínimo"
                        quebra_min += 1
                        print("Um novo placar mínimo na temporada foi registrado!")
                        
                    elif parametro > placar_max:
                        tipo = "novo máximo"
                        quebra_max += 1                        
                        print("Um novo placar máximo na temporada foi registrado!")

                    bd.adiciona_placar([parametro, placar_min, placar_max, quebra_min, quebra_max], tipo)

                else:                  
                    bd.adiciona_placar(parametro, "primeiro jogo")


