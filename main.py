import pandas as pd
import filtrado_datos


def convertirCVSaSQL(input_path, output_path, separador = ','):
    """
    Convierte los datos del CSV en datos de SQL generando un nuevo archivo .sql

    input_path -> path
    output_path -> path

    return pass
    """

    df = pd.read_csv(input_path, sep=separador)

    print(df)
    print('---------------')

    lista_query = []
    codigo_empleado = 1
    for i in df.index:

        # ? ejemplo de query
        # query = "INSERT INTO email (idemail, email) \
        #    VALUES ('{}',{});".format(df['nombres'][i],df['idemail'][i])

        query = "INSERT INTO analisis_cefalo (idanalisis_cefalo, orden_idorden, prestaciones_idprestaciones, ruta_analisis_1, ruta_analisis_2, ruta_analisis_3) VALUES ({}, {}, {}, '{}','{}', '{}');".format(
             df['idanalisis_cefalo'][i], df['orden_idorden'][i],df['prestaciones_idprestaciones'][i], df['ruta_analisis_1'][i], df['ruta_analisis_2'][i], df['ruta_analisis_3'][i])

        lista_query.append(query)
        # codigo_empleado = codigo_empleado + 1

    data = pd.DataFrame(lista_query)

    data.to_csv(output_path, index=False)  # ajustar al nombre del archivo
    # print(data)
    print('Archivo convertido con exito')


if __name__ == "__main__":
    try:
        # filtra los datos a un nuevo csv
        # nuevo_path = filtrado_datos.convertir_datos_pacientes('archivos csv/Pacientes talca 2022 total.csv','archivos csv/PACIENTES TALCA 2022 FILTRADOS.csv')
        # convierte los datos a sql
        convertirCVSaSQL('archivos csv/data_analisis_cefalo.csv',
                         'archivos sql/insert_analisis_cefalo.sql', ',')
    except (RuntimeError, TypeError, NameError, BaseException) as e:
        print('ocurrio el siguiente error: ')
        print(e)
