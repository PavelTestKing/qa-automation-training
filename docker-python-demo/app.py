import psycopg2
import os
import time

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5433')
DB_NAME = os.getenv('DB_NAME', 'docker_test_db')
DB_USER = os.getenv('DB_USER', 'docker_user')
DB_PASS = os.getenv('DB_PASS', 'docker_pass')

max_retries = 10
retry_delay = 2

for attempt in range(max_retries):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM docker_learning;")
        rows = cur.fetchall()
        print("Данные из таблицы docker_learning:")
        for row in rows:
            print(row)
        cur.close()
        conn.close()
        break
    except Exception as e:
        print(f"Попытка {attempt+1}/{max_retries}: {e}")
        if attempt < max_retries - 1:
            time.sleep(retry_delay)
        else:
            print("Не удалось подключиться к базе данных после всех попыток.")
            exit(1)