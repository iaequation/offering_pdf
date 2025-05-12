from flask import Flask,jsonify,request

app= Flask(__name__)

@app.route('/')
def index():
    return "API funcionando"

@app.route('/run', methods=['POST'])
def run():
    data = request.get_json()
    result = {"mensaje": "Hola, recibí tus datos", "datos": data}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
