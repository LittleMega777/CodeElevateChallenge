import pandas as pd
import sqlite3


df_info_transportes = pd.read_csv('info_transportes.csv',
                sep=';',
                encoding='utf-8',
                )

df_info_transportes['DT_REFE'] = pd.to_datetime(df_info_transportes['DATA_INICIO'], format='%m-%d-%Y %H:%M')\
                                    .dt.strftime('%Y-%m-%d')

count_por_negocio = lambda campo: (campo == 'Negocio').sum()
count_por_pessoal = lambda campo: (campo == 'Pessoal').sum()
count_por_reuniao = lambda campo: (campo == 'Reunião').sum()
count_nao_reuniao_declarado = lambda campo: ((campo.notna()) & (campo != 'Reunião')).sum()

df_info_corridas_do_dia = df_info_transportes.groupby('DT_REFE').agg(
    QT_CORR=('DATA_INICIO', 'count'),
    QT_CORR_NEG=('CATEGORIA', count_por_negocio),
    QT_CORR_PESS=('CATEGORIA', count_por_pessoal),
    VL_MAX_DIST=('DISTANCIA', 'max'),
    VL_MIN_DIST=('DISTANCIA', 'min'),
    VL_AVG_DIST=('DISTANCIA', 'mean'),
    QT_CORR_REUNI=('PROPOSITO', count_por_reuniao),
    QT_CORR_NAO_REUNI=('PROPOSITO', count_nao_reuniao_declarado)
    ).reset_index()

conexao_database = sqlite3.connect(':memory:')

df_info_corridas_do_dia.to_sql('info_corridas_do_dia' ,conexao_database,  if_exists='replace', index=False)

df_info_corridas_lida_sql = pd.read_sql('SELECT * FROM info_corridas_do_dia', conexao_database)

print(df_info_corridas_lida_sql)
