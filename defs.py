

from pandas_datareader import data
import numpy as np 
import pandas as pd


def precos_diarios(END_DATE, START_DATE, tickers):

    listaPrecos = []

    for ticker in tickers:

        df = data.DataReader('{}.SA'.format(ticker), 'yahoo', start=START_DATE, end=END_DATE)['Close']

        listaPrecos.append(df)
                               
    return listaPrecos



def variacoes_diarias(listaPrecos):
    
    lista_variacoes = []

    for precosDiarios in listaPrecos:

        lista_var_local = []

        for n in range(len(precosDiarios) - 1):
            var = (precosDiarios[n + 1] * 100 / precosDiarios[n]) - 100

            lista_var_local.append(var)

        lista_variacoes.extend(lista_var_local)

    array_variacoes = np.array(lista_variacoes)

    return array_variacoes


def separar_dataframe(df):
    receitas_trimestrais_2020 = []  

    for c in range(0, 200, 20):
        receitas_trimestrais_2020.append(df.iloc[16 + c:20 + c])

    df_2020 = pd.concat(receitas_trimestrais_2020) 

    df_2016_2019 = df.iloc[np.delete(np.array(df.index), np.array(df_2020.index))]

    df_2020.index = np.arange(len(df_2020.index))

    df_2016_2019.index = np.arange(len(df_2016_2019.index))

    
    return df_2020, df_2016_2019
