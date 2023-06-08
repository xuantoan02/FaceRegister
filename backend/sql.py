import mysql.connector
from backend.core.config import *

# Thiết lập thông tin kết nối đến cơ sở dữ liệu
config = {
    'user': USER,
    'password': PASSWORD,
    'host': HOST,
    'database': DATABASE,
    'raise_on_warnings': True
}

# Kết nối đến cơ sở dữ liệu
conn = mysql.connector.connect(**config)
cursor = conn.cursor()
table_name = 'users'
create_table_query = '''
CREATE TABLE {} (
    ID INT(11) AUTO_INCREMENT,
	user_name VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,)

'''.format(table_name)

cursor.execute(create_table_query)
conn.commit()
conn.close()
