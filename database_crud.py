import psycopg2

#Criar o banco de dados

#Abertura de conexao
conexao=psycopg2.connect(
    host='localhost',
    database='postgresDB',
    user='admin',
    password='admin123'
)

#Criacao do cursor do banco de dados
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS public."AGENDA"(
    id integer NOT NULL, 
    nome text COLLATE pg_catalog."default" NOT NULL, 
    telefone char(12) COLLATE pg_catalog."default" NOT NULL)
    
    TABLESPACE pg_default;
    ALTER TABLE public."AGENDA" OWNER to Admin;""")

#Inserir dados na tabela
cursor.execute("""INSERT INTO public."AGENDA"(id, nome, telefone)
                VALUES(1, 'teste 1', '021999999999'),
                        (2, 'teste 2', '021888888888'); """)

conexao.commit()

#Ler os dados
cursor.execute("""SELECT id, nome, telefone FROM public."AGENDA"; """)
rows=cursor.fetchall()
for row in rows:
    print(f'ID: {row[0]}, NOME: {row[1]}, TELEFONE: {row[2]}')
conexao.commit()

#Fechar conexao
cursor.close()
conexao.close()




#Fazer update na tabela

conexao = psycopg2.connect(host = 'localhost', database='postgresDB', user='admin', password='admin123')
cursor = conexao.cursor()

#Atualização dados na tabela
cursor.execute("""UPDATE public."AGENDA"
                SET nome = 'teste atualizado' 
                WHERE id = 1; """)
conexao = commit()

#Ler os dados atualizados
cursor.execute("""SELECT id, nome, telefone FROM public."AGENDA"; """)
rows = cursor.fetchall()
for row in rows:
    print(f'ID: {row[0]}, NOME: {row[1]}, TELEFONE: {row[2]}')

cursor.close()
conexao.close()




#Função de deletar

conexao = psycopg.connect(host="localhost", database="postgresDB", user="admin", password='admin123')
cursor = cursor.cursor()

#Excluir dados
cursor.execute("""DELETE FROM public."AGENDA
                WHERE id=1; """)
conexao.commit()

#Ler os dados atualizados
cursor.execute(""" SELECT id, nome, telefone FROM public."AGENDA"; """)
rows=cursor.fetchall()
for row in rows:
    print(f'ID: {row[0]}, NOME: {row[1]}, TELEFONE: {row[2]}')

#Fechar a conexao
cursor.close()
conexao.close()
