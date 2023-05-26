import  psycopg2 as bd

conexion = bd.connect(user= 'postgres', password= '1704', host= '127.0.0.1', port= '5432', database= 'test_bd')
try:
    conexion.autocommit = False #Esto directamente no debería estar
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, mail) VALUES (%s, %s, %s)'
    valores = ('Jorge', 'Prol', 'jprol@mail.mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDETE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores= ('Juan Carlos', 'Pérez', 'jcperez@mail.com', 1)
    cursor.execute(sentencia, valores)

    conexion.commit() #Hacemos el commit manualmente, acá se cierra manualmente la transacción
    print('Termina la transacciòn')
except Exception as e:
    print(f'Ocurrio un error: {e}')
    conexion.rollback()
finally:
    conexion.close()