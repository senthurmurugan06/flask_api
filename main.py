from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/helloWorld', methods=['GET'])
def hello_world():
    return "Hello, World!"

@app.route('/api/json', methods=['GET'])
def get_json():
    updated_json = {
        "computer_name": "*",
        "greeting": "Hello, World!",
        "details": {
            "language": "Python",
            "framework": "Flask"
        },
        "endpoints": [
            "/api/helloWorld",
            "/api/json"
        ]
    }
    return jsonify(updated_json)

if __name__ == '__main__':
    app.run(debug=True)
