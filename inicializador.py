


from sys import argv






try:
    if argv[1] not in ["GUI", "CLI"]:        
        raise Exception
    
except Exception as e:
    print("\nErro! O programa deve ser iniciado com um dos seguintes parâmetros: 'GUI' ou 'CLI'...\n")
    print(e)
    quit()

if argv[1] == "CLI":
    from controlador_cli import ControladorCli
    app = ControladorCli()

else:
    from gui import Gui
    app = Gui()    
    app.geometry("980x640")
    app.after(1000, interface.atualiza_nomes)
    
    app.mainloop()
    app.fim()
        
