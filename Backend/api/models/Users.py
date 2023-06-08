import mysql.connector
from mysql.connector import Error


class UserDatabase:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
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

    def create_user(self, username, password):
        try:
            self.connect()
            cursor = self.connection.cursor()

            insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            values = (username, password)

            cursor.execute(insert_query, values)
            self.connection.commit()

            print(f'{cursor.rowcount} user(s) created successfully.')
        except Error as e:
            print(f'Error while creating user: {e}')
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.disconnect()

    def update_user(self, user_id, new_password):
        try:
            self.connect()
            cursor = self.connection.cursor()

            update_query = "UPDATE users SET password = %s WHERE id = %s"
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

            delete_query = "DELETE FROM users WHERE id = %s"
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


# Sử dụng lớp UserDatabase để thao tác với cơ sở dữ liệu
db = UserDatabase(host='your_host', database='your_database', user='your_user', password='your_password')

# Thêm mới người dùng
db.create_user(username='john_doe', password='password123')

# Chỉnh sửa thông tin người dùng
db.update_user(user_id=1, new_password='new_password')

# Xóa người dùng
db.delete_user(user_id=1)
