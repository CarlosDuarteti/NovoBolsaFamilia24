from leitura_dados import ler_dados
from tratamento_dados import tratar_dados
from graficos import GraficosBolsaFamilia
import matplotlib
matplotlib.use('TkAgg')
from pyspark.sql.functions import sum, avg, countDistinct, desc

caminho_csv = "dados/NovoBolsaFamilia24.csv"

df = ler_dados(caminho_csv)

df_tratado = tratar_dados(df)

df_tratado.show(5)
df_tratado.printSchema()

# 3.1 Faturamento total
df_tratado.agg(
    sum("valor_parcela").alias("total_pago")
).show()

# 3.2 Média geral
df_tratado.agg(
    avg("valor_parcela").cast("decimal(10,2)").alias("media_pagamento")
).show()

# Média por UF
df_tratado.groupBy("uf").agg(
    avg("valor_parcela").cast("decimal(10,2)").alias("media_por_uf")
).show()

# Média por cpf_favorecido
df_tratado.groupBy("cpf_favorecido").agg(
    avg("valor_parcela").cast("decimal(10,2)").alias("media_por_cpf")
).show(5, truncate=False)

# 3.3 Ranking dos estados
df_tratado.groupBy("uf") \
    .agg(sum("valor_parcela").alias("total_pago")) \
    .orderBy(desc("total_pago")) \
    .show(5)

# 3.4 Ranking por CPF (Top 10)
df_tratado.groupBy("cpf_favorecido") \
    .agg(sum("valor_parcela").alias("total_recebido")) \
    .orderBy(desc("total_recebido")) \
    .show(10)

# 3.5 Quantidade de beneficiários
df_tratado.select("cpf_favorecido").distinct().count()

df_tratado.groupBy("uf") \
    .agg(countDistinct("cpf_favorecido").alias("qtd_beneficiarios")) \
    .show()

graficos = GraficosBolsaFamilia(caminho_csv)

graficos.carregar_dados()
graficos.grafico_top_ufs()
graficos.grafico_evolucao_tempo()