from leitura_dados import ler_dados
from tratamento_dados import tratar_dados

from pyspark.sql.functions import sum, desc, concat_ws, col
import matplotlib.pyplot as plt


class GraficosBolsaFamilia:

    def __init__(self, caminho_csv):
        self.caminho_csv = caminho_csv
        self.df = None
        self.df_tratado = None

    def carregar_dados(self):
        self.df = ler_dados(self.caminho_csv)
        self.df_tratado = tratar_dados(self.df)

    # -------------------------------
    # Gráfico 1 – Top 5 UFs
    # -------------------------------
    def grafico_top_ufs(self):

        df_top_ufs = (
            self.df_tratado
            .groupBy("uf")
            .agg(sum("valor_parcela").alias("total_pago"))
            .orderBy(desc("total_pago"))
            .limit(5)
        )

        pdf = df_top_ufs.toPandas()

        plt.figure()
        plt.bar(pdf["uf"], pdf["total_pago"])
        plt.title("Top 5 UFs com maior valor total pago")
        plt.xlabel("UF")
        plt.ylabel("Total Pago")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("grafico_top_ufs.png")
        plt.close()

    # -------------------------------
    # Gráfico 2 – Evolução temporal
    # -------------------------------
    def grafico_evolucao_tempo(self):

        df_tempo = (
            self.df_tratado
            .groupBy("ano_competencia", "mes_competencia_num")
            .agg(sum("valor_parcela").alias("total_pago"))
            .orderBy("ano_competencia", "mes_competencia_num")
        )

        df_tempo = df_tempo.withColumn(
            "ano_mes",
            concat_ws("-", col("ano_competencia"), col("mes_competencia_num"))
        )

        pdf = df_tempo.toPandas()

        print(pdf)  # debug

        plt.figure()
        plt.plot(pdf["ano_mes"], pdf["total_pago"])
        plt.title("Evolução do valor total pago ao longo do tempo")
        plt.xlabel("Ano/Mês")
        plt.ylabel("Total Pago")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("grafico_evolucao.png")
        plt.close()


# -------------------------------
# Execução
# -------------------------------
if __name__ == "__main__":

    caminho = "dados/NovoBolsaFamilia24.csv"

    graficos = GraficosBolsaFamilia(caminho)

    graficos.carregar_dados()
    graficos.grafico_top_ufs()
    graficos.grafico_evolucao_tempo()