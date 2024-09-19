from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    lang = request.headers.get('Accept-Language', 'en').split(',')[0]
    messages = {
        'en': "Hello from Flask!",
        'it': "Ciao da Flask!",
        'es': "¡Hola desde Flask!"
    }
    return jsonify({"message": messages.get(lang, messages['en'])})

if __name__ == '__main__':
    app.run(debug=True)