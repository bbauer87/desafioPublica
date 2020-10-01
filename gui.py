import tkinter as tk
from tkinter import ttk

from controlador_gui import ControladorGui

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style



##from matplotlib import pyplot as plt


style.use('ggplot')

LARGE_FONT = ("Verdana", 12)

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

##from tabulate import tabulate
##
##def vitili():
##    janela = tk.Tk()
##    janela.wm_title("Vitiligos?")
##
##    tab = tabulate([(1, 2), (3, 4)], ["vaira", "laigo"], numalign = "center", tablefmt = "grid")
##
##    msg = ttk.Label(janela, text=
##                    f"""{tab}""")
##    msg.pack(side = "top", fill = "x", pady = 10)
##    entrada = ttk.Entry(janela)
##    entrada.insert(0, "1 a 999")
##    entrada.pack()
##    botao = ttk.Button(janela, text = "Sairley", width = 10, command = janela.destroy)
##    botao.pack()
##
##    entrada.focus_force()      
##    tk.mainloop()



def add_jogo():
    janela = tk.Tk()
    janela.wm_title("Vitiligos?")

    msg = ttk.Label(janela, text="Soltei um peido marotáço!")
    msg.pack(side = "top", fill = "x", pady = 10)
    entrada = ttk.Entry(janela)
    entrada.insert(0, "1 a 999")
    entrada.pack()
    botao = ttk.Button(janela, text = "Sairley", width = 10, command = janela.destroy)
    botao.pack()

    entrada.focus_force()      
    tk.mainloop()


##              qndo quiser um popup rapidexter
##       tk.messagebox.showinfo(title="Testes",  message="Testamento"))

def temporada():
    pass

def del_temporada():
    pass

def opcoes_BD():
    pass

def del_BD():
    pass

def estatisticas(tipo):
    if tipo == 1:#tabela normal
        pass
    else:#estatisticas 2
        pass

def sobre():
    pass








class PaginaGraph(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Menu inicial",
                            command=lambda: controller.ativa_frame("PaginaTopLevel"))
        button1.pack()

        f = Figure()
        a = f.add_subplot(111)
        a.set_title("Pontuação temporada XXXX")        
        a.set_ylabel('Placar')
        a.set_xlabel('Jogo número')
        
        a.plot([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5])###aki vai dados da tabela.. ex, x = nro jogo, y = placar desse jogo

        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)




class PaginaTopLevel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text = "Start Page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button = ttk.Button(self, text = "EscolheBanco",
                            command=lambda: controller.ativa_frame("PaginaEscolheBanco"))
        button.pack()

        button2 = ttk.Button(self, text="Graph",
                            command=lambda: controller.ativa_frame("PaginaGraph"))
        button2.pack()


