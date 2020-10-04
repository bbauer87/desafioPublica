__author__ = "Bruno Silveira Bauer"
__version__ = "1.0.1"

from tabulate import tabulate
from pathvalidate import is_valid_filename



class Cli:
    '''
    Classe que atua como visão quando o programa é inicializado em linha de comando.
    '''
    
    def __init__(self, bancos):
        '''
        Parâmetro:
        ----------
        bancos : list
            Lista de bancos de dados localizados no diretório do programa.
        '''

        self.bancos = bancos[:]


    def escolhe_temporada(self, lista):
        '''
        Método que escolhe uma temporada
        
        Parâmetro:
        ----------
        lista : list
            Lista de temporadas localizadas em um BD.
        '''

        print(f"\nO BD escolhido tem {len(lista)} temporadas. Escolha uma:\n")

        self.lista_opcoes(lista)

        return lista[self.entrada_int(len(lista)) - 1]


    def escolhe_banco(self):
        '''
        Método em que usuário cria ou escolhe um BD.

        Retorna o nome do BD escolhido bem como a variável "temporada", que pode
        ou ser setada pelo usuário ou pode ser um valor inválido, que indicará
        ao controlador_cli.py que deve ser executada uma busca por temporadas no
        BD escolhido.
        '''

        temporada = 0
        
        if self.bancos:
            print("\nEscolha um banco de dados:\n")
            if "Criar um novo BD" not in self.bancos:
                self.bancos.append("Criar um novo BD")

            self.lista_opcoes(self.bancos)
            
            nome_bd = self.bancos[self.entrada_int(len(self.bancos)) - 1]
            if "Criar um novo BD" in nome_bd:
                print("\nDigite um nome para criarmos o BD:\n")
                nome_bd = self.entrada_str()
                print("\nAgora digite um valor inteiro positivo para numerar a temporada (limite 10000):\n")
                temporada = self.entrada_int(10000)

        else:
            print("\nNão foi localizado nenhum banco de dados. Insira um nome para criarmos o BD:\n")
            nome_bd = self.entrada_str()
            print("\nAgora digite um valor inteiro positivo para numerar a temporada (limite 10000):\n")
            temporada = self.entrada_int(10000)

        return nome_bd, temporada


    def entrada_str(self):
        '''
        Método em que usuário efetua uma entrada cujo retorno será uma string.

        Possui consistência ao verificar se foi utilizado algum caracter inválido
        utilizando-se da biblioteca pathvalidate.
        '''

        while True:
            print("\n" + "-" * 100 + "\n")  
            resposta = input("\n>>> ")    
            if not resposta:
                print("\nDigite algo!!\n")
                continue
            if not is_valid_filename(resposta):
                print("\nNão é possível usar os seguites caracteres: :, *, /, \", ?, >, |, <, \\. Tente novamente!\n")
                continue
            break
            
        print("\n" + "-" * 100 + "\n")
        return resposta + ".db"

        
    def entrada_int(self, limite):
        '''
        Método em que usuário efetua uma entrada cujo retorno será um int.

        Possui consistência ao verificar caracter inválido e se o placar a adicionar
        está dentro dos limites estabelecidos pelo enunciado do desafio.
        '''
        
        while True:
            print("\n" + "-" * 100 + "\n")            
            resposta = input("\n>>> ")
            if not resposta.isdigit() or (int(resposta) < 1 or int(resposta) > limite):
                print("\nOpção inválida! Tente de novo!\n")
                continue
            break
            
        print("\n" + "-" * 100 + "\n")
        return int(resposta)


    def lista_opcoes(self, lista):
        '''
        Método que imprime com numeração o parâmetro "lista".
        
        Parâmetro:
        ----------
        lista : list
            Lista com os itens a serem impressos com numeração.
        '''
        
        for x, y in enumerate(lista):
            print(f" [{x + 1}] - {y}")


    def consultar_tabela(self, itens, colunas):
        '''
        Método que utiliza a biblioteca "tabulate" para imprimir a tabela de
        maneira organizada.

        Parâmetros:
        ----------
        itens : list
            Lista com os dados de cada linha.

        colunas : list
            Lista com os nomes das colunas da tabela.
        '''
        
        print(tabulate(itens, colunas, numalign = "center", tablefmt = "grid"))
        print("\n\n")


    def verif_tabela_existente(self, lista):
        '''
        Método responsável por verificar se usuário inseriu uma numeração de
        temporada que já exista.

        Retorna "False" caso já exista ou o número da temporada caso contrário.

        Parâmetros:
        ----------
        lista : list
            Lista com as temporadas do BD.
        '''
        
        if "Criar nova temporada" in lista:
            lista.remove("Criar nova temporada")

        temporada = self.entrada_int(10000)
        for x in lista:
            if str(temporada) == x.replace("temporada_", ""):
                return False

        return temporada
        

    def alterar_temporada(self, lista, tabela_atual):   
        '''
        Método responsável por alterar e criar uma temporada ativa no sistema.

        Retorna a escolha do usuário (criar ou alterar a temporada) e a temporada
        escolhida ou o parâmetro "Abortar", indicando ao controlador que não será
        alterada a temporada.

        Parâmetros:
        ----------
        lista : list
            Lista com as temporadas do BD.

        tabela_atual : str
            Nome da temporada atual.
        '''
             
        temporada = 0
        opcoes = [x[0] for x in lista]        
        opcoes.remove(tabela_atual)
        
        if len(opcoes) < 1:
            print("\nNo BD atual consta apenas uma temporada... Deseja criar uma nova?\n")
            opcoes = ["Sim", "Não"]
            self.lista_opcoes(opcoes)
            
            if "Sim" in opcoes[self.entrada_int(len(opcoes)) - 1]:
                escolha = "Criar nova temporada"
                print("\nDigite um valor inteiro positivo para numerar a temporada (limite 10000):\n")
                validacao = self.verif_tabela_existente(opcoes)
                
                if validacao == False:
                    escolha = "Abortar"
                    print("\nErro! O número escolhido para a temporada já consta no BD.\n")
                else:
                    temporada = validacao
                    print(f"\nCriada nova temporada {temporada}!\n")

            else:
                escolha = "Abortar"
                print("\nNão foi criada nova temporada...\n")

        else:            
            opcoes.append("Criar nova temporada")
            opcoes.append("Sair")
            
            print("Escolha uma opção:\n")
            self.lista_opcoes(opcoes)

            escolha = opcoes[self.entrada_int(len(opcoes)) - 1]

            if "Sair" in escolha:
                print("\nRetornando ao menu...\n")

            elif "Criar nova temporada" in escolha:
                print("\nDigite um valor inteiro positivo para numerar a temporada (limite 10000):\n")
                validacao = self.verif_tabela_existente(opcoes)
                
                if validacao == False:
                    escolha = "Abortar"
                    print("\nErro! O número escolhido para a temporada já consta no BD.\n")
                else: 
                    temporada = validacao
                    print(f"\nCriada nova temporada: {temporada}!\n")

            else:
                print(f"\nAlterada temporada: {escolha}\n")

        return escolha, temporada


    def deletar_temporada(self, lista, tabela_atual):   
        '''
        Método responsável por deletar uma temporada no sistema.
        Se o BD tiver apenas uma temporada, o sistema impede o usuário
        de deletá-la.

        Retorna a escolha do usuário se realmente deleta ou não a temporada.

        Parâmetros:
        ----------
        lista : list
            Lista com as temporadas do BD.

        tabela_atual : str
            Nome da temporada atual.
        '''
        
        lista = [x[0] for x in lista]
        lista.remove(tabela_atual)
        
        if len(lista) < 1:
            print("\nSó há uma temporada no sistema, não sendo possível deletá-la pois está em uso. Crie uma nova temporada e tente novamente.")
            return "Sair"
        
        lista.append("Sair")
        self.lista_opcoes(lista)
        escolha = lista[self.entrada_int(len(lista)) - 1]

        if "Sair" in escolha:
            print("\nNão foi deletada nenhuma temporada...\n")
            
        else:
            print(f"\nTem certeza que quer deletar {escolha}? Esse processo não pode ser revertido caso confirmado!\n")
            opcoes = ["Sim", "Não"]
            self.lista_opcoes(opcoes)

            if "Sim" in opcoes[self.entrada_int(len(opcoes)) - 1]:
                print(f"\nFoi deletada {escolha} do BD!!!\n")
                
            else:
                escolha = "Sair"
                print("\nNão foi deletada nenhuma temporada...\n")

        return escolha


    def opcoes_BD(self, lista_ou_str, tipo):
        '''
        Método responsável por alterar ou deletar um BD.

        Retorna a escolha do usuário se realmente deleta ou não o BD.
        Caso haja apenas um BD no diretório, o programa impede o usuário
        de deletá-lo.

        Parâmetros:
        ----------
        lista_ou_str : list ou str
            Lista com os BDs localizados no diretório ou uma string
            "abortar".

        tipo : str
            Nome da função a ser executada: alterar ou deletar BD.
        '''
        
        if type(lista_ou_str) == list:
            lista_ou_str.append("Sair")
        
        if tipo == "Alterar BD":
            if "abortar" in lista_ou_str:
                print("\nNão é possível alterar o BD pois consta somente um...\n")
                return "Sair"
            
            print("\nAlterar para qual BD?\n")
            self.lista_opcoes(lista_ou_str)
            escolha = lista_ou_str[self.entrada_int(len(lista_ou_str)) - 1]

        if tipo == "Deletar BD":
            if lista_ou_str == "abortar":
                print("Não foi localizado outro BD no sistema, por isso não será possível deletar o BD em uso!")
                return "Sair"
            
            print("\nAtenção! A exclusão do BD é irreversível!!\n\nAviso: não é possível deletar um BD que esteja em uso.\n")
            print("\nDeletar qual BD?\n")
            self.lista_opcoes(lista_ou_str)

            escolha = lista_ou_str[self.entrada_int(len(lista_ou_str)) - 1]

            if "Sair" in escolha:
                print("\nNão foi deletado nenhum BD...\n")

            else:                
                print(f"\nTem certeza que quer deletar {escolha}?\n")
                opcoes = ["Sim", "Não"]
                self.lista_opcoes(opcoes)

                if "Sim" in opcoes[self.entrada_int(len(opcoes)) - 1]:
                    print(f"\nFoi deletado o BD {escolha}!!!\n")
                    
                else:
                    escolha = "Sair"
                    print("\nNão foi deletado nenhum BD...\n")

        return escolha
       

    def menu(self, nome_bd, tabela):
        '''
        Método que imprime um menu com opções para o usuário.

        Retorna ao controlador a escolha do usuário bem como um eventual
        parâmetro, como nos casos de adicionar placar ou ao deletar uma
        temporada.

        Parâmetros:
        ----------
        nome_bd : str
            Nome do BD em uso, pois será impresso no topo do menu.

        tabela : str
            Nome da temporada em uso, que também será impressa no menu.

        '''
        
        print(f"\nREGISTRO DE PONTUAÇÕES - BD: {nome_bd} - {tabela.upper().replace('_', ' ')}:\n\n")

        opcoes = ["Consultar estatísticas",
                  "Adicionar um jogo",
                  "Sair",
                  "Alterar/Criar temporada",
                  "Deletar temporada",
                  "Alterar BD",
                  "Deletar BD",
                  "Consultar outras estatísticas",
##                  "",
                  ]

        opcoes.sort()
        self.lista_opcoes(opcoes)

        parametro = None
        escolha = opcoes[self.entrada_int(len(opcoes)) - 1]

        if "Deletar temporada" in escolha:
            parametro = tabela

        if "Sair" in escolha:
            print("\n\nENCERRANDO REGISTRO DE PONTUAÇÕES...\n\n")

        elif "Adicionar um jogo" in escolha:
            print("\n\nINTERFACE PARA ADICIONAR JOGOS...\n\nQual foi o placar do jogo? (limite 999)")
            parametro = self.entrada_int(999)
            
            opcoes = ["Sim", "Não"]
            print(f"\nAdicionar novo jogo com placar {parametro}... Confirma?\n")
            self.lista_opcoes(opcoes)

            if "Sim" in opcoes[self.entrada_int(len(opcoes)) - 1]:
                print(f"\nIncluído novo jogo com {parametro} pontos!\n")

            else:
                escolha = "não adicionar"
                print("\nNão foi incluído o novo jogo na tabela...\n")

        else:
            print(f"\n\nINTERFACE PARA {escolha.upper()}...\n\n")


        return escolha, parametro
