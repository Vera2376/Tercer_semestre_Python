import  psycopg2 as bd

conexion = bd.connect(user= 'postgres', password= '1704', host= '127.0.0.1', port= '5432', database= 'test_bd')
try:
    #conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, mail) VALUES (%s, %s, %s)'
    valores = ('María', 'Esparza', 'mesparza@mail.mail.com')
    cursor.execute(sentencia, valores)
    conexion.commit() #Hacemos el commit manualmente
    print('Termina la transacciòn')
except Exception as e:
    print(f'Ocurrio un error: {e}')
    conexion.rollback()
finally:
    conexion.close() 