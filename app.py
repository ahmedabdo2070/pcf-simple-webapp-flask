import os
from flask import Flask
app = Flask(__name__)

port = int(os.getenv("PORT", 8080))

@app.route("/")
def main():
    return "Welcome 1!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

# Test
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
