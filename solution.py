#import socket module
from socket import *
import sys # In order to terminate the program

#serverPort = 13331
def webServer(port=13331):
   serverSocket = socket(AF_INET, SOCK_STREAM)
   serverSocket.bind(('',port))
   serverSocket.listen(1)
   #print ('The server is ready to receive')# comment all print statements before submission

   #Fill in end

   while True:
       #Establish the connection
       #print('Ready to serve...')
       connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
       try:
           message = connectionSocket.recv(1024).decode() #Fill in start    #Fill in end
           filename = message.split()[1]
           f = open(filename[1:])
           outputdata = f.read() #Fill in start     #Fill in end
           f.close()
           #Send one HTTP header line into socket
           connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())  # http OK message



           #Fill in end

           #Send the content of the requested file to the client
           for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())
           connectionSocket.send("\r\n".encode())
           connectionSocket.close()

       except IOError:
           #Send response message for file not found (404)
           #Fill in start
           connectionSocket.send('HTTP/1.1 404 not found \r\n\r\n'.encode())
           connectionSocket.close()
           #Fill in end
       except BrokenPipeError:
           break
           #Close client socket
           #Fill in start

           #Fill in end

   serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(13331)

