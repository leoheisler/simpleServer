#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
host = 'localhost'
port = 6789
serverSocket.bind((host,port))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =   serverSocket.accept()
    try:
        #Catch the message
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() 

        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("content-type: txt/html \r\n".encode())
        connectionSocket.send("\r\n".encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 NOT FOUND \r\n".encode())
        connectionSocket.send("content-type: txt/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<h1>404 Not Found</h1>".encode())
        
        #Close client socket
        connectionSocket.close()
      
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 

