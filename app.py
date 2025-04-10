from flask import Flask,render_template,request,redirect
import mysql.connector

app = Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user ="root",
        password="",
        database="control_tareas"

    )
@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tareas2")
    tareas = cursor.fetchall()
    conn.close()
    return render_template('index.html', actividades=tareas)

@app.route('/add', methods=['POST'])
def add():
    #se instancian dos variables para poder mandar dos datos sin probocar un null que cause error en la conexión 
    actividad = request.form['actividad']  
    fecha = request.form['fecha']  
    conn = get_db_connection()
    cursor = conn.cursor()
    #se insertan los valores 
    cursor.execute("INSERT INTO tareas2 (nombre, fecha) VALUES (%s, %s)", (actividad, fecha))
    conn.commit()
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tareas2 WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

