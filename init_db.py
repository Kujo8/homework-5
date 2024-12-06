import sqlite3
from config import DB_PATH 
 
create_post_table = """ 
    CREATE TABLE posts( 
    post_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title TEXT NOT NULL, 
    content TEXT NOT NULL 
); 
""" 
 
connection = sqlite3.connect(DB_PATH) 
cursor = connection.cursor() 
cursor.execute(create_post_table) 
connection.commit() 
connection.close() 
print("таблица posts создана")