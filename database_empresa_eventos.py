import sqlite3

def conectar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

def criar_tabelas(conexao):
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS locais(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   endereco TEXT NOT NULL);''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS eventos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   data TEXT NOT NULL,
                   local_id INTEGER NOT NULL,
                   FOREIGN KEY (local_id) REFERENCES locais(id));''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS participantes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL, 
                    email TEXT NOT NULL,
                    evento_id INTEGER NOT NULL,
                    FOREIGN KEY(evento_id) REFERENCES eventos(id)) ''')

    conexao.commit()

if __name__=="__main__":
    conexao = conectar_banco("eventos.db")
    criar_tabelas(conexao)
    conexao.close()
