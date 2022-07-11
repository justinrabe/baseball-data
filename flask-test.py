from flask import Flask, render_template
import psycopg2
try:
    conn = psycopg2.connect(database="baseball_data", user="root", password = "root", host="localhost")
    print("Connection Successful!")
except:
    print("Connection Failed!")
curr = conn.cursor()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def v_pitching():
    curr.execute("SELECT * FROM pitching limit 100")
    data = curr.fetchall()
    return render_template('pitching.html', data=data)


