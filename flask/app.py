from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Database configuration
DB_NAME = os.environ.get('DB_NAME','postgres')
DB_USER = os.environ.get('DB_USER','postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD','postgres')
DB_HOST = os.environ.get('DBHOST',"localhost")
DB_PORT = '5432'


def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Connected to the PostgreSQL database successfully")
        return conn
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return None

# Define a route to test the database connection
@app.route('/')
def test_db_connection():
    conn = connect_to_database()
    if conn:
        conn.close()
        return "Database connection successful!"
    else:
        return "Failed to connect to the database."

if __name__ == '__main__':
    
    connect_to_database()
    app.run(debug=True)
    