class PaginaIntro(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text = "aqui vai uma imagem bacanoida e supimpatablet!", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

##        label = tk.Label(self, text = "aqui vai uma imagem bacanoida e supimpatablet!", font = LARGE_FONT)
##        label.pack(pady = 10, padx = 10)

        button = ttk.Button(self, text = "Avançar",
                            command=lambda: controller.ativa_frame("PaginaEscolheBanco"))
        button.pack()




class PaginaEscolheBanco(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
##        titulo = tk.Label(self, text = "Escolha uma opção:")
##        titulo.grid(row = 0, column = 0)

        sep1 = ttk.Separator(self)
        sep1.configure(orient = "vertical")
        sep1.grid(row = 1, column = 2, rowspan = 6, sticky = "ns")



        v = tk.IntVar()
        botao1 = ttk.Radiobutton(self, text = "BDs localizados", variable = v, value = 1)
        botao1.grid(row = 1, column = 0, pady = 10)
        botao2 = ttk.Radiobutton(self, text = "Criar BD", variable = v, value = 0)
        botao2.grid(row = 1, column = 4, pady = 10)

        

        listagem = tk.Listbox(self)
        listagem.configure(background = "white")
        listagem.configure(disabledforeground = "#a3a3a3")
        listagem.grid(columnspan = 2, row = 2, rowspan = 4, padx = 10, pady = 10)
        
        msg1 = tk.Label(self, text = "Nome:")
        msg1.grid(row = 3, column = 3)

        entrada1 = ttk.Entry(self)    
        entrada1.grid(row = 3, column = 4, padx = 5)
        
        msg2 = tk.Label(self, text = "Temporada:") 
        msg2.grid(row = 4, column = 3, padx = 5)

        entrada2 = ttk.Entry(self)
        entrada2.insert(0, "1 a 10000")#insere um valor mesmo q user nadal tenha digitado ainda, qndo janela recem abriu 
        entrada2.grid(row = 4, column = 4, padx = 5)
        

        botao1 = ttk.Button(self, text = "Menu inicial", command = lambda: controller.ativa_frame("PaginaTopLevel"))
        botao1.grid(row = 6, column = 0, pady = 10)

        botao2 = ttk.Button(self, text = "Confirmar", command = lambda: controller.ativa_frame("PaginaDois"))
        botao2.grid(row = 6, column = 4, pady = 10)


class PaginaDois(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.ativa_frame("PaginaTopLevel"))
        button1.pack()

        button2 = ttk.Button(self, text="EscolheBanco",
                            command=lambda: controller.ativa_frame("PaginaEscolheBanco"))
        button2.pack()  


class Gui(tk.Tk):
    def __init__(self, *args, **kwargs):

        self.controlador = ControladorGui()

        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, "ball.ico")
        tk.Tk.wm_title(self, "Registro de pontuação")
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        barra_menu = tk.Menu(container)
        menu_arquivo = tk.Menu(barra_menu, tearoff=0)#tearoff eh uma opcao doida onde tu pode destacar o menu, onde se cria uma nova doida janela
        menu_arquivo.add_command(label="Adicionar um jogo", command=add_jogo)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Alterar/Criar temporada", command=temporada)
        menu_arquivo.add_command(label="Deletar temporada", command=del_temporada)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Alterar/Criar banco de dados", command=opcoes_BD)
        menu_arquivo.add_command(label="Deletar banco de dados", command=del_BD)
        
##        menu_arquivo.add_command(label="Adicionar um jogo", command=lambda: vitili()) ##soh use lambda qndo funcao precisar passar parametros
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label = "Sair", command = self.destroy)
        barra_menu.add_cascade(label = "Arquivo", menu = menu_arquivo)

        menu_estats = tk.Menu(barra_menu, tearoff=0)
        menu_estats.add_command(label="Consultar jogos, placares e recordes", command=lambda: estatisticas(1))
        menu_estats.add_command(label="Consultar soma de placares, média, top 5 e outras", command=lambda: estatisticas(2))
        barra_menu.add_cascade(label = "Estatísticas", menu = menu_estats)

        menu_ajuda = tk.Menu(barra_menu, tearoff=0)
        menu_ajuda.add_command(label="Sobre", command=sobre)
        menu_ajuda.add_separator()
        menu_ajuda.add_command(label="Tutorial", command=tutorial)
        barra_menu.add_cascade(label = "Ajuda", menu = menu_ajuda)


        tk.Tk.config(self, menu=barra_menu)

        self.frames = {}

        verif_classes(globals())   

##        print("CLASSES ", CLASSES)
##        print("self.frames ", self.frames)
        
        for F in CLASSES:
##            print("F ", F, type(F))
##            print(locals())
##            print(locals()[F])
##            print("CLASSES[F]", CLASSES[F])

            frame = CLASSES[F](container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

##        print("self.frames ", self.frames)

        self.ativa_frame("PaginaIntro")

    def ativa_frame(self, cont):
##        print("cont ", cont)
##
        frame = self.frames[cont]
        frame.tkraise()
        

def verif_classes(param):
    global CLASSES   

    CLASSES = {}
    x = 0
    for x in param:
        if x.startswith("Pagina"):
            CLASSES[x] = param[x]


if __name__ == '__main__':       
    interface = Gui()
    interface.geometry("480x640")
    interface.mainloop()
