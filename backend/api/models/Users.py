import mysql.connector
from mysql.connector import Error
from pydantic import BaseModel
from core.Security import HashAlgorithm


class User(BaseModel):
    user_name: str
    password: str


class UserManager:
    def __init__(self, host, database, admin, password, name_table):
        self.host = host
        self.database = database
        self.admin = admin
        self.password = password
        self.name_table = name_table

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.admin,
                password=self.password
            )
            if self.connection.is_connected():
                print('Connected to MySQL database')
        except Error as e:
            print(f'Error while connecting to MySQL: {e}')

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print('Connection closed.')

    def get_user(self, user_name):
        row: tuple = ()
        try:
            self.connect()
            cursor = self.connection.cursor()

            select_query = f"SELECT * FROM  {self.name_table} WHERE user_name = '{user_name}' LIMIT 1"
            cursor.execute(select_query)
            row = cursor.fetchone()
            self.connection.commit()
            if row:
                print(f"get user {user_name} success")
            else:
                print(f"{user_name} not exit")
        except Error as e:
            print(f'Error while get user: {e}')
        finally:
            if self.connection.is_connected():
                cursor.close()
        return row

    def create_user(self, user: User):

        message = None
        try:
            self.connect()
            cursor = self.connection.cursor()
            insert_query = f"INSERT INTO {self.name_table} (user_name, password) VALUES (%s, %s)"
            password_hash = HashAlgorithm().get_password_hash(user.password, 22)

            values = (user.user_name, password_hash)
            cursor.execute(insert_query, values)
            self.connection.commit()
            message = f'{cursor.rowcount} user(s) created successfully.'

        except Error as e:
            print(f'Error while creating user: {e}')
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.disconnect()
            return message

    def update_user(self, user_id, new_password):
        try:
            self.connect()
            cursor = self.connection.cursor()

            update_query = f"UPDATE {self.name_table} SET password = %s WHERE id = %s"
            values = (new_password, user_id)

            cursor.execute(update_query, values)
            self.connection.commit()

            print(f'{cursor.rowcount} user(s) updated successfully.')
        except Error as e:
            print(f'Error while updating user: {e}')
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.disconnect()

    def delete_user(self, user_id):
        try:
            self.connect()
            cursor = self.connection.cursor()

            delete_query = f"DELETE FROM {self.name_table} WHERE id = %s"
            value = (user_id,)

            cursor.execute(delete_query, value)
            self.connection.commit()

            print(f'{cursor.rowcount} user(s) deleted successfully.')
        except Error as e:
            print(f'Error while deleting user: {e}')
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.disconnect()
