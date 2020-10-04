import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from datetime import datetime


from pathvalidate import is_valid_filename

from controlador_gui import ControladorGui

import matplotlib
matplotlib.use("Agg")
##matplotlib.use("TkAgg")


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style

from matplotlib import pyplot as plt


style.use('ggplot')

LARGE_FONT = ("Verdana", 12)

NOME_BANCO = NOME_TABELA = None

ICONE = ".\\Misc\\ball.ico"


def tutorial():

    def page2():
        tut.destroy()
        tut2 = tk.Tk()

        def page3():
            tut2.destroy()
            tut3 = tk.Tk()

            tut3.wm_title("Part 3!")

            label = ttk.Label(tut3, text="Part 3", font=NORM_FONT)
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(tut3, text="Done!", command= tut3.destroy)
            B1.pack()
            tut3.mainloop()



        tut2.wm_title("Part 2!")
        label = ttk.Label(tut2, text="Part 2", font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(tut2, text="Next", command= page3)
        B1.pack()
        tut2.mainloop()

    tut = tk.Tk()
    tut.wm_title("Tutorial")
    label = ttk.Label(tut, text="What do you need help with?", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)

    B1 = ttk.Button(tut, text = "Overview of the application", command=page2)
    B1.pack()

    B2 = ttk.Button(tut, text = "How do I trade with this client?", command=lambda:popupmsg("Not yet completed"))
    B2.pack()

    B3 = ttk.Button(tut, text = "Indicator Questions/Help", command=lambda:popupmsg("Not yet completed"))
    B3.pack()

    tut.mainloop()






##def add_jogo():
##    janela = tk.Tk()
##    janela.iconbitmap(self, ICONE)
##    janela.wm_title("Vitiligos?")
##
##    msg = ttk.Label(janela, text="Soltei um peido marotáço!")
##    msg.pack(side = "top", fill = "x", pady = 10)
##    entrada = ttk.Entry(janela)
##    entrada.insert(0, "1 a 999")
##    entrada.pack()
##    botao = ttk.Button(janela, text = "Sairley", width = 10, command = janela.destroy)
##    botao.pack()
##
##    entrada.focus_force()      
##    tk.mainloop()











def sobre():
    pass


        
        



class Gui(tk.Tk):
    
    def inicio(self, tipo):
        global NOME_TABELA
        
        self.controlador = ControladorGui()

        #########################
        def confirmar(tipo, param = ""):
            global NOME_BANCO
            global NOME_TABELA
            
            if tipo == "banco":
                self.controlador.conecta(f".\\BD\\{param}")
                tk.messagebox.showinfo(title="Sucesso!",  message=f"Conexão estabelecida com {param}!")
                NOME_BANCO = param

            elif tipo == "tabela":                
                self.controlador.tabela("escolhe", param)
                NOME_TABELA = param

            elif tipo == "iniciar o programa":                
                NOME_BANCO = "Testes.db"
                NOME_TABELA = str(datetime.now().year)
                self.controlador.tabela("escolhe", NOME_TABELA)
                
                
            janela.destroy()
        ########################

        
        if "criar" in tipo:
            janela = tk.Tk()
            janela.wm_title("Aviso")            
            janela.iconbitmap(self, ICONE)

            msg = ttk.Label(janela, text="Não foi localizado nenhum banco de dados.\nSerá criado um chamado 'Testes.db' para que você se familiarize.")
            msg.pack(side="top")
            
            self.controlador.conecta(f".\\BD\\Testes.db")

            botao1 = tk.Button(janela, text = "Confirmar", width = 15, command =lambda: confirmar("iniciar o programa"), bg='green',fg='white')
            botao1.pack()
            
            janela.geometry("340x206")
            tk.mainloop()

        if "listar" in tipo:
            janela = tk.Tk()
            janela.wm_title("Banco de dados")            
            janela.iconbitmap(self, ICONE)

            msg = ttk.Label(janela, text="Escolha um BD:")
            msg.pack(side="top")

            listagem = tk.Listbox(janela, selectmode=tk.SINGLE)
            listagem.pack(side="left")

            for item in self.controlador.bancos:
                listagem.insert(tk.END, item)
                
            listagem.selection_set(first=0)##tem q ser dps q inseriu os itens, neh, cumpadi.. agora funfa

                    
            botao1 = tk.Button(janela, text = "Confirmar", width = 15, command =lambda: confirmar("banco", listagem.get(listagem.curselection())), bg='green',fg='white')
            botao1.pack()
            
            botao2 = tk.Button(janela, text = "Sair", width = 10, command = janela.destroy, bg='brown',fg='white')
            botao2.pack()


            janela.geometry("480x206")
            tk.mainloop()


        ################################dps de conectar com banco tem q escolher uma temporada caso mais de uma tabela no bd
        try:
            tabelas = self.controlador.tabela("consulta")

        except AttributeError:
            return "SAIR"

        print(tabelas)#deletar

        if len(tabelas) <= 0:
            print("tabelas if <= 0 ", tabelas)#deletar
            
            self.controlador.tabela("escolhe", datetime.now().year)
            NOME_TABELA = str(datetime.now().year)

        elif len(tabelas) == 1:
            print("tabelas if == 1 ", tabelas)#deletar
            
            self.controlador.tabela("escolhe", tabelas[0])
            NOME_TABELA = tabelas[0]

        else:            
            janela = tk.Tk()
            janela.wm_title("Temporadas")
            janela.iconbitmap(self, ICONE)

            msg = ttk.Label(janela, text="Escolha uma temporada:")
            msg.pack(side="top")

            listagem = tk.Listbox(janela, selectmode=tk.SINGLE)
            listagem.pack(side="left")

            for item in tabelas:
                listagem.insert(tk.END, item)
            
            listagem.selection_set(first=0)
                    
            botao1 = tk.Button(janela, text = "Confirmar", width = 15, command =lambda: confirmar("tabela", listagem.get(listagem.curselection())), bg='green',fg='white')
            botao1.pack()
            
            janela.geometry("480x206")
            tk.mainloop()


    def fim(self):
        self.controlador.encerra()


    def atualiza_nomes(self):
        tk.Tk.wm_title(self, f"Registro de pontuação  |  Conectado em: {NOME_BANCO}")
        self.after(5000, self.atualiza_nomes)

        
    def __init__(self, *args, **kwargs):

        self.controlador = ControladorGui()
        
        if self.controlador.bancos:
            self.escolha = self.inicio("listar")                

        else:
            self.escolha = self.inicio("criar")
            
            
        if self.escolha != "SAIR":

            tk.Tk.__init__(self, *args, **kwargs)
            tk.Tk.iconbitmap(self, ICONE)
            tk.Tk.wm_title(self, f"Registro de pontuação | Conectando...")
            
            container = tk.Frame(self)
            container.pack(side = "top", fill = "both", expand = True)
    ##        container.grid_rowconfigure(0, weight=1)
    ##        container.grid_columnconfigure(0, weight=1)

            barra_menu = tk.Menu(container)
            menu_arquivo = tk.Menu(barra_menu, tearoff=0)#tearoff eh uma opcao doida onde tu pode destacar o menu, onde se cria uma nova doida janela

            menu_arquivo.add_command(label="Adicionar um jogo", command=self.add_jogo)#pronto e bombamdexter
            menu_arquivo.add_separator()
            
            menu_arquivo.add_command(label="Alterar/Criar temporada", command=lambda:self.ativa_frame("PaginaTemporadas"))#pronto e bombamdexter
            menu_arquivo.add_command(label="Deletar temporada", command=self.del_temporada)#pronto e bombamdexter
            menu_arquivo.add_separator()
            
            menu_arquivo.add_command(label="Alterar/Criar banco de dados", command=lambda:self.ativa_frame("PaginaEscolheCriaBanco"))#pronto soh precisa uma lev consistencia
            menu_arquivo.add_command(label="Deletar banco de dados", command=self.del_BD)#pronto e bombamdexter
            menu_arquivo.add_separator()
            
            menu_arquivo.add_command(label = "Sair", command = self.destroy)
            
            barra_menu.add_cascade(label = "Arquivo", menu = menu_arquivo)

            menu_estats = tk.Menu(barra_menu, tearoff=0)
            menu_estats.add_command(label="Consultar gráfico", command=lambda: self.ativa_frame("PaginaGrafico"))#pronto e bombamdexter
            menu_estats.add_command(label="Consultar tabelas", command=lambda: self.ativa_frame("PaginaTabelas"))#pronto e bombamdexter
            barra_menu.add_cascade(label = "Estatísticas", menu = menu_estats)
            
            menu_ajuda = tk.Menu(barra_menu, tearoff=0)
            menu_ajuda.add_command(label="Sobre", command=sobre)#nadal
            menu_ajuda.add_separator()
            
            menu_ajuda.add_command(label="Tutorial", command=tutorial)#nadal
            barra_menu.add_cascade(label = "Ajuda", menu = menu_ajuda)

            tk.Tk.config(self, menu=barra_menu)

            self.frames = {}
            verif_classes(globals())           
            for F in CLASSES:
                frame = CLASSES[F](container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")


            self.ativa_frame("PaginaInicial")
        

    def del_BD(self):
        def confirmar():
            pergunta = tk.messagebox.askquestion("Deletar BD", f"Tem certeza que quer deletar {listagem.get(listagem.curselection())}? Esse processo não pode ser revertido caso confirmado!", icon = "warning")
            if pergunta == "yes":
                self.controlador.deletar("deletar BD", listagem.get(listagem.curselection()))
                tk.messagebox.showinfo(title="Sucesso!",  message=f"Foi deletado o BD {listagem.get(listagem.curselection())}!!")
            janela.destroy()

        
        self.controlador.busca_bds()
        
##        print("self.controlador.bancos -> ", self.controlador.bancos)
        
        self.controlador.bancos.remove(NOME_BANCO)
        
##        print("self.controlador.bancos 2 -> ", self.controlador.bancos)

        if not self.controlador.bancos:
            tk.messagebox.showinfo(title="Aviso",  message="Só há um BD no sistema, não sendo possível deletá-lo pois está em uso. Crie um novo BD e tente novamente.")
            return

        
        janela = tk.Tk()
        janela.wm_title("Deletar um BD")
        janela.iconbitmap(self, ICONE)

        msg = ttk.Label(janela, text="Escolha um BD:")
        msg.pack(side="top")

        listagem = tk.Listbox(janela, selectmode=tk.SINGLE)
        listagem.pack(side="left")

        for item in self.controlador.bancos:
            listagem.insert(tk.END, item)

        listagem.selection_set(first=0)##tem q ser dps q inseriu os itens, neh, cumpadi.. agora funfa

                
        botao1 = tk.Button(janela, text = "Confirmarley", width = 15, command = confirmar, bg='green',fg='white')
        botao1.pack()
        
        botao2 = tk.Button(janela, text = "Sairley", width = 10, command = janela.destroy, bg='brown',fg='white')
        botao2.pack()


##        janela.geometry("280x106")
        
        tk.mainloop()
        
    

    def del_temporada(self):
        def confirmar():
            pergunta = tk.messagebox.askquestion("Deletar temporada", f"Tem certeza que quer deletar {listagem.get(listagem.curselection())}? Esse processo não pode ser revertido caso confirmado!", icon = "warning")
            if pergunta == "yes":
                self.controlador.deletar("deletar temporada", listagem.get(listagem.curselection()))
                tk.messagebox.showinfo(title="Sucesso!",  message=f"Foi deletada a temporada {listagem.get(listagem.curselection())}!!")
            janela.destroy()

        
        temporadas, temp_atual = self.controlador.altera_cria_temp("inicial")

        if not temporadas:
            tk.messagebox.showinfo(title="Aviso",  message="Só há uma temporada no sistema, não sendo possível deletá-la pois está em uso. Crie uma nova temporada e tente novamente.")
            return
            
        
        janela = tk.Tk()
        janela.wm_title("Deletar uma temporada")
        janela.iconbitmap(self, ICONE)

        msg = ttk.Label(janela, text="Escolha uma temporada:")
        msg.pack(side="top")

        listagem = tk.Listbox(janela, selectmode=tk.SINGLE)
        listagem.pack(side="left")

        for item in temporadas:
            listagem.insert(tk.END, item)

        listagem.selection_set(first=0)##tem q ser dps q inseriu os itens, neh, cumpadi.. agora funfa

                
        botao1 = tk.Button(janela, text = "Confirmarley", width = 15, command = confirmar, bg='green',fg='white')
        botao1.pack()
        
        botao2 = tk.Button(janela, text = "Sairley", width = 10, command = janela.destroy, bg='brown',fg='white')
        botao2.pack()


##        janela.geometry("280x106")
        
        tk.mainloop()

    


    def add_jogo(self):

        def recebe_resposta(placar):
            try:
                placar = int(placar)
                if placar < 1 or placar > 999:
                    raise Exception
                
            except:
                tk.messagebox.showinfo(title="ERROU!!!",  message="O placar deve ser um número de 1 a 999!!")

            else:                
                resposta = self.controlador.add_placar(placar)

                if resposta == "novo mínimo":
                    tk.messagebox.showinfo(title="Recorde quebrado!!",  message="Um novo placar mínimo foi registrado na temporada!")

                elif resposta == "novo máximo":
                    tk.messagebox.showinfo(title="Recorde quebrado!!",  message="Um novo placar máximo foi registrado na temporada!")

                else:
                    tk.messagebox.showinfo(title="Sucesso!!",  message="Um novo placar foi registrado na temporada!")

            finally:
                janela.destroy()
            
        janela = tk.Tk()
        janela.iconbitmap(self, ICONE)
        janela.wm_title("Adicionar um jogo")
        janela.grid_rowconfigure(0, weight=1)
        janela.grid_columnconfigure(0, weight=1)

        msg = ttk.Label(janela, text="Insira a pontuação (1 a 999):")
        msg.grid(row = 0, column = 0)
        
    ##    msg.grid(row = 0, column = 1, rowspan = 6, sticky = "ns")
        
        entrada = ttk.Entry(janela)
        entrada.grid(row = 0, column = 1)
        
        botao1 = tk.Button(janela, text = "Confirmarley", width = 15, command = lambda: recebe_resposta(entrada.get()), bg='green',fg='white')
        botao1.grid(row = 1, column = 0, pady=5)

        
        botao2 = tk.Button(janela, text = "Sairley", width = 10, command = janela.destroy, bg='brown',fg='white')
        botao2.grid(row = 1, column = 1, pady=5)

        entrada.focus_force()
        janela.geometry("280x106")
        tk.mainloop()
        
        

    def ativa_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()




class PaginaGrafico(tk.Frame):##dps q gerou o grafico e add um placar, ele nao atualiza o graifoc.. se pah olhe nos vids do malucao lah pra ver como ele atualiza

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        button1 = ttk.Button(self, text="Menu inicial",
                            command=lambda: controller.ativa_frame("PaginaInicial"))
        button1.pack()

        self.button2 = ttk.Button(self, text="Gerar",
                            command=lambda: self.gera(controller.controlador.retorna_dados()[0]))
        self.button2.pack()

##        self.canvas = None

##        self.tabela = controller.nome_tabela



    def gera(self, dados):#tah comendo uns 6 mega de memoria a cada vez q atualiza, mas pleo menos atualiza >D
        try: 
            self.canvas.get_tk_widget().pack_forget()
            self.toolbar.pack_forget()
##            self.canvas.destroy("all")
##            self.canvas = None
##            self.f.clear()
##            plt.close(self.f)
        except AttributeError: 
            pass
        
        self.button2["text"] = "Atualizar"

        f = Figure()
        
##        self.f = plt.figure()
        
        plotar = f.add_subplot(111)
        plotar.set_title(f"Pontuação temporada {NOME_TABELA}")        
        plotar.set_ylabel("Placar")
        plotar.set_xlabel("Jogo número")       

        placares = [x[1] for x in dados]
        jogos = [x + 1 for x in range(len(dados))]

        plotar.set_xticks(jogos)            
        plotar.plot(jogos, placares)###aki vai dados da tabela.. ex, x = nro jogo, y = placar desse jogo

        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.canvas.draw()

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()


class PaginaInicial(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        container_botoes = tk.LabelFrame(self)

        container1 = tk.LabelFrame(container_botoes, text = "Inserir/Visualizar")
        container2 = tk.LabelFrame(container_botoes, text = "Temporadas")
        container3 = tk.LabelFrame(container_botoes, text = "Banco de Dados")

        container_botoes.pack(side = "left", padx = 10, pady = 10)
        
        container1.pack(fill = "both", padx = 10, pady = 10)
        container2.pack(fill = "both", padx = 10, pady = 10)
        container3.pack(fill = "both", padx = 10, pady = 10)

#################
        add_placar = ttk.Button(container1, text = "Adicionar placar",
                            command= controller.add_jogo)
        add_placar.pack(side="left", padx = 5, pady = 5)
        
        tabelas = ttk.Button(container1, text = "Tabelas",
                            command=lambda: controller.ativa_frame("PaginaTabelas"))
        tabelas.pack(side="right", padx = 5, pady = 5)

        grafico = ttk.Button(container1, text = "Gráfico",
                            command=lambda: controller.ativa_frame("PaginaGrafico"))
        grafico.pack(padx = 5, pady = 5)
#################

        temporada1 = ttk.Button(container2, text = "Alterar/Criar",
                            command=lambda: controller.ativa_frame("PaginaTemporadas"))
        temporada1.pack(padx = 5, pady = 5)
        
        temporada2 = ttk.Button(container2, text = "Deletar",
                            command= controller.del_temporada)
        temporada2.pack(padx = 5, pady = 5)
#################

        banco1 = ttk.Button(container3, text = "Alterar/Criar",
                            command=lambda: controller.ativa_frame("PaginaEscolheCriaBanco"))
        banco1.pack(padx = 5, pady = 5)
        
        banco2 = ttk.Button(container3, text = "Deletar",
                            command= controller.del_BD)
        banco2.pack(padx = 5, pady = 5)
#################   
        
        sair = tk.Button(container_botoes, text = "Sair",
                         command= controller.destroy,
                         bg="red", fg="white",
                         width = 10)
        sair.pack(padx = 15, pady = 15)   



        imagem = Image.open(".\\Misc\\fundo.png")
        render = ImageTk.PhotoImage(imagem)
        
        painel = tk.Label(self, image = render)
        painel.image = render
        painel.pack(side = "right")#, fill = "both", expand = "yes")




        


        


        

##        janela = tk.Tk()
##        janela.iconbitmap(self, ICONE)
##        janela.wm_title("Adicionar um jogo")
##        janela.grid_rowconfigure(0, weight=1)
##        janela.grid_columnconfigure(0, weight=1)
##
##        msg = ttk.Label(janela, text="Insira a pontuação (1 a 999):")
##        msg.grid(row = 0, column = 0)
##        
##    ##    msg.grid(row = 0, column = 1, rowspan = 6, sticky = "ns")
##        
##        entrada = ttk.Entry(janela)
##        entrada.grid(row = 0, column = 1)
##        
##        botao1 = tk.Button(janela, text = "Confirmarley", width = 15, command = lambda: recebe_resposta(entrada.get()), bg='green',fg='white')
##        botao1.grid(row = 1, column = 0, pady=5)
##
##        
##        botao2 = tk.Button(janela, text = "Sairley", width = 10, command = janela.destroy, bg='brown',fg='white')
##        botao2.grid(row = 1, column = 1, pady=5)
##
##        entrada.focus_force()
##        janela.geometry("280x106")
##        tk.mainloop()
        

        
        




class PaginaEscolheCriaBanco(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
##        titulo = tk.Label(self, text = "Escolha uma opção:")
##        titulo.grid(row = 0, column = 0)

        self.botao_buscar = ttk.Button(self, text = "Buscar BDs", command= lambda: self.buscar(controller))
        self.botao_buscar.grid()

        sep1 = ttk.Separator(self)
        sep1.configure(orient = "vertical")
        sep1.grid(row = 1, column = 2, rowspan = 6, sticky = "ns")

        self.botao_escolhido = tk.StringVar()
        self.botao_escolhido.set("criar")
        
        self.botao_rad_1 = ttk.Radiobutton(self, text = "BDs localizados",
                                           variable = self.botao_escolhido, value = "localizar", command= self.escolhas)
        self.botao_rad_1.grid(row = 1, column = 0, pady = 10)
        
        botao_rad_2 = ttk.Radiobutton(self, text = "Criar BD",
                                      variable = self.botao_escolhido, value = "criar", command=self.escolhas)
        botao_rad_2.grid(row = 1, column = 4, pady = 10)

   
        self.listagem = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listagem.configure(background = "gray")
        self.listagem.configure(disabledforeground = "black")
        self.listagem.grid(columnspan = 2, row = 2, rowspan = 4, padx = 10, pady = 10)

##        itens = 
##        itens.remove(NOME_BANCO)
##        
##        for item in itens:
##            self.listagem.insert(tk.END, item)
##
##        self.listagem.selection_set(first=0)##tem q ser dps q inseriu os itens, neh, cumpadi.. agora funfa
        
        msg1 = tk.Label(self, text = "Nome:")
        msg1.grid(row = 3, column = 3)

        self.entrada1 = ttk.Entry(self)  
        self.entrada1.grid(row = 3, column = 4, padx = 5)
        
        msg2 = tk.Label(self, text = "Temporada:") 
        msg2.grid(row = 4, column = 3, padx = 5)

        self.entrada2 = ttk.Entry(self)
        self.entrada2.insert(0, "1 a 10000")
        self.entrada2.grid(row = 4, column = 4, padx = 5)
        

        botao1 = ttk.Button(self, text = "Menu inicial", command = lambda: controller.ativa_frame("PaginaInicial"))
        botao1.grid(row = 6, column = 0, pady = 10)

        botao2 = ttk.Button(self, text = "Confirmar", command = lambda: self.confirmar(controller))
        botao2.grid(row = 6, column = 4, pady = 10)

        self.primeiravez = True
        
        self.botao_escolhido.set("localizar")
        self.botao_buscar.invoke()
        self.botao_escolhido.set("criar")
        botao_rad_2.invoke()


    def buscar(self, controller):
        controller.controlador.busca_bds()

        controller.controlador.bancos.remove(NOME_BANCO)


        
        self.botao_escolhido.set("localizar")
        self.botao_rad_1.invoke()

        if self.primeiravez:
            self.primeiravez = False

        else:
            self.listagem.delete(0, 'end')
        
        for item in controller.controlador.bancos:
            self.listagem.insert(tk.END, item)

        self.listagem.selection_set(first=0)##tem q ser dps q inseriu os itens, neh, cumpadi.. agora funfa


    def escolhas(self):
        if self.botao_escolhido.get() == "criar":#bloqueia listagem
            self.listagem.configure(background = "gray", state=tk.DISABLED)
            
            self.entrada1.configure(state=tk.NORMAL)
            self.entrada2.configure(state=tk.NORMAL)

        else:#bloqeia campos criar bd            
            self.listagem.configure(background = "white", state=tk.NORMAL)
            
            self.entrada1.configure(state=tk.DISABLED)
            self.entrada2.configure(state=tk.DISABLED)


    def confirmar(self, controller):
        global NOME_BANCO
        global NOME_TABELA
        
        validacao = False
        
        if self.botao_escolhido.get() == "criar":
            controller.controlador.busca_bds()
            
            
            print("### ", self.entrada1.get())
            print("$$$ ", controller.controlador.bancos)

            try:
                if not is_valid_filename(self.entrada1.get()) or self.entrada1.get() + ".db" in controller.controlador.bancos:
                    raise Exception
                    
                numero = int(self.entrada2.get())
                if numero < 1 or numero > 10_000:
                    raise Exception

            except:
                tk.messagebox.showinfo(title="ERROU!!!",  message=f"O número da temporada deve estar entre 1 e 10.000.\n\nAlém disso, não é possível usar um nome já existente ou que contenha os seguites caracteres:\n:, *, /, \", ?, >, |, <, \\.\n\nTente novamente!")

            else:
                tk.messagebox.showinfo(title="Testes criar",  message=f"Criar BD com nome {self.entrada1.get()} e temporada {self.entrada2.get()}")
                controller.controlador.altera_cria_bd((self.entrada1.get() + ".db", self.entrada2.get()))
                NOME_BANCO = self.entrada1.get() + ".db"
                NOME_TABELA = self.entrada2.get()

                print(NOME_BANCO, NOME_TABELA)#deletar
                
                validacao = True

        else:            
            tk.messagebox.showinfo(title="Testes localizar",  message=f"Alterar BD para {self.listagem.get(self.listagem.curselection())}")

            nome = controller.controlador.altera_cria_bd((self.listagem.get(self.listagem.curselection()), None))

            NOME_BANCO = self.listagem.get(self.listagem.curselection())            
            NOME_TABELA = nome


            print(NOME_BANCO, NOME_TABELA)#deletar

            validacao = True

        if validacao:
            controller.ativa_frame("PaginaInicial")


class PaginaTemporadas(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.botao_buscar = ttk.Button(self, text = "Buscar temporadas", command= lambda: self.buscar(controller.controlador.altera_cria_temp("inicial")))
        self.botao_buscar.pack()

        self.botao_escolhido = tk.StringVar()
##        self.botao_escolhido.set("criar")
        
        self.botao_rad_1 = ttk.Radiobutton(self, text = "Temporadas localizadas",
                                 variable = self.botao_escolhido, value = "localizar", command= self.escolhas)
        self.botao_rad_1.pack()
        
        self.botao_rad_2 = ttk.Radiobutton(self, text = "Criar temporada",
                                 variable = self.botao_escolhido, value = "criar", command=self.escolhas)
        self.botao_rad_2.pack()
   
        self.listagem = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listagem.configure(background = "gray")
        self.listagem.configure(disabledforeground = "black")

        self.listagem.pack(side="left")

##        for item in self.temporadas:
##            self.listagem.insert(tk.END, item)
        
        msg1 = tk.Label(self, text = "Temporada:")
        msg1.pack()

        self.entrada1 = ttk.Entry(self)
        self.entrada1.insert(0, "1 a 10000")
        self.entrada1.pack()       

        botao1 = tk.Button(self, text = "Página inicial", command = lambda: controller.ativa_frame("PaginaInicial"), bg='brown',fg='white')
        botao1.pack()

        botao2 = tk.Button(self, text = "Confirmar", command = lambda: self.confirmar(controller), bg='green',fg='white')
        botao2.pack()

        self.primeiravez = True
        
        self.botao_escolhido.set("localizar")
        self.botao_buscar.invoke()
        self.botao_escolhido.set("criar")
        self.botao_rad_2.invoke()
        


    def escolhas(self):
        if self.botao_escolhido.get() == "criar":#bloqueia listagem
            self.listagem.configure(background = "gray", state=tk.DISABLED)            
            self.entrada1.configure(state=tk.NORMAL)

        else:#bloqeia campos criar temporada            
            self.listagem.configure(background = "white", state=tk.NORMAL)            
            self.entrada1.configure(state=tk.DISABLED)


    def buscar(self, controller):
        self.temporadas, self.temp_atual = controller

        
        self.botao_escolhido.set("localizar")
        self.botao_rad_1.invoke()

        if self.primeiravez:
            self.primeiravez = False

        else:
            self.listagem.delete(0, 'end')
        
        for item in self.temporadas:
            self.listagem.insert(tk.END, item)

        self.listagem.selection_set(first=0)##tem q ser dps q inseriu os itens, neh, cumpadi.. agora funfa
            

    def verif_tabela_existente(self, lista, entrada, temp_atual):
        if entrada == temp_atual.replace("temporada_", ""):
            return False

        for x in lista:
            print("x ", x)
            if entrada == x.replace("temporada_", ""):
                return False

        return entrada



    def confirmar(self, controller):
        global NOME_TABELA
        
        validar = True

        msg = "Erro!\n"
        
        if self.botao_escolhido.get() == "criar":
            try:
                numero = int(self.entrada1.get())
                if numero < 1 or numero > 10_000:
                    print("erro 1")
                    msg += "O número da temporada deve estar entre 1 e 10.000. Tente novamente!"
                    raise Exception

                verif = self.verif_tabela_existente(self.temporadas, self.entrada1.get(), self.temp_atual)

                if not verif:
                    print("erro 2")
                    msg += "Não foi possível criar essa temporada pois a numeração escolhida já consta no BD."
                    raise Exception

            except ValueError:
                tk.messagebox.showinfo(title="ERROU!!!",  message="Valor inválido na numeração da temporada!")

            except Exception:
                tk.messagebox.showinfo(title="ERROU!!!",  message=msg)

            else:
                tk.messagebox.showinfo(title="Testes criar",  message=f"Criar temporada de número {self.entrada1.get()}")
                
                controller.controlador.altera_cria_temp("criação", self.entrada1.get())
                NOME_TABELA = self.entrada1.get()

                print("apos criar temporada _>", NOME_TABELA)#deletar
                
                validar = True
                
                tk.messagebox.showinfo(title="Sucesso!",  message=f"Temporada {self.entrada1.get()} criada com sucesso!")

        else:
            try:
                tk.messagebox.showinfo(title="Testes localizar",  message=f"Alterar temporada para {self.listagem.get(self.listagem.curselection())}")

                controller.controlador.altera_cria_temp("alterar", self.listagem.get(self.listagem.curselection()))
                
                NOME_TABELA = self.listagem.get(self.listagem.curselection()).replace("temporada_", "")

                print("apos alterar nome tabela", NOME_TABELA)#deletar

                validar = True

                tk.messagebox.showinfo(title="Sucesso!",  message=f"Alteração com sucesso para temporada {NOME_TABELA}!")

            except:
                pass

        if validar:#volta menu principal
            self.botao_buscar.invoke()
            
            controller.ativa_frame("PaginaInicial")



            


class PaginaTabelas(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button1 = ttk.Button(self, text="Menu inicial",
                            command=lambda: controller.ativa_frame("PaginaInicial"))
        button1.pack(pady=10, padx=10, side="top")

        button2 = ttk.Button(self, text="Busca tabela",
                            command=lambda: self.atualiza(controller.controlador.retorna_dados()))
        button2.pack(pady=10, padx=10, side="bottom")

        self.container1 = tk.LabelFrame(self, text=f"Temporada {NOME_TABELA}")
        container2 = tk.LabelFrame(self)
        container3 = tk.LabelFrame(container2)
        container4 = tk.LabelFrame(container2)

        self.container1.pack(fill="both", padx=20, pady=10)
        container2.pack(fill="both", padx=20, pady=10)
        container3.pack(fill="both", side="left", padx=5, pady=5)
        container4.pack(fill="x", side="right", padx=5, pady=5)

        self.tabela1 = ttk.Treeview(self.container1, columns=(1,2,3,4,5,6), show="headings", height="10", selectmode="browse")

        scroll = ttk.Scrollbar(self.container1, orient="vertical", command=self.tabela1.yview)
        scroll.pack(side='right', fill='y')

        self.tabela1.configure(yscrollcommand=scroll.set)
        self.tabela1.pack(pady=10)

        self.tabela1.column(1, anchor="center", stretch=True, width=50)
        self.tabela1.column(2, anchor="center", stretch=True, width=60)
        self.tabela1.column(3, anchor="center", stretch=True)
        self.tabela1.column(4, anchor="center", stretch=True)
        self.tabela1.column(5, anchor="center", stretch=True)
        self.tabela1.column(6, anchor="center", stretch=True)

        self.tabela1.heading(1, text="JOGO", anchor="center")
        self.tabela1.heading(2, text="PLACAR", anchor="center")
        self.tabela1.heading(3, text="MÍN. DA TEMPORADA", anchor="center")
        self.tabela1.heading(4, text="MÁX. DA TEMPORADA", anchor="center")
        self.tabela1.heading(5, text="QUEBRA RECORDE MÍN.", anchor="center")
        self.tabela1.heading(6, text="QUEBRA RECORDE MAX.", anchor="center")

        
        self.tabela2 = ttk.Treeview(container3, columns=(1,2), show="headings", height="5", selectmode="none")
        self.tabela2.pack(pady=5, padx=5)
        self.tabela2.column(1, anchor="center", stretch=True, width=110)
        self.tabela2.column(2, anchor="center", stretch=True, width=150)

        self.tabela2.heading(1, text="TOP 5 PLACARES", anchor="center")
        self.tabela2.heading(2, text="TOP 5 PIORES PLACARES", anchor="center")

        self.tabela3 = ttk.Treeview(container3, columns=(1,2), show="headings", height="1", selectmode="none")
        self.tabela3.pack(pady=5, padx=5)
        self.tabela3.column(1, anchor="center", stretch=True, width=160)
        self.tabela3.column(2, anchor="center", stretch=True)

        self.tabela3.heading(1, text="SOMA DO TOP 5 PLACARES", anchor="center")
        self.tabela3.heading(2, text="SOMA DO TOP 5 PIORES PLACARES", anchor="center")

        self.tabela4 = ttk.Treeview(container4, columns=(1,2), show="headings", height="1", selectmode="none")
        self.tabela4.pack(pady=10, padx=5)
        self.tabela4.column(1, anchor="center", stretch=True)
        self.tabela4.column(2, anchor="center", stretch=True)

        self.tabela4.heading(1, text="SOMA DOS PLACARES", anchor="center")
        self.tabela4.heading(2, text="MÉDIA DOS PLACARES", anchor="center")
        

    def atualiza(self, dados):
        self.container1["text"] = f"Temporada {NOME_TABELA}"
        
        try:
            self.tabela1.delete(*self.tabela1.get_children())

            c = 1
            for item in dados[0]:
                self.tabela1.insert('', 'end', values=item, tags = ("pares" if c % 2 == 0 else "impares"))
                c += 1
                
            self.tabela1.tag_configure('impares', background='white')
            self.tabela1.tag_configure('pares', background='#dbdbdb')

            tmp = []
            for x in range(len(dados[1])):
                tmp.append([dados[1][x], dados[2][x]])
                
            self.tabela2.delete(*self.tabela2.get_children())

            c = 1
            for item in tmp:
                self.tabela2.insert('', 'end', values=item, tags = ("pares" if c % 2 == 0 else "impares"))
                c += 1

            
            self.tabela2.tag_configure('impares', background='white')
            self.tabela2.tag_configure('pares', background='#dbdbdb')


            tmp = [[sum(dados[1]), sum(dados[2])]]
                
            self.tabela3.delete(*self.tabela3.get_children())
            for item in tmp:
                self.tabela3.insert('', 'end', values=item)

            media = round((dados[3] / len(dados[0])), 2)
            tmp = [[dados[3], media]]
                
            self.tabela4.delete(*self.tabela4.get_children())
            for item in tmp:
                self.tabela4.insert('', 'end', values=item)
##
##            print("aki rola vitiligssss", NOME_TABELA)#deletar

            

        except TypeError:
            tk.messagebox.showinfo(title="Erro",  message="Impossível imprimir a tabela pois não há dados registrados.")




   

def verif_classes(param):
    global CLASSES   

    CLASSES = {}
    x = 0
    for x in param:
        if x.startswith("Pagina"):
            CLASSES[x] = param[x]


##OBS:
                    
## menu_arquivo.add_command(label="Adicionar um jogo", command=lambda: vitili()) ##soh use lambda qndo funcao precisar passar parametros
        
##              qndo quiser um popup rapidexter
##       tk.messagebox.showinfo(title="Testes",  message="Testamento")





if __name__ == '__main__':       
    interface = Gui()
    if interface.escolha != "SAIR":
        interface.geometry("980x640")
        interface.after(1000, interface.atualiza_nomes)
        
        interface.mainloop()
        interface.fim()
