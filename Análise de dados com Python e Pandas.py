#ANÁLISE 1, utilizando dados demográficos:

# Análise de dados com a biblioteca Pandas, uma biblioteca Python de código aberto para análise de dados:
# Pandas permite ao Python a capacidade de trabalhar com dados do tipo planilha, permitindo carregar, manipular e combinar dados rapidamente, entre outras funções.

# Primeiro passo, importando pandas
import pandas as pd

#,error_bad_lines=False (ignora linha com erros)
# e sep =";" (para que o separador ; seja lido pelo pandas e melhor organize a planilha
df = pd.read_csv('Gapminder.csv',error_bad_lines=False, sep=";")

#Visualizando as 5 primeiras linhas:
df.head()

#Trocando nome das colunas
df = df.rename(columns={"country": "País", "continent": "Continente", "year": "Ano", "lifeExp": "Expectativa de Vida", "pop":"Pop Total", "gdpPercap": "PIB"})


#Visualizando as 10 primeiras linhas:
df.head(10)

#Total de linhas e colunas
df.shape

#Retornando título das colunas
df.columns

#Tipo de dados em cada coluna
df.dtypes

#Retornando ultimas linhas
df.tail(15)

#Estatística
df.describe()

#Fazendo filtros, buscando valores únicos p coluna especifica "continente"
df["Continente"].unique()

#Filtrando "Oceania" apos listar continentes
Oceania = df.loc[df["Continente"] == "Oceania"]
Oceania.head()

#Agrupando para saber países por continente
df.groupby("Continente")["País"].unique()

df.groupby("Ano")["Expectativa de Vida"].mean()

#Média do Pib
df["PIB"].mean()



#Soma do Pib
df["PIB"].sum()

#ANÁLISE 2, utilizando base de vendas:
#Análise de dados oriundos do excel
#Biblioteca pandas já importada conforme análise 1


# Lendo os arquivos base em excel
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")


# Mostrando as 5 primeiras linas do arquifo df1 e demais p confirmar sequência de colunas
df1.head()

# Unindo as 5 tabelas para formar único arquivo
df = pd.concat([df1,df2,df3,df4,df5])

# Primeiras 5 linhas com arquivo agrupado
df.head()



# Ultimas 5 linhas com arquivo agrupado
df.tail()



# Tipo de dados das colunas
df.dtypes

# Amostra de dados em 5 linhas
df.sample(5)



# Alterando tipo de dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")



# Revendo tipo de dados 
df.dtypes

# Tratando valores faltantes (nulos)
df.isnull().sum()



# Substituindo os valores nulos pela média
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)



# Confirmando correção dos valores faltantes (nulos)
df.isnull().sum()



# Substituindo valores nulos por zero
df["Vendas"].fillna(0, inplace=True)



# Apagando linhas com valores nulos
df.dropna(inplace=True)



# Apagando as linhas com valores nulos com base em 1 coluna
df.dropna(subset=["Vendas"], inplace=True)



# Removendo linhas que estejam com valores faltantes em todas colunas
df.dropna(how="all", inplace=True)

# Criando colunas novas
# Criando coluna de receita
df["Receita"] = df["Vendas"].mul(df["Qtde"])


#Visualizando
df.head()


# Criando coluna com resultado divisão (Receita x Vendas)
df["Receita/Vendas"] = df["Receita"] / df ["Vendas"]



# Visualizando alterações
df.head()



# Retornando a maior receita
df["Receita"].max()

# Retornando a menor receita
df["Receita"].min()



# Comando "nlargest" para saber o TOP 3 da coluna "Receita"
df.nlargest(3, "Receita")



# Comando "nsmallest" para saber os 3 piores da coluna "Receita"
df.nsmallest(3, "Receita")



# Agrupamento por cidade
df.groupby("Cidade")["Receita"].sum()

# Para ordenar o conjunto de dados usando como base coluna "Receita"
# "ascending=False" p classificar do maior para o menor
# "head(10)" p mostrar 10 primeiras linhas
df.sort_values("Receita", ascending=False).head(10)

#ANÁLISE 3, trabalhando com datas:

# Transformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")




# Transformando coluna de data em data
df["Data"] = pd.to_datetime(df["Data"])



# Visualizando o formato dos dados
df.dtypes



# Agrupamento da "Receita" por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()



# Criando uma nova coluna com ano
df["Ano_Venda"] = df["Data"].dt.year



# Vendo 5 linhas
df.sample(5)



# Extraindo o mês e dia
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)



# Vendo 5 linhas
df.sample(5)

# Data mais antiga
df["Data"].min()



# Calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()



# Vendo 5 linhas
df.sample(5)



# Criando a coluna de trimestre
df["trimestre_venda"] = df["Data"].dt.quarter



