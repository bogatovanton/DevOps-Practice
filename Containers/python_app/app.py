from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Подключение к БД
def get_db():
    return psycopg2.connect(
        host="db",
        database="mydb",
        user="user",
        password="password"
    )

@app.route('/')
def home():
    conn = get_db()
    cur = conn.cursor()
    
    # Проверяем, существует ли таблица
    cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'java_data')")
    table_exists = cur.fetchone()[0]
    
    if table_exists:
        # Читаем данные из таблицы, которую создал Java
        cur.execute("SELECT * FROM java_data")
        rows = cur.fetchall()
        result = "<h1>Данные из базы:</h1><ul>"
        for row in rows:
            result += f"<li>ID: {row[0]}, Сообщение: {row[1]}</li>"
        result += "</ul>"
    else:
        result = "<h1>Таблица ещё не создана</h1>"
    
    cur.close()
    conn.close()
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)