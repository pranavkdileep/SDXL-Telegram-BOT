from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def run_app():
    subprocess.Popen(['python', 'app.py'])
    return 'App running forever'

if __name__ == '__main__':
    app.run(port=8080)
