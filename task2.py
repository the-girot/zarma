import sqlite3


def fetch_users_older_than_30(db_file):
    # Подключение к базе данных SQLite
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Создание таблицы users (если еще не создана)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """)

    # Пример вставки данных в таблицу (удалите или закомментируйте после первого запуска)
    cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 31)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Charlie', 35)")
    conn.commit()

    # Выбор всех пользователей старше 30 лет
    cursor.execute("SELECT name, age FROM users WHERE age > 30")
    results = cursor.fetchall()

    # Вывод результатов
    for row in results:
        print(f"Name: {row[0]}, Age: {row[1]}")

    # Закрытие соединения
    conn.close()


db_file = "example.db"
fetch_users_older_than_30(db_file)
