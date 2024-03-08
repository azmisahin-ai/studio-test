# app/main.py

import sys
from pathlib import Path



# Projeye ait kök dizini yolu
proje_kok_dizin = Path(__file__).resolve().parents[1]
sys.path.append(str(proje_kok_dizin))

from pathlib import Path
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from src.ana_modul.fonksiyonlar import create_image
from src.yapay_modul import create_image_with_ai
from io import BytesIO
import base64
import threading
import socket
import json

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_image', methods=['POST'])
def create_image_endpoint():
    params = request.json
    result_image = create_image(params)
    
    img_buffer = BytesIO()
    result_image.save(img_buffer, format="PNG")
    img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

    response = {
        'success': True,
        'image': img_str
    }

    return jsonify(response)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('yeni_socket_event')
def handle_yeni_socket_event(data):
    # result_image = create_image(data)
    result_image = create_image_with_ai(data)
    img_buffer = BytesIO()
    result_image.save(img_buffer, format="PNG")
    img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

    emit('yeni_socket_event_response', {'image': img_str})

def socket_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen(5)

    print("Socket server listening on port 5555...")

    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")

        data = client.recv(1024)
        params = json.loads(data.decode('utf-8'))

        result_image = create_image(params)

        img_buffer = BytesIO()
        result_image.save(img_buffer, format="PNG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        emit('yeni_socket_event_response', {'image': img_str})
        
        client.close()

if __name__ == '__main__':
    socket_thread = threading.Thread(target=socket_server)
    socket_thread.start()
    socketio.run(app, debug=True)
