import socket			 
import threading

def handle_receive(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Server: {message}")
            else:
                break
        except:
            break  

def handle_send(client_socket):
    while True:
        message = input("Enter message to send: ")
        client_socket.send(message.encode())

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('70.177.142.69', 12345))

# Start threads for sending and receiving
receive_thread = threading.Thread(target=handle_receive, args=(client_socket,))
send_thread = threading.Thread(target=handle_send, args=(client_socket,))

#receive_thread.daemon = True

receive_thread.start()
send_thread.start()

# Keep the main thread running to wait for threads to complete
receive_thread.join()
send_thread.join()

client_socket.close()
