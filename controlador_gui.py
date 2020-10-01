import os
from sys import argv
from datetime import datetime


from banco import BD







class ControladorGui:    
    def __init__(self):
        self.busca_bds()


    def busca_bds(self):
        self.diretorio = os.path.dirname(__file__) + "\\BD\\"        
        self.bancos = [file for file in os.listdir(self.diretorio) if file.endswith(".db")]

