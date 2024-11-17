
# import socket library
import socket

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

# a forever loop until we interrupt it or 
# an error occurs 
while True: 
 
# Establish connection with client. 
  c, addr = s.accept()     
  print ('Got connection from\n', addr )
 
  # send a thank you message to the client. encoding to send byte type. 
  c.send('Thank you for connecting\n'.encode()) 
 
  # Close the connection with the client 
  c.close()
   
  # Breaking once connection closed
  break