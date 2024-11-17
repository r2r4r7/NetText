
# import socket library
import socket
import threading

# Function to handle receiving messages
def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')  # Adjust buffer size as needed
            if message:
                print(message)  # Print Recieved Message
            else:
                break  # Connection closed
        except Exception as e:
            print(f"Error receiving message: {e}")
            break
        
def send_messages(connection):
    while True:
        text = input('>')
    
        if text == 'exit':
            break
        else:
            connection.send(text.encode()) 

# create socket object
s = socket.socket()

port = int(input("\nWhat is the port for the server?\n"))

# bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))         
print ("Socket binded to %s\n" %(port))

# 5 argument specifies the maximum number of queued connections
s.listen(5)     
print ("Socket is listening\n")

# Establish connection with client. 
c, addr = s.accept()
print ('Got connection from\n', addr )

receive_thread = threading.Thread(target=receive_messages, args=(s,))
receive_thread.daemon = True  # Daemonize the thread so it exits with the main program
receive_thread.start()
  
send_messages(c)
 
# send a thank you message to the client. encoding to send byte type. 
c.send('Thank you for connecting\n'.encode()) 
 
# Close the connection with the client 
c.close()