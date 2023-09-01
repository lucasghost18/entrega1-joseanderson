import requests
import psycopg2 as db

import random

class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "postgres",
                "password": "admin",
                "host": "127.0.0.1",
                "port": "5432",
                "database": "postgres"
            }
        }

class Connection(Config):
    def __init__(self):
        super().__init__()
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Erro na conexão", e)
            exit(1)

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
    
class JsonTeste(Connection):
    def __init__(self):
        super().__init__()
    def insert(self, *args):
        try:
            sql = "INSERT INTO todolist (userId, title, completed) VALUES (%s, %s, %s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao inserir", e)



base_url = 'https://jsonplaceholder.typicode.com/todos/5'

response = requests.get(base_url)

data = response.json()
   
if __name__ == "__main__":
    userId = data["userId"]  * random.randint(1, 145266454)
    title = data["title"]
    completed = data["completed"]

    jsonTeste = JsonTeste()
    jsonTeste.insert(userId, title, completed)








    