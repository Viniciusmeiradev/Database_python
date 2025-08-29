from pyspark.sql import SparkSession
import pandas as pd
import numpy as np

# Create a SparkSession
spark = SparkSession.builder.appName("example").getOrCreate()


#Ler os dados de um arquivo
dataset = spark.read.csv('/content/sample_data/california_housing_test.csv', inferSchema=True, header=True)
dataset.head

#Cria uma tabela temporaria em SQL
dataset.createOrReplaceTempView('tabela_temporaria')
print(spark.catalog.listTables())

#Consulta sql
query = 'FROM tabela_temporaria SELECT longitude, latitude LIMIT 3'
saida = spark.sql(query)
saida.show( )

#Quantidade maxima de quartos
query1 = 'SELECT MAX(total_rooms) as maximo_quartos FROM tabela_temporaria'
q_maximo_quartos = spark.sql(query1)
pd_maximo_quartos = q_maximo_quartos.toPandas()
print('A quantidade máxima de quartos é: {}'.format(pd_maximo_quartos['maximo_quartos']))
qtd_maximo_quartos = int(pd_maximo_quartos.loc[0,'maximo_quartos'])

#Obter a localizacao do bloco residencial com a maior quantidade de quartos
query2 = 'SELECT longitude, latitude FROM tabela_temporaria WHERE total_rooms = ' + str(qtd_maximo_quartos)
localizacao_maximo_quartos = spark.sql(query2)
pd_localizacao_maximo_quartos = localizacao_maximo_quartos.toPandas()
print(pd_localizacao_maximo_quartos.head())


#Converter pandas para Spark
media = 0
desvio_padrao = 0.1
pd_temporario = pd.DataFrame(np.random.normal(media, desvio_padrao, 100))
spark_temporario = spark.createDataFrame(pd_temporario)
print(spark.catalog.listTables())
spark_temporario.createOrReplaceTempView('nova_tabela_temporaria')
print(spark.catalog.listTables())