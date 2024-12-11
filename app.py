from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'  # not the best practice but ok for learning
socketio = SocketIO(app)

# Using a dictionary (HashMap) to store messages
message_storage = {}

@app.route('/')
def index():
    return "Welcome to my Chat App!"

@socketio.on('message')
def handle_message(data):
    try:
        user = data.get('user')
        message = data.get('message')
        
        # Store message in our HashMap (dictionary)
        if user in message_storage:
            message_storage[user].append(message)
        else:
            message_storage[user] = [message]
        
        # Emit the message to all clients
        emit('message', {'user': user, 'message': message}, broadcast=True)
        return {'status': 'success', 'message': 'Message sent successfully'}
    
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@socketio.on('get_all_messages')
def get_all_messages(data):
    try:
        user = data.get('user')
        if user in message_storage:
            return {'status': 'success', 'messages': message_storage[user]}
        else:
            return {'status': 'error', 'message': 'No messages found for this user'}
    
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
