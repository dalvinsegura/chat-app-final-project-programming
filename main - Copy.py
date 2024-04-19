from tkinter import *
import pyrebase
from datetime import datetime

firebase = pyrebase.initialize_app({
    'apiKey': "AIzaSyD2jv9Y-3B7d8Xz8ZyK1i3bF4k3K1zJ6JY",
    'authDomain': "chat-app-python-c1ee4.firebaseapp.com",
    'databaseURL': "https://chat-app-python-c1ee4-default-rtdb.firebaseio.com",
    'projectId': "chat-app-python-c1ee4",
    'storageBucket': "chat-app-python-c1ee4.appspot.com",
    'messagingSenderId': "1052926820610",
    'appId': "1:1052926820610:web:0d1a6d5f3f7e4d1b3c0d8f",
    'measurementId': "G-7V8Z7KZJ3C"

})

db = firebase.database()

root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


# Send function
def send():
    user_message = e.get()
    txt.insert(END, "\n" + "You -> " + user_message)
    e.delete(0, END)
    save_message(user_message)


def save_message(message):
    chat_ref = db.child('chat_messages')
    chat_ref.push({
        'sender': 'user',
        'message': message,
        'timestamp': datetime.now().isoformat()
    })



lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1)

def stream_handler(params):
    # Delete the previous messages
    txt.delete(1.0, END)
    print("Stream handler called")
    print("Params: ", params)
    chat_ref = db.child('chat_messages')
    messages = chat_ref.get().val()
    if messages is not None:
        print("Messages are not None")
        for message_id, message_data in messages.items():
            txt.insert(END, f"\nBot -> {message_data['message']}")
    else:
        # Let's fetch the initial messages
        print("Messages are None")
        #If the messages are None, let's add a message to the chat saying that there are no messages without saving it to the database
        txt.insert(END, f"\nBot -> There are no messages in the chat")

my_stream = db.child("chat_messages").stream(stream_handler, None, "chat_messages")

root.mainloop()
