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

Neste programa, uma tabela do SQLite é uma temporada, sendo possível adicionar e remover temporadas que são numeradas de 1 a 10.000.

Além disso, é possível através do programa criar e deletar bancos de dados.

Na interface gráfica é possível transitar pelos BDs sem sair da aplicação. Aqui também foi implementado um gráfico que acompanha a evolução das pontuações ao longo da temporada, utilizando-se da biblioteca matplotlib.

A cada tabela gera-se uma segunda tabela com informações baseadas na primeira, como soma dos placares da temporada, média desses placares, top 5 melhores e piores e as somas de cada um desses top 5.

# Observações
Testado somente em ambiente Windows.

Já foi criado um banco de dados chamado "Maria.db", o qual foi populado conforme tabela que consta no enunciado do Desafio.
