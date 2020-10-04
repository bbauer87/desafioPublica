__author__ = "Bruno Silveira Bauer"
__version__ = "1.0.1"

import os
from datetime import datetime

from banco import BD
from cli import Cli



class ControladorCli:
    '''
    Classe que atua como controlador do programa quando a interface é por linha de comando.
    '''
    
    def __init__(self):
        '''
        A classe inicializa dois métodos.

        O primeiro faz uma busca pelos bancos de dados no diretório do programa;
        O segundo inicia a visão CLI.
        '''
        
        self.busca_bds()
        self.cli()


    def busca_bds(self):
        '''
        Método que faz uma busca pelos bancos de dados no diretório do programa
        '''
        
        self.diretorio = os.path.dirname(__file__) + "\\BD\\"        
        self.bancos = [file for file in os.listdir(self.diretorio) if file.endswith(".db")]


    def cli(self):
        '''
        Método que inicia a visão CLI.

        Cria uma instância da classe Cli enviando a lista de BDs encontrados no diretório.
        O usuário escolhe um BD e uma temporada para iniciar o programa.
        
        Em seguida inicia-se um laço que recebe instruções do usuário e executa ações no
        BD modelado pelo script banco.py
        '''
        
        def escolha_tabela():
            '''
            Função invocada para que se defina uma temporada.

            Caso haja mais de uma, a visão mostra ao usuário opções de escolha;
            Caso haja apenas uma, esta temporada é escolhida;
            Caso não haja nenhuma, é criada uma temporada com numeração do ano atual.
            '''
            
            tabelas = bd.verifica_tabelas()
            tabelas = [x[0] for x in tabelas]

            if len(tabelas) > 1:
                temporada = self.visao.escolhe_temporada(tabelas).replace("temporada_", "")

            elif len(tabelas) == 1:
                temporada = tabelas[0].replace("temporada_", "")

            else:
                temporada = datetime.now().year

            return temporada
        
        self.visao = Cli(self.bancos)
        nome_bd, temporada = self.visao.escolhe_banco()

        bd = BD(self.diretorio + nome_bd)
        
        if temporada == 0:
            temporada = escolha_tabela()
            
        bd.define_tabela(temporada)
  
        while True:
            escolha_menu, parametro = self.visao.menu(nome_bd, bd.tabela)
            if "Sair" in escolha_menu:
                bd.encerra()
                quit()

            elif "Consultar outras estatísticas" in escolha_menu:
                estats_1, estats_2, colunas_1, colunas_2 = bd.printa_tabela_2()               
                self.visao.consultar_tabela(estats_1, colunas_1)
                self.visao.consultar_tabela(estats_2, colunas_2)

            elif "Alterar BD" in escolha_menu:
                self.busca_bds()
                self.bancos.remove(nome_bd)
                if len(self.bancos) < 1:
                    escolha = self.visao.opcoes_BD("abortar", escolha_menu)

                else:                    
                    escolha = self.visao.opcoes_BD(self.bancos, escolha_menu)
                
                if "Sair" not in escolha:
                    bd.encerra()
                    bd = BD(self.diretorio + escolha)
                    nome_bd = escolha
                    
                    temporada = escolha_tabela()
                    bd.define_tabela(temporada)
                
            elif "Deletar BD" in escolha_menu:
                self.busca_bds()
                self.bancos.remove(nome_bd)
                
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
                        print("Um novo placar mínimo foi registrado na temporada!")
                        
                    elif parametro > placar_max:
                        tipo = "novo máximo"
                        quebra_max += 1                        
                        print("Um novo placar máximo foi registrado na temporada!")

                    bd.adiciona_placar([parametro, placar_min, placar_max, quebra_min, quebra_max], tipo)

                else:                  
                    bd.adiciona_placar(parametro, "primeiro jogo")


