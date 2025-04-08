import pandas as pd





if __name__ == "__main__":
    
    df_info_transportes = pd.read_csv('info_transportes.csv',
                    sep=';',
                    encoding='utf-8',
                    )

    df_info_transportes['DT_REFE'] = pd.to_datetime(df_info_transportes['DATA_INICIO'], format='%m-%d-%Y %H:%M').dt.strftime('%Y-%m-%d')

    df_info_corridas_do_dia = df_info_transportes.groupby('DT_REFE').agg(
        QT_CORR=('DATA_INICIO', 'count'),
        QT_CORR_NEG=('CATEGORIA', lambda x: (x == 'Negocio').sum()),
        QT_CORR_PESS=('CATEGORIA', lambda x: (x == 'Pessoal').sum()),
        VL_MAX_DIST=('DISTANCIA', 'max'),
        VL_MIN_DIST=('DISTANCIA', 'min'),
        VL_AVG_DIST=('DISTANCIA', 'mean'),
        QT_CORR_REUNI=('PROPOSITO', lambda x: (x == 'Reunião').sum()),
        QT_CORR_NAO_REUNI=('PROPOSITO', lambda x: ((x.notna()) & (x != 'Reunião')).sum())
    ).reset_index()

    print(df_info_corridas_do_dia.head(10))