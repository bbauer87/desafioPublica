from tabulate import tabulate


class Cli():
    def __init__(self, bancos):
        self.bancos = bancos[:]

    def escolhe_banco(self):
        temporada = 0
        
        if self.bancos:
            print("\nEscolha uma opção de banco de dados:\n")
            if "Criar um novo BD" not in self.bancos:
                self.bancos.append("Criar um novo BD")

            self.lista_opcoes(self.bancos)
            
            nome_bd = self.bancos[self.entrada_int(len(self.bancos)) - 1]
            if "Criar um novo BD" in nome_bd:
                print("\nDigite um nome para criarmos o BD:\n")
                nome_bd = self.entrada_str() + ".db"
                print("\nAgora digite um valor inteiro positivo para numerar a temporada (limite 10000):\n")
                temporada = self.entrada_int(10000)             

        else:
            print("\nNão foi localizado nenhum banco de dados. Insira um nome para criarmos o BD:\n")
            nome_bd = self.entrada_str() + ".db"
            print("\nAgora digite um valor inteiro positivo para numerar a temporada (limite 10000):\n")
            temporada = self.entrada_int(10000)

        return nome_bd, temporada

    def entrada_str(self):##usar https://pypi.org/project/pathvalidate/ no futuro
        while True:
            print("\n" + "-" * 100 + "\n")  
            resposta = input("\n>>> ")    
            if not resposta:
                print("\nDigite algo!!\n")
                continue            
            break
            
        print("\n" + "-" * 100 + "\n")
        return resposta
        
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
        

    def menu(self, nome_bd, tabela):
        print(f"\nREGISTRO DE PONTUAÇÕES - BD: {nome_bd} - {tabela.upper().replace('_', ' ')}:\n\n")

        opcoes = ["Consultar estatísticas",
                  "Adicionar um jogo",
                  "Sair",
    ##              "Alterar temporada",
    ##              "Alterar BD",
    ##              "",
                  ]

        opcoes.sort()
        self.lista_opcoes(opcoes)

        parametro = None
        escolha = opcoes[self.entrada_int(len(opcoes)) - 1]   

        if "Sair" in escolha:
            print("\n\nENCERRANDO REGISTRO DE PONTUAÇÕES...\n\n")
            
        if "Adicionar" in escolha:
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
        
        if "Consultar" in escolha:
            print("\n\nINTERFACE PARA CONSULTA DOS JOGOS...\n\n")

        return escolha, parametro





