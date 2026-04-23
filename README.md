# 📊 Projeto de Análise de Dados – Bolsa Família (PySpark)

## 📌 Sobre o Projeto

Este projeto tem como objetivo realizar o processamento, análise e visualização dos dados do programa **Bolsa Família**, utilizando **PySpark** para lidar com grandes volumes de dados e **Matplotlib** para geração de gráficos.

O fluxo do projeto segue as etapas clássicas de um pipeline de dados:

* 📥 Leitura dos dados (CSV)
* 🧹 Tratamento e limpeza
* 📊 Análises estatísticas
* 📈 Visualizações gráficas

---

## 🛠️ Tecnologias Utilizadas

* Python 3.x
* PySpark
* Pandas
* Matplotlib

---

## 📁 Estrutura do Projeto

```
📦 projeto-bolsa-familia
 ┣ 📂 dados
 ┃ ┗ NovoBolsaFamilia24.csv
 ┣ 📂 notebooks
 ┃ ┗ analise_exploratoria.ipynb
 ┣ 📄 leitura_dados.py
 ┣ 📄 tratamento_dados.py
 ┣ 📄 analises.py
 ┣ 📄 graficos.py
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```

---

## ⚙️ Como Funciona

### 🔹 1. Leitura dos Dados

O arquivo `leitura_dados.py` cria uma sessão Spark e realiza a leitura do CSV com as configurações adequadas.

### 🔹 2. Tratamento dos Dados

O arquivo `tratamento_dados.py`:

* Padroniza nomes das colunas
* Trata valores monetários
* Cria colunas de ano e mês
* Remove dados nulos

### 🔹 3. Análises

O arquivo `analises.py` executa:

* Faturamento total
* Média de pagamentos
* Ranking de estados
* Ranking de beneficiários
* Quantidade de beneficiários

### 🔹 4. Visualizações

O arquivo `graficos.py` gera:

* 📊 Gráfico de barras (Top 5 UFs)
* 📈 Gráfico de linha (evolução no tempo)

---

## 🚀 Como Instalar o Projeto

### 🔹 1. Clonar o repositório

```bash
git clone https://github.com/CarlosDuarteti/NovoBolsaFamilia24.git
cd seu-repositorio
```

---

### 🔹 2. Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

#### Ativar no Windows:

```bash
venv\Scripts\activate
```

#### Ativar no Linux/Mac:

```bash
source venv/bin/activate
```

---

### 🔹 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 📦 Exemplo de `requirements.txt`

Caso ainda não tenha, crie um arquivo `requirements.txt` com:

```
pyspark
pandas
matplotlib
```

---

## ▶️ Como Executar

Para rodar todo o projeto:

```bash
python analises.py
```

---

## 📊 Saídas Geradas

Após a execução, serão gerados:

* 📁 `grafico_top_ufs.png`
* 📁 `grafico_evolucao.png`

---

## 📓 Notebook

O projeto também possui um notebook:

```
notebooks/analise_exploratoria.ipynb
```

Que permite visualizar:

* Dados
* Análises
* Gráficos
* Explicações em Markdown

---

## 💡 Possíveis Melhorias

* Criar dashboard interativo (Streamlit ou Power BI)
* Filtrar por região ou período
* Deploy em ambiente cloud (AWS, Azure)

---

## 👨‍💻 Autor

Carlos Duarte


