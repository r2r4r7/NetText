# Import socket module 
import socket			 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = int(input("\nWhat is the port for the server?\n"))

# connect to the server on local computer 
ip = input("\nWhat is the ip address for the server?\n")
s.connect((ip, port)) 

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection 
s.close()	 
