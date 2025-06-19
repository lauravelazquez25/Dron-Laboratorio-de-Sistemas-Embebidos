from flask import Flask, render_template, request, jsonify
import control_dron
from gps_reader import gps  # NUEVO

app = Flask(__name__)

@app.route('/gps')
def gps_data():
    return jsonify(gps.obtener_datos())


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accion', methods=['POST'])
def accion():
    comando = request.form['comando']
    control_dron.ejecutar(comando)
    return ('', 204)  # No Content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
