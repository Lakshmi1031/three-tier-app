import os
import psycopg2
from flask import Flask, render_template, request
import socket

app = Flask(__name__)

# Database configuration (from environment variables)
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "postgres")

# Hardcoded table name for safety
TABLE_NAME = "postgres_user"


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


def create_table():
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    country VARCHAR(255) NOT NULL
                )
            """)
    connection.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    country = request.form['country']

    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO {TABLE_NAME} (name, email, country) VALUES (%s, %s, %s)",
                (name, email, country)
            )
    connection.close()

    return "Data stored successfully!"


@app.route('/getdata')
def get_data():
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {TABLE_NAME}")
            records = cursor.fetchall()
    connection.close()

    return render_template('data.html', records=records)


# Optional: verify round-robin works
@app.route('/whoami')
def whoami():
    return f"Served by container: {socket.gethostname()}\n"


if __name__ == '__main__':
    import os

    # Create DB table only in one container
    if os.getenv("APP_ROLE") == "creator":
        create_table()

    app.run(host='0.0.0.0', port=5000, debug=False)
