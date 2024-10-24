# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Route to serve the main whiteboard page
@app.route('/')
def index():
    return render_template('index.html')

# Handle the drawing event from a user
@socketio.on('draw')
def handle_draw(data):
    # Broadcast the drawing data to all users
    emit('draw', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
