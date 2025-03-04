import sqlite3 as conector

conexao = conector.connect("./database_concessionaria")        #Abrir conexao com o banco
cursor = conexao.cursor()

#Criar tabela cliente
comando1 = '''CREATE TABLE cliente(
            cpf INTEGER NOT NULL,
            nome TEXT NOT NULL,
            nascimento DATE NOT NULL,
            oculos BOOLEAN NOT NULL,
            PRIMARY KEY (cpf)
            );'''

cursor.execute(comando1)

#Criar tabela marca
comando2 = '''CREATE TABLE marca(
            id INTEGER NOT NULL,
            nome TEXT NOT NULL,
            sigla CHARACTER NOT NULL,
            PRIMARY KEY (id)
            );'''

cursor.execute(comando2)

#Criar tabela veiculo
comando3 = '''CREATE TABLE veiculo(
            placa CHARACTER(7) NOT NULL,
            ano INTEGER NOT NULL,
            cor TEXT NOT NULL,
            motor REAL NOT NULL,
            proprietario INTEGER NOT NULL,
            marca INTEGER NOT NULL,
            PRIMARY KEY (placa),
            FOREIGN KEY (proprietario) REFERENCES cliente(cpf),
            FOREIGN KEY (marca) REFERENCES marca(id)
            );'''

cursor.execute(comando3)

#Inserir valores na tabela cliente
comando4 = '''INSERT INTO cliente (cpf, nome, nascimento, oculos)
            VALUES (968585754464, 'Carla','2000-05-12', 1),
            (747532798631, 'Diego','2007-01-10', 1),
            (243423413434, 'Estefani','2003-09-06',0),
            (865335665434, 'Cleiton', '1999-06-24', 0);'''

cursor.execute(comando4)

conexao.commit()                #Salvar as execucoes

cursor.close()                  #Fechar o cursor
conexao.close()                 #Fechar conexao
