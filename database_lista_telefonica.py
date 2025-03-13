import psycopg2
from psycopg2 import Error

#Funcao para conectar ao banco de dados
def connect_to_db():
    try:
        conexao = psycopg2.connect(host='localhost', database='postgresDB', user='admin', password='admin123')
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados PostgreSQL: {e}")
        return None

#Funcao para criar dados
def create_contact(nome, telefone):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""INSERT INTO public."AGENDA" (nome, telefone)
                            VALUES (%s, %s) RETURNING id; """, (nome, telefone))
            contact_id = cursor.fetchone()[0]
            conn.commit()
            print(f'Contato adicionado com ID: {contact_id}')
        except Error as e:
            print(f'Erro ao adicionar contato: {e}')
        finally:
            cursor.close()
            conn.close()

#Funcao para ler os dados
def read_contacts():
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT id, nome, telefone From public."AGENDA";""")
            contacts = cursor.fetchall()
            for contact in contacts:
                print(f'ID: {contact[0]}, NOME: {contact[1]}, TELEFONE: {contact[2]}')
        except Error as e:
            print("Erro ao ler contatos: {e}")
        finally:
            cursor.close()
            conn.close()

#Funcao para atualizar e inserir os dados
def update_contact(contact_id, novo_nome, novo_telefone):
    conn = connect_to_db()                                                      #Variavel que recebe a funçao de conexao
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""UPDATE public."AGENDA" 
                            SET nome = %s, telefone = s%
                            WHERE id = %s; """, (novo_nome, novo_telefone, contact_id))
            conn.commit()
            print("Contato atualizado com sucesso.")
        except Error as e:
            print(f"Erro ao atualizar contato. {e}")
        finally:
            cursor.close()
            conn.close()

def delete_contact(contact_id):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""DELETE FROM public."AGENDA"
                            WHERE id = %s; """, (contact_id))
            conn.commit()
            print("Contato deletado com sucesso.")
        except Error as e:
            print("Erro as deletar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar novo contato")
        print("2. Mostrar todos os contatos")
        print("3. Atualizar um contato")
        print("4. Deletar um Contato")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        #tratamento de opcao, pode usar o match/case
        if opcao == '1':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            create_contact(nome, telefone)
        elif opcao == '2':
            read_contacts()
        elif opcao == '3':
            contact_id = int(input('Digite o ID do contato para atualizar: '))
            novo_nome = input('Novo nome: ')
            novo_telefone = input('Novo telefone: ')
            update_contact(contact_id, novo_nome, novo_telefone)
        elif opcao == '4':
            contact_id = int(input("Digite o ID do contato que deseja deletar: "))
            delete_contact()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print('Opção inválida. Por favor, tente novamente.')

if __name__=='__main__':
    main()
