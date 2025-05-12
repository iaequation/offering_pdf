from flask import Flask,jsonify,request

app= Flask(__name__)

@app.route('/')
def index():
    return "API funcionando"

@app.route('/run', methods=['POST'])
def run():
    data = request.get_json()
    if not data:
        return jsonify ({"mensaje":"No se recibieron datos"}),400
    try:
        result=subprocess.run('python3','prueba.py'],capture_output=True, text=True)
        if result.return.code==0:
            return jsonify({
                "mensaje" : "Datos recibidos y script ejecutado",
                "datos":data,
                "script_output":result.stdout
            })
        else:
            return jsonify({
                "mensaje": "Hubo un error al ejecutar el script",
                "error": result.stderr
            }), 500
    except Exception as e:
        return jsonify({
            "mensaje": "Error al ejecutar el script",
            "error": str(e)
        }), 500
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
