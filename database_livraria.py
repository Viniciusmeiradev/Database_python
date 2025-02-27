import sqlite3

#Classes de referencia das tabelas em modelo def 
class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Pedido:
    def __init__(self, cliente_id, livro_id, quantidade, data_pedido):
        self.cliente_id = cliente_id
        self.livro_id = livro_id
        self.quantidade = quantidade
        self.data_pedido = data_pedido

#Conexao com banco de dados com a def
def conectar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

#Criar tabelas com a def
def criar_tabela(conexao):
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS livros(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   autor TEXT NOT NULL,
                   preco REAL NOT NULL
                   );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL
                    );''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_id INTEGER NOT NULL,
                    livro_id INTEGER NOT NULL,
                    quantidade INTEGER NOT NULL,
                    data_pedido TEXT NOT NULL,
                    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                    FOREIGN KEY (livro_id) REFERENCES livros(id)
                    );''')

    conexao.commit()
    cursor.close()

def inserir_dados(conexao):
    cursor = conexao.cursor()

    livros =[Livro('Nunca Minta', 'Freida MCFADDEN', 53.99),
            Livro('A Metamorfose', 'Franz Kafta', 13.80),
            Livro('Habitos Atomicos', 'James Clear', 42.90),
            Livro('A Unica Coisa', 'Gary Keller', 31.50)]

    clientes = [Cliente('Alice', 'alice@gmail.com'),
                Cliente('Diego', 'diego@gmail.com'),
                Cliente('Estefani', 'estefani@gmail.com'),
                Cliente('Lucas', 'lucas@gmail.com')]

    pedidos = [Pedido(1, 2, 2, '2025-02-05'),
                Pedido(2, 4, 1, '2025-02-06'),
                Pedido(3, 1, 5, '2025-02-07'),
                Pedido(4, 3, 1, '2025-02-07')]

    for livro in livros:
        cursor.execute('''INSERT INTO livros (titulo, autor, preco)
                        VALUES (:titulo, :autor, :preco)''', vars(livro))
    
    for cliente in clientes:
        cursor.execute('''INSERT INTO clientes(nome, email)
                        VALUES (:nome, :email)''', vars(cliente))
    
    for pedido in pedidos:
        cursor.execute('''INSERT INTO pedidos(cliente_id, livro_id, quantidade, data_pedido)
                        VALUES (:cliente_id, :livro_id, :quantidade, :data_pedido)''', vars(pedido))
    
    conexao.commit()
    cursor.close()


def exibir_pedidos(conexao):
    cursor = conexao.cursor()
    
    query = '''SELECT pedidos.id, clientes.nome, livros.titulo, pedidos.quantidade, pedidos.data_pedido
            FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id
            JOIN livros ON pedidos.livro_id = livros.id;'''
    
    cursor.execute(query)
    pedid = cursor.fetchall()
    print('Pedidos: ')
    for p in pedid:
        print(p)


if __name__=='__main__':
    conexao = conectar_banco('livraria.db')
    criar_tabela(conexao)
    inserir_dados(conexao)
    exibir_pedidos(conexao)
    conexao.close() 
