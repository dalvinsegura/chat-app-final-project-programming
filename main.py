from tkinter import *
import pyrebase
from datetime import datetime
import random
import string



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


def chat_room(chat_code):
    print("Chat room code: ", chat_code)
    print("Name: ", user_name)
    chat_ref = db.child(chat_code)
    chat = Tk()
    chat.title("Chatbot")
    # block the chat window from being resized
    chat.resizable(width=False, height=False)



    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"

    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"

    # Send function
    def send_func():
        user_message = e.get()
        txt.insert(END, "\n" + f'{user_name} -> '  + user_message)
        e.delete(0, END)
        save_message(user_message)
        chat.bind("<Return>", (lambda event: send_func()))

    def save_message(message):
        db.child(chat_code).push({
            'sender': user_name,
            'message': message,
            'timestamp': datetime.now().isoformat()
        })

    lable1 = Label(chat, bg=BG_COLOR, fg=TEXT_COLOR, text=f'Chat room code: {chat_code}', font=FONT_BOLD, pady=10, height=1).grid(
        row=0)

    txt = Text(chat, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)

    scrollbar = Scrollbar(txt, background=BG_COLOR)
    scrollbar.place(relheight=1, relx=0.974)

    # Botón "Leave Chat"
    leave_chat_button = Button(chat, text="Leave Chat", font=FONT_BOLD, bg="red", fg="white", command=chat.destroy)
    leave_chat_button.grid(row=0, column=1, sticky="e")  # Asegurar que el botón "Leave Chat" esté al lado derecho

    e = Entry(chat, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)

    send = Button(chat, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                  command=send_func).grid(row=2, column=1)


    def stream_handler(params):
        # Delete the previous messages
        txt.delete(1.0, END)
        print("Stream handler called")
        # print("Params: ", params)
        messages = db.child(chat_code).get().val()

        if messages is not None and len(messages) > 0:
            print("Messages are not None")
            for message_id, message_data in messages.items():
                txt.insert(END, f"\n{message_data['sender']} -> {message_data['message']}")
        else:
            # Let's fetch the initial messages
            print("Messages are None")
            # If the messages are None, let's add a message to the chat saying that there are no messages without saving it to the database
            txt.insert(END, f"\nBot -> There are no messages in the chat")

    my_stream = db.child("/").stream(stream_handler)
    chat.mainloop()


def create_chat():
    # Forget the main frame
    lable1.pack_forget()
    description_label.pack_forget()
    create_chat_button.pack_forget()
    join_chat_label.pack_forget()
    join_chat_entry.pack_forget()
    join_chat_button.pack_forget()
    go_back_button.pack_forget()
    current_name_label.pack_forget()
    name_label.pack_forget()
    name_entry.pack_forget()
    join_button.pack_forget()
    # root.destroy()

    #Let's generate a random chat code: 6 characters long with uppercase letters and digits. Example: 'AB3CD4'
    random_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    chat_room(random_code)



def join_chat():
    chat_code = join_chat_entry.get()
    #Let's check if the chat exists in the database
    chat_ref = db.child(chat_code)
    if chat_ref.get().val() is not None:
        # root.destroy()
        chat_room(chat_code)
    else:
        print(f"Chat '{chat_code}' does not exist.")



BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

root = Tk()
root.title("Chatbot")
root.geometry("800x400")
root.configure(bg=BG_COLOR)
root.resizable(width=False, height=False)


def show_main_frame():
    main_frame.pack()


def join_or_create():
    global user_name
    user_name = name_entry.get()
    if user_name:
        name_label.pack_forget()
        name_entry.pack_forget()
        join_button.pack_forget()

        create_chat_button.pack(
            side=TOP, padx=10, pady=30
        )
        join_chat_label.pack(
            side=TOP, padx=20, pady=5,
        )
        join_chat_entry.pack(
            padx=200, pady=5,
            side=TOP,
            anchor="center",
            fill=X
        )
        join_chat_button.pack(
            padx=200, pady=5,
            side=TOP,
            anchor="center",
            fill=X
        )

        # current_name_label.pack(
        #     side=BOTTOM, padx=0, pady=0,
        #     text=f"Nombre actual: {user_name}",
        # )

        current_name_label.insert(END, f"Nombre actual: {user_name}")
        current_name_label.pack(side=BOTTOM, padx=20, pady=5)
        current_name_label.config(state=DISABLED)
        # go_back_button.pack(side=BOTTOM, padx=20, pady=5)




def show_main_frame():
    create_chat_button.pack_forget()
    join_chat_label.pack_forget()
    join_chat_entry.pack_forget()
    join_chat_button.pack_forget()
    go_back_button.pack_forget()
    current_name_label.pack_forget()
    name_label.pack(side=TOP, padx=10, pady=20, anchor="w", fill=X)
    name_entry.pack(side=TOP, padx=150, pady=0, fill=X, anchor="w")
    join_button.pack(side=TOP, padx=150, pady=5, fill=X, anchor="w")




lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to Dalvin's Chat App", font="Helvetica 18 bold", pady=10,
               height=1)
lable1.pack(side=TOP, padx=10, pady=0)

description_label = Label(root, bg=BG_COLOR, fg=TEXT_COLOR,
                          text="Introduce tu nombre para poder identificarte dentro de un chat room",
                          font="Helvetica 12")
description_label.pack(side=TOP, padx=10, pady=10)

name_label = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Introduce your public nickname:", font=FONT_BOLD)
name_label.pack(side=TOP, padx=10, pady=20, anchor="w", fill=X)

name_entry = Entry(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
name_entry.pack(side=TOP, padx=150, pady=0, fill=X, anchor="w")

join_button = Button(root, text="Join/Create Chat", font=FONT_BOLD, bg=BG_GRAY, command=join_or_create)
join_button.pack(side=TOP, padx=150, pady=5, fill=X, anchor="w")

create_chat_button = Button(root, text="Create Chat", font=FONT_BOLD, bg=BG_GRAY, command=create_chat)

join_chat_label = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Enter chat code:", font=FONT_BOLD)

join_chat_entry = Entry(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
join_chat_entry.insert(0, "Introduce el código del chat")
join_chat_entry.bind("<FocusIn>", lambda args: join_chat_entry.delete('0', 'end'))

join_chat_button = Button(root, text="Join", font=FONT_BOLD, bg=BG_GRAY, command=join_chat)

current_name_label = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, bd=0)

go_back_button = Button(root, text="Volver Atrás", font="Helvetica 13 bold", fg="#fff", bg=BG_COLOR, bd=0,
                        command=show_main_frame)
# go_back_button.pack(side=BOTTOM, padx=20, pady=5)

chat_frame = Frame(root)


root.mainloop()
