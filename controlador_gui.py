__author__ = "Bruno Silveira Bauer"
__version__ = "1.0.1"

import os
from sys import argv
from datetime import datetime


from banco import BD



class ControladorGui:    
    '''
    Classe que atua como controlador do programa quando se utiliza interface gráfica.
    '''
    
    def __init__(self):
        '''
        A classe inicializa o método "busca_bds" para que se tenha uma lista de BDs.
        '''
        
        self.busca_bds()


    def busca_bds(self):
        '''
        Método que faz uma busca pelos bancos de dados no diretório do programa
        '''
        
        self.diretorio = os.path.dirname(__file__) + "\\BD\\"        
        self.bancos = [file for file in os.listdir(self.diretorio) if file.endswith(".db")]


    def conecta(self, nome_bd):
        '''
        Método que inicia uma conexão com o BD.
        
        Parâmetro:
        ----------
        nome_bd : str
            Nome do BD a ser conectado.
        '''
        
        self.bd = BD(nome_bd)
        

    def encerra(self):
        '''
        Método que encerra uma conexão com o BD.
        '''
        
        self.bd.encerra()
        

    def altera_cria_bd(self, param):
        '''
        Método que altera ou cria um BD.

        Primeiro encerra a atual conexão e então cria uma nova com base nos
        parâmetros recebidos. Em seguida, define qual tabela será usada no
        BD.

        Retorna para interface gráfica informações para que possam ser definidas
        as variáveis globais relativas aos nomes do BD e da temporada em uso
        no script gui.py.
        
        Parâmetro:
        ----------
        param : list
            Lista que contem o nome do banco e a numeração da temporada.
        '''
        
        self.encerra()            
        self.conecta(f".\\BD\\{param[0]}")
        
        if param[1] != None:            
            self.tabela("escolhe", param[1])
            return param[1]

        else:
            try:
                self.tabela("escolhe", self.tabela("consulta")[0])
                return self.tabela("consulta")[0]

            except:
                self.tabela("escolhe", str(datetime.now().year))
                return str(datetime.now().year)               
            

    def tabela(self, tipo, param = ""):
        '''
        Método que consulta as tabelas do BD ou define uma.

        Se o tipo escolhido for "consulta", retorna uma lista das temporadas
        existentes no BD.

        Parâmetros:
        ----------
        tipo : str
            Qual tipo de ação o método deve executar.
            
        param : str (opcional)
            Parâmetro relativo a numeração da temporada.
        '''
        
        if tipo == "consulta":
            return [x[0].replace("temporada_", "") for x in self.bd.verifica_tabelas()]

        if tipo == "escolhe":
            self.bd.define_tabela(param)
            

    def retorna_dados(self):
        '''
        Método para retornar dados da tabela ativa no BD.

        Retorna:
        uma lista com a tabela inteira;
        duas listas, uma com os cinco melhores e outra com os
        cinco piores placares registrados;
        a soma dos placares registrados.
        '''
        
        return self.bd.retorna_tabela("inteira"), self.bd.top_5("lista"), self.bd.top_5_piores("lista"), self.bd.soma_placares()


    def altera_cria_temp(self, etapa, param = ""):
        '''
        Método que fornece informações ou executa ações na tabela ativa no BD.

        O método pode retornar à interface GUI uma lista com as tabelas ativas bem
        como o nome da atual tabela em uso.
        
        Parâmetros:
        ----------
        etapa : str
            Indica ao método qual tipo de ação a executar.

        param : str (opcional)
            Parâmetro relativo a numeração da temporada.
        '''
        
        if etapa == "inicial":
            tabelas = self.bd.verifica_tabelas()
            tabelas = [x[0] for x in tabelas] 
            tabelas.remove(self.bd.tabela)

            return tabelas, self.bd.tabela

        if etapa == "criação":            
            self.bd.tabela = f"temporada_{param}"
            self.bd.cria_tabela()

        if etapa == "alterar":    
            self.bd.tabela = param
            

    def deletar(self, etapa, param = ""):
        '''
        Método que possibilita deletar um BD ou uma temporada.
        
        Parâmetros:
        ----------
        etapa : str
            Indica ao método qual tipo de ação a executar.

        param : str (opcional)
            Parâmetro relativo a numeração da temporada.
        '''

        if etapa == "deletar temporada":
            self.bd.deleta_tabela(param)

            
        if etapa == "deletar BD":            
            if os.path.isfile(self.diretorio + param):
                os.remove(self.diretorio + param)
            

    def add_placar(self, placar):
        '''
        Método que envia da interface gráfica ao BD o placar a ser adicionado.

        Efetua verificações se o novo placar quebra os recordes mínimos ou máximos
        da temporada.

        Retorna à interface o tipo de inserção na tabela:
        se gerou um novo placar máximo;
        se gerou um novo placar mínimo;
        se não gerou nenhuma quebra de recorde;
        se foi o primeiro jogo da tabela.
        
        Parâmetro:
        ----------
        placar : int
            Qual o placar a ser adicionado na tabela.
        '''
        
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

