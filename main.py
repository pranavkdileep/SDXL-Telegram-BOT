from flask import Flask, request, jsonify
import subprocess
from get import get_truecaller_info


app = Flask(__name__)

@app.route('/', methods=['GET'])
def run_app():
    phone_number = request.args.get('phone_number')
    if not phone_number:
        subprocess.Popen(['python', 'app.py'])
        return jsonify({'error': 'phone_number is required'})
    
    info = get_truecaller_info(phone_number)
    return info

if __name__ == '__main__':
    app.run()
