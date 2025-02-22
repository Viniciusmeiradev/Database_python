import sqlite3 

def conectar_banco(nome_banco):
    #Função para conectar-se ao banco de dados.
    conexao = sqlite3.connect(nome_banco)
    return conexao

def criar_tabelas(conexao):
    #Função para criar as tabelas Produtos, Clientes e Pedidos.
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   preco REAL NOT NULL,
                   estoque INTEGER NOT NULL
                   );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL, 
                   email TEXT NOT NULL
                   );''')
    cursor.execute(''' CREATE TABLE IF NOT EXISTS pedidos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   cliente_id INTEGER NOT NULL,
                   produto_id INTEGER NOT NULL,
                   quantidade INTEGER NOT NULL,
                   data_pedido TEXT NOT NULL,
                   FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                   FOREIGN KEY (produto_id) REFERENCES produtos(id)
                   );''')
    
    conexao.commit()

def inserir_dados(conexao):
    #Função para inserir dados nas tabelas.
    cursor = conexao.cursor()

    produtos = [('Notebook', 2999.99, 10),
                ('Smartphone', 1500.00, 20),
                ('Tablet', 799.90, 15),
                ('Teclado', 150.00, 8)]
    
    clientes = [('Alice', 'alice@gmail.com'),
                ('Bob', 'bob@gmail.com'),
                ('Charlie', 'charlie@gmail.com'),
                ('Flavia', 'flavia@gmail.com')]
    
    pedidos = [(1,2,3,'2025-01-12'),
               (2,1,1,'2025-01-13'),
               (3,4,2,'2025-01-14'),
               (4,3,5,'2025-01-15')]
    
    cursor.executemany('INSERT INTO produtos(nome, preco, estoque) VALUES (?,?,?)', produtos)

    cursor.executemany('INSERT INTO clientes(nome, email) VALUES (?,?)', clientes)

    cursor.executemany('''INSERT INTO pedidos(cliente_id, produto_id, quantidade, data_pedido) 
                       VALUES (?,?,?,?)''', pedidos)
    
    conexao.commit()
    conexao.close()


if __name__=='__main__':
    conexao = conectar_banco('data_ecomme.db')
    criar_tabelas(conexao)
    inserir_dados(conexao)
    conexao.close()
