from firebase_admin import credentials, initialize_app, db
from datetime import datetime

# Firebase configuration
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_app = initialize_app(cred, {
    'databaseURL': 'https://chat-app-python-c1ee4-default-rtdb.firebaseio.com/'
})

# Let's build the chat app using the terminal. User must insert their name first before showing up the menu for joining or creating a chat room.
# The user can join a chat room or create a new chat room. After joining or creating a chat room, the user can send messages to the chat room.
# The chat room will show all messages sent by the user and other users in the chat room.

# Global variable to store user name
user_name = None

# Function to send a message to a chat
def send_message(chat_ref):
    while True:
        message = input("Enter your message (type '/exit' to leave): ")
        if message == '/exit':
            break
        chat_ref.child('messages').push({
            'sender': user_name,
            'message': message,
            'timestamp': datetime.now().isoformat()
        })

# Function to join a chat
def join_chat():
    chat_name = input("Enter the name of the chat you want to join: ")
    chat_ref = db.reference(f'chats/{chat_name}')
    if chat_ref.get() is not None:
        print(f"Joined chat '{chat_name}'")
        listen_to_messages(chat_ref)
    else:
        print(f"Chat '{chat_name}' does not exist.")

# Function to create a chat
def create_chat():
    chat_name = input("Enter the name of the chat you want to create: ")
    chat_ref = db.reference(f'chats/{chat_name}')
    if chat_ref.get() is None:
        chat_ref.set({
            'created_at': datetime.now().isoformat(),
            'created_by': user_name,
            'messages': []
        })
        print(f"Chat '{chat_name}' created successfully")
        send_message(chat_ref)
    else:
        print(f"Chat '{chat_name}' already exists.")

# Function to send a message to a chat
def send_message(chat_ref):
    while True:
        message = input("Enter your message (type '/exit' to leave): ")
        if message == '/exit':
            break
        chat_ref.child('messages').push({
            'sender': user_name,
            'message': message,
            'timestamp': datetime.now().isoformat()
        })

# Function to join a chat
def join_chat():
    chat_name = input("Enter the name of the chat you want to join: ")
    chat_ref = db.reference(f'chats/{chat_name}')
    if chat_ref.get() is not None:
        print(f"Joined chat '{chat_name}'")
        listen_to_messages(chat_ref)
    else:
        print(f"Chat '{chat_name}' does not exist.")

# Function to create a chat
def create_chat():
    chat_name = input("Enter the name of the chat you want to create: ")
    chat_ref = db.reference(f'chats/{chat_name}')
    if chat_ref.get() is None:
        chat_ref.set({
            'created_at': datetime.now().isoformat(),
            'created_by': user_name,
            'messages': []
        })
        print(f"Chat '{chat_name}' created successfully")
        send_message(chat_ref)
    else:
        print(f"Chat '{chat_name}' already exists.")

# Function to listen to messages in a chat
def listen_to_messages(chat_ref):
    print("Chat messages:")
    chat_ref_messages = chat_ref.child('messages')
    chat_ref_messages.listen(callback)

def callback(event):
    message = event.data
    print(f"({message['timestamp']}) {message['sender']}: {message['message']} ")

# Main loop
while True:
    if user_name is None:
        user_name = input("Enter your name: ")

    print("1. Join a chat")
    print("2. Create a chat")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Joining chat as {user_name}")
        join_chat()
    elif choice == "2":
        print(f"Creating chat as {user_name}")
        create_chat()
    elif choice == "3":
        break
    else:
        print("Invalid choice")

    print()