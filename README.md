# WebSocket Chat Application

This is my implementation of the WebSocket chat application using Flask-SocketIO. 

## How to Run

1. First install the requirements:
```
pip install -r requirements.txt
```

2. Run the application:
```
python app.py
```

## Testing with Postman

To test the WebSocket connections in Postman:

1. Create a new WebSocket request
2. Connect to: ws://localhost:5000
3. Send a message with this format:
```json
{
   "user": "JohnDoe",
   "message": "Hello world!"
}
```

4. To get all messages for a specific user:
```json
{
   "user": "JohnDoe"
}
```

## What I Learned
- How to implement WebSocket server using Flask-SocketIO
- Using HashMap (dictionary in Python) for efficient message storage
- Handling WebSocket events and broadcasting messages
