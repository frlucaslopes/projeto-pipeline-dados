import pandas as pd

def calcular_faturamento(df):
    df["faturamento"] = df["preco"] * df["quantidade"]
    return df

def carregar_dados(caminho):
    return pd.read_csv(caminho)

def salvar_dados(df, caminho_saida):
    df.to_csv(caminho_saida, index=False)

def executar_pipeline():
    df = carregar_dados("data/vendas.csv")
    df = calcular_faturamento(df)
    salvar_dados(df, "data/output.csv")

if __name__ == "__main__":
    executar_pipeline()