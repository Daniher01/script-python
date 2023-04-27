import pandas as pd

"""MODIFICAR EL CSV Y AJUSTA QUITANDO LAS ; SOBRANTES
LUEGO GENERAR OTRO CSV YA AJUSTADO"""
    
    
def convertir_datos_pacientes(path_input, path_output):
    df = pd.read_csv(path_input, sep=',')
    rut_filtrado = list(set(df['RUT']))
    nuevo_df = []
    
    print(f'cantidad de filas antes : {len(df)}')
    print(f'cantidad de filas despues {len(rut_filtrado)}')
    
    print('leyendo los datos')
    print('Espere...')
    for index in df.index:
        if df['RUT'][index] in rut_filtrado:
            nuevo_df.append(df.iloc[index])
            #eliminar el dato del conjunto
            rut_filtrado.remove(df['RUT'][index])
    print('Datos filtrados con exito')        
                   
    
    data = pd.DataFrame(nuevo_df)
    data.to_csv(path_output, index = False) #ajustar al nombre del archivo
    return path_output

