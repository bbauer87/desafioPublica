from tabulate import tabulate
from pathvalidate import is_valid_filename

class Cli:
    def __init__(self, bancos):
        self.bancos = bancos[:]#precisa do [:]?


    def escolhe_temporada(self, lista):
        print(f"\nO BD escolhido tem {len(lista)} temporadas. Escolha uma:\n")

        self.lista_opcoes(lista)

        return lista[self.entrada_int(len(lista)) - 1]


    def escolhe_banco(self):
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
        for x, y in enumerate(lista):
            print(f" [{x + 1}] - {y}")


    def consultar_tabela(self, itens, colunas):
        print(tabulate(itens, colunas, numalign = "center", tablefmt = "grid"))
        print("\n\n")


    def verif_tabela_existente(self, lista):
        if "Criar nova temporada" in lista:
            lista.remove("Criar nova temporada")

        temporada = self.entrada_int(10000)
        for x in lista:
            if str(temporada) == x.replace("temporada_", ""):
                return False

        return temporada
        

    def alterar_temporada(self, lista, tabela_atual):        
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





