import pandas as pd

df_info_transportes = pd.read_csv('info_transportes.csv',
                 sep=';',
                 encoding='utf-8',
                 )

df_info_transportes['DATA_INICIO'] = pd.to_datetime(df_info_transportes['DATA_INICIO']).dt.strftime('%Y-%m-%d')
# df_info_transportes_corridos = df_info_transportes['DATA_INICIO']



print(df_info_transportes[['DATA_INICIO', 'LOCAL_INICIO', 'LOCAL_FIM', 'DISTANCIA', 'PROPOSITO']].head(10))