# Visualizando 5 linhas trimestre
df.sample(5)



# Filtrando as vendas de 2019 do mes de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]



# Amostra vendas março 2019
vendas_marco_19

# Amostra das 20 vendas março 2019
vendas_marco_19.sample(20)

#ANÁLISE 4, visualização de dados:
# Value _counts somando e organizando as vendas decrescente
df["LojaID"].value_counts(ascending=False)

# Gráfico de barras decrescente
df["LojaID"].value_counts(ascending=False).plot.bar()



# Gráfico de barras horizontais decrescente
df["LojaID"].value_counts().plot.bar()



# Gráfico de barras horizontais decrescente e para retirar linha só colocar ";" ao final do código
df["LojaID"].value_counts(ascending=True).plot.barh()



# Gráfico de Pizza
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

# Total de vendas por cidade
df["Cidade"].value_counts()



# Incluindo título e alterando nome dos eixos
import matplotlib.pyplot as plt
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

# Alterando a cor das barras
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

# Alterando estilo do gráfico
# Site para códigos gráficos: https://matplotlib.org/3.2.1/gallery/
# Usando modelo ggplot
plt.style.use("ggplot")

df.groupby(df["mes_venda"])["Qtde"].sum().plot()
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend();

# Colocando o título no gráfico
df.groupby(df["mes_venda"])["Qtde"].sum().plot(title = "Total Produtos Vendidos x Mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend()

# Agrupando quantidade por mês
df.groupby(df["mes_venda"])["Qtde"].sum()




# Selecionando somente vendas 2019
df_2019 = df[df["Ano_Venda"] == 2019]



# Total produtos vendidos por mês
# "v" letra v minusculo = muda o marcador do gráfico para V
# "*" simbolo asterisco = muda o marcador para *
# "o" letra v minusculo = muda o marcador do gráfico para bolinha
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend()

# "*" simbolo asterisco = muda o marcador para *
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "*")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend()

# "o" letra v minusculo = muda o marcador do gráfico para bolinha
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "o")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend()

# Histograma
# Cores que podemos usar no site https://matplotlib.org/examples/color/named_colors.html
plt.hist(df["Qtde"], color="dodgerblue");

# Usando gráfico de disperção
plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"]);

# Salvando imagens e gráficos "plt.savefig("Nome-arquivo.png")
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend()
plt.savefig("Gráfico Qtd x Mes.png")

#ANÁLISE 5, análise exploratória:

# Importando bibliotecas
# "pandas" para análise de dados
# "matplotlib" para visualização de dados
# "seaborn" também para visualização de dados ou somente estilo como neste exemplo
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

# Upload arquivos via comando ou como preferir
#from google.colab import files
#arq = files.upload()

# Criando DataFrame
df = pd.read_excel("AdventureWorks.xlsx")

# Vendo 5 linhas
df.head()

# Vendo quantidade de linhas e colunas
df.shape

# Verificando os tipos de dados
df.dtypes

# Receita total?
df["Valor Venda"].sum()

# Custo total
# Criando coluna custo
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"])

# Visualizando nova coluna
df.head(1)

# Arredondando custo total
# Passando "round" para arredondar em 2 casas decimais
round(df["custo"].sum(), 2)

# Coluna lucro (receita - custo)
df["lucro"] = df["Valor Venda"] - df["custo"]

df.head(1)

# Lucro Total
round(df["lucro"].sum(), 2)

# Coluna "Tempo de envio" do produto
df["Tempo_envio"] = df["Data Envio"] - df ["Data Venda"]

df.head(1)

# Média do tempo de envio por marca
# Transformando coluna "Tempo_envio" em númerica, pois na coluna consta números e texto
# Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days


df.head(1)

# Verificando o tipo de dados para coluna "Tempo_envio"
df["Tempo_envio"].dtype

# Média do tempo de envio por marca
df.groupby("Marca")["Tempo_envio"].mean()

# Valores ausentes (missing values)
# Verificando se temos dados faltantes
df.isnull().sum()

# Lucro por ano e marca
# Agrupando coluna "Data Venda" por ano e marca. E tambpem a coluna "Lucro" por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()

pd.options.display.float_format = '{:20,.2f}'.format

# Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_ano

# Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

# Gráfico total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

# Selecionando apenas as vendas 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.head()

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

df["Tempo_envio"].describe()

# Gráfico de Boxplot
plt.boxplot(df["Tempo_envio"]);

# Histograma
plt.hist(df["Tempo_envio"]);

# Tempo mínimo de envio
df["Tempo_envio"].min()

# Tempo máximo de envio
df["Tempo_envio"].max()

# Identificando o Outlier (discrepância)
df[df["Tempo_envio"] == 20]

# Salvando a análise em formato csv
df.to_csv("df_Analise_Nordeste.csv", index=False)