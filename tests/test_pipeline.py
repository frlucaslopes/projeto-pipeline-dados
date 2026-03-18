import pandas as pd
from src.pipeline import calcular_faturamento

def test_calculo_faturamento():
    df = pd.DataFrame({
        "preco": [10, 20],
        "quantidade": [2, 3]
    })

    resultado = calcular_faturamento(df)

    assert resultado["faturamento"].tolist() == [20, 60]