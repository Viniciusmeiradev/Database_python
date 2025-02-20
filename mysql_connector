import mysql.connector as conector

conexao = conector.connect("URL do MySQL")        #Abertura de conexao
cursor = conexao.cursor()                         #Aquisição de um cursor
cursor.execute("....")                            #Execucao dos comandos
cursor.fetchall()                                 #Retorna as linhas do banco
conexao.commit()                                  #Confirmar alteração
cursor.close()                                    #Fechamento de cursor
conexao.close()                                   #Fechamento de conexao
