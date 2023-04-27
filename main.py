import pandas as pd
import filtrado_datos

def convertirCVSaSQL(input_path, output_path):
    """
    Convierte los datos del CSV en datos de SQL generando un nuevo archivo .sql
    
    input_path -> path
    output_path -> path
    
    return pass
    """

    df = pd.read_csv(input_path, sep=',')
    
        # ? convertir columna 'FECHA DE INGRESO' en datetaime
    df['FECHA DE INGRESO'] = pd.to_datetime(df['FECHA DE INGRESO'], format='%d/%m/%Y')
    # ? cambiar formato de fecha en el dataframe
    df['FECHA DE INGRESO'] = df['FECHA DE INGRESO'].dt.strftime('%Y-%m-%d')
    
    print(df)
    print('---------------')
    

    lista_query = []
    codigo_empleado = 1
    for i in df.index:

        # ? ejemplo de query
        # query = "INSERT INTO email (idemail, email) \
        #    VALUES ('{}',{});".format(df['nombres'][i],df['idemail'][i])

        query = "INSERT INTO empleado (idempleado, nombre, sucursal, empresa, cargo, fecha_ingreso) \
                    VALUES ({}, '{}', '{}', '{}', '{}', '{}');".format(codigo_empleado, df['NOMBRE'][i], df['SUCURSAL'][i], df['Empresa'][i], df['CARGO'][i], df['FECHA DE INGRESO'][i])

        query2 = "INSERT INTO dias_admin(iddias_admin, empleado_idempleado, cantidad_dias, anio) \
                    VALUES ({}, {}, 5, '2023-05-01');".format(codigo_empleado,codigo_empleado)

        lista_query.append(query)
        lista_query.append(query2)
        codigo_empleado = codigo_empleado + 1


    data = pd.DataFrame(lista_query)

    data.to_csv(output_path, index = False) #ajustar al nombre del archivo
    #print(data)
    print('Archivo convertido con exito')


if __name__ == "__main__": 
    try:
        #filtra los datos a un nuevo csv
        #nuevo_path = filtrado_datos.convertir_datos_pacientes('archivos csv/Pacientes talca 2022 total.csv','archivos csv/PACIENTES TALCA 2022 FILTRADOS.csv')
        #convierte los datos a sql
        convertirCVSaSQL('archivos csv/Lista empleados.csv', 'archivos sql/insert empleados.sql')
    except (RuntimeError, TypeError, NameError,BaseException ) as e:
        print('ocurrio el siguiente error: ')
        print(e)