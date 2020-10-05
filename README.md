# Desafio Pública Tecnologia - 2020

Aplicativo de registro de pontuações desenvolvido conforme solicitado no processo seletivo realizado pela ProWay.

O programa possui duas interfaces: gráfica e por linha de comando.

# Requisitos
Python 3 e os seguintes módulos:

-- sqlite3

-- tabulate

-- pathvalidate

-- datetime

-- tkinter

-- PIL

-- matplotlib (versão 3.0.3)

-- unittest

-- os

-- sys

# Como iniciar
Utilize o arquivo inicializador.py acompanhado de um argumento.

Para iniciar em linha de comando:
python inicializador.py CLI

Para iniciar interface gráfica:
python inicializador.py GUI

# Documentação
Encontra-se na pasta Misc\Docs, gerada através do pydoc.

A interface gráfica possui um tutorial para cada uma das funcionalidades do programa.

# Testes unitários
Localizados nos scripts que começam por "testes_", onde utilizou-se o framework unittest.

# Descrição
Neste programa buscou-se utilizar o princípio da separação de responsabilidades, mais precisamente através do modelo MVC.

O script banco.py atua como modelo do banco de dados;

Os scripts cli.py e gui.py atuam como visões;

Os scripts controlador_gui.py e controlador_cli.py atuam como controladores.

# Observação
Testado somente em ambiente Windows.

Já foi criado um banco de dados chamado "Maria.db", o qual foi populado conforme tabela que consta no enunciado do Desafio.
