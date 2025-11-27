from flask import Flask, request, jsonify
from app import handle_task

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    user_input = data.get('input', '')
    result = handle_task(user_input)
    return jsonify({"result": result})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=False)
