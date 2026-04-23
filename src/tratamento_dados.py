from pyspark.sql.functions import col, regexp_replace, substring

def tratar_dados(df):
    df_tratado = df

    # 2.1 Padronização correta
    colunas_padrao = {
        "MÊS COMPETÊNCIA": "mes_competencia",
        "MÊS REFERÊNCIA": "mes_referencia",
        "UF": "uf",
        "CÓDIGO MUNICÍPIO SIAFI": "codigo_municipio_siafi",
        "NOME MUNICÍPIO": "nome_municipio",
        "CPF FAVORECIDO": "cpf_favorecido",
        "NIS FAVORECIDO": "nis_favorecido",
        "NOME FAVORECIDO": "nome_favorecido",
        "VALOR PARCELA": "valor_parcela"
    }

    for antiga, nova in colunas_padrao.items():
        df_tratado = df_tratado.withColumnRenamed(antiga, nova)

    # 2.3 Tratamento valor
    df_tratado = df_tratado.withColumn(
        "valor_parcela",
        regexp_replace(col("valor_parcela"), '"', '')
    )

    df_tratado = df_tratado.withColumn(
        "valor_parcela",
        regexp_replace(col("valor_parcela"), ",", ".").cast("decimal(10,2)")
    )

    # 2.2 Criação de colunas
    df_tratado = df_tratado \
        .withColumn("ano_competencia", substring(col("mes_competencia"), 1, 4)) \
        .withColumn("mes_competencia_num", substring(col("mes_competencia"), 5, 2)) \
        .withColumn("ano_referencia", substring(col("mes_referencia"), 1, 4)) \
        .withColumn("mes_referencia_num", substring(col("mes_referencia"), 5, 2))

    # 2.4 Limpeza
    df_tratado = df_tratado.dropna()

    return df_tratado