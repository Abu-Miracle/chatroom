import socket
import threading

host = '127.0.0.1'
port = 55561

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

nickname = input("PLEASE CHOOSE A NICKNAME: ")
sock.send(nickname.encode("utf-8"))
    
def write():
        while True:
            message = input()
            if message.startswith('/pm'):
                recipient, msg = message.split(' ', 2)[1:]  # Extract recipient and message
                sock.send(f"/pm {recipient} {msg}".encode("utf-8"))  # Send private message command
            else:
                sock.send(message.encode("utf-8"))  # Send as public message

def receive():
    while True:
        try:
            message = sock.recv(1024).decode("utf-8")
            print(message)
        except ConnectionAbortedError:
            break
        except:
            print("Error")
            sock.close()
            break
    
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()  # Start writing messages
