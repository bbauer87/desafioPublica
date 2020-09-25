from sys import argv
import os

from banco import BD
import cli

class Controlador():
    def __init__(self):
        self.busca_bds()
        
        try:
            if argv[1] == "GUI":
                pass
            elif argv[1] == "CLI":
                self.cli()
            else:
                raise Exception
        except Exception as e:
            print("\nErro! O programa deve ser iniciado com um dos seguintes parâmetros: 'GUI' ou 'CLI'...\n")
            print(e)
            quit()

    def busca_bds(self):
        self.diretorio = os.path.dirname(__file__) + "\\BDs\\"        
        self.bancos = [file for file in os.listdir(self.diretorio) if file.endswith(".db")]

    def cli(self):
        self.visao = cli.Cli(self.bancos)
        nome_bd, temporada = self.visao.escolhe_banco()

        try:
            if nome_bd in self.bancos:
                bd = BD(self.diretorio + nome_bd)
            else:
                bd = BD(self.diretorio + nome_bd, temporada)
        except Exception as e:
            print(f"\nErro fatal na conexão com o BD '{nome_bd}'!\n")
            print(e)
            quit()

        while True:
            escolha, parametro = self.visao.menu(nome_bd, bd.tabela)
            if "Sair" in escolha:
                quit()
                
            elif "Consultar" in escolha:
                dados = bd.printa_tabela()
                self.visao.consultar_tabela(dados[0], dados[1])

            elif "Adicionar" in escolha:
                itens_serie = bd.retorna_tabela("inteira")
                
                if len(itens_serie) > 0:                 
                    ultima_linha = bd.retorna_tabela("última linha")
                    placar_min = ultima_linha[1]
                    placar_max = ultima_linha[2]
                    quebra_min = ultima_linha[3]
                    quebra_max = ultima_linha[4]
                    tipo = "normal"

                    if parametro < placar_min:
                        tipo = "novo mínimo"
                        quebra_min += 1
                        print("Um novo placar mínimo na temporada foi registrado!")
                        
                    elif parametro > placar_max:
                        tipo = "novo máximo"
                        quebra_max += 1                        
                        print("Um novo placar máximo na temporada foi registrado!")

                    bd.add_placar_2([parametro, placar_min, placar_max, quebra_min, quebra_max], tipo)

                else:                  
                    bd.add_placar_1(parametro)



app = Controlador()        
