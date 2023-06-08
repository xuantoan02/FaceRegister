import mysql.connector
from mysql.connector import Error
from Backend.core import config


class RegisterFace:
    def __init__(self):


try:
    connection = mysql.connector.connect(
        host='127.0.0.1',
        database='Faces',
        user='Admin',
        password='admin'
    )
    if connection.is_connected():
        print('Connected to MySQL database')

    cursor = connection.cursor()

    insert_query = "INSERT INTO face_register (NAME, FEATURE) VALUES (%s, %s)"
    values = ("test1", "[1,2,3,5]")

    cursor.execute(insert_query, values)
    connection.commit()
    print(f'{cursor.rowcount} row(s) inserted successfully.')
except Error as e:
    print(f'Error while connecting to MySQL: {e}')
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('Connection closed.')
