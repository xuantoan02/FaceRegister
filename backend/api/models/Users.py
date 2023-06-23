import mysql.connector
from mysql.connector import Error
from pydantic import BaseModel
from core.Security import HashAlgorithm
from core import config


class User(BaseModel):
    email: str = None
    user_name: str
    password: str


class Db:
    def __init__(self, name_table):
        self.connection = None
        self.host = config.HOST
        self.database = config.DATABASE
        self.admin = config.ADMIN
        self.password = config.PASSWORD
        self.name_table = name_table

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.admin,
                password=self.password
            )
        except Error as e:
            print(f'Error while connecting to MySQL: {e}')

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()


class FaceManager(Db):
    def __init__(self, name_table):
        super().__init__(name_table)

    def create_face_feature(self, id_user, feature):
        message = None
        self.connect()
        cursor = self.connection.cursor()
        try:
            insert_query = f"INSERT INTO {self.name_table} (user_id, feature) VALUES (%s, %s)"
            values = (id_user, feature)
            cursor.execute(insert_query, values)
            self.connection.commit()
            message = f'face_feature of {id_user} created successfully.'
        except Error as e:
            print(f'Error while creating user: {e}')
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.disconnect()
        return message

    def get_user(self, user_id):
        row: tuple = ()
        self.connect()
        cursor = self.connection.cursor()
        try:
            select_query = f"SELECT * FROM  {self.name_table} WHERE user_id = '{user_id}' LIMIT 1"
            cursor.execute(select_query)
            row = cursor.fetchone()
            self.connection.commit()
        except Error as e:
            print(f'Error while get user: {e}')
        finally:
            if self.connection.is_connected():
                cursor.close()
        return row

    def update_face_feature(self, user_id, new_feature):
        self.connect()
        cursor = self.connection.cursor()
        try:
            update_query = f"UPDATE {self.name_table} SET feature = %s WHERE user_id = %s"
            values = (new_feature, user_id)

            cursor.execute(update_query, values)
            self.connection.commit()

        except Error as e:
            print(f'Error while updating user: {e}')
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.disconnect()


class UserManager(Db):
    def __init__(self, name_table):
        super().__init__(name_table)

    def get_user(self, user_name):
        row: tuple = ()
        self.connect()
        cursor = self.connection.cursor()
        try:
            select_query = f"SELECT * FROM  {self.name_table} WHERE name = '{user_name}' LIMIT 1"
            cursor.execute(select_query)
            row = cursor.fetchone()
            self.connection.commit()
        except Error as e:
            print(f'Error while get user: {e}')
        finally:
            if self.connection.is_connected():
                cursor.close()
        return row

    def create_user(self, user: User):

        message = None
        self.connect()
        cursor = self.connection.cursor()
        try:
            insert_query = f"INSERT INTO {self.name_table} (name,email, password) VALUES (%s,%s, %s)"
            password_hash = HashAlgorithm().get_password_hash(user.password, 22)
            values = (user.user_name, user.email, password_hash)
            cursor.execute(insert_query, values)
            self.connection.commit()
            message = f'{user.user_name} created successfully.'

        except Error as e:
            print(f'Error while creating user: {e}')
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.disconnect()
            return message

    def update_user(self, id_user, new_password):
        self.connect()
        cursor = self.connection.cursor()
        try:
            update_query = f"UPDATE {self.name_table} SET password = %s WHERE id = %s"
            values = (new_password, id_user)

            cursor.execute(update_query, values)
            self.connection.commit()
        except Error as e:
            print(f'Error while updating user: {e}')
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.disconnect()

    def delete_user(self, id_user):
        self.connect()
        cursor = self.connection.cursor()
        try:
            delete_query = f"DELETE FROM {self.name_table} WHERE id = %s"
            value = (id_user,)

            cursor.execute(delete_query, value)
            self.connection.commit()

        except Error as e:
            print(f'Error while deleting user: {e}')
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.disconnect()
