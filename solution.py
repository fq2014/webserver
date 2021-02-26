#import socket module
from socket import *
import sys


def webServer(port=13331):
   serverSocket = socket(AF_INET, SOCK_STREAM)
   serverSocket.bind(('',port))
   serverSocket.listen(1)
   #print ('The server is ready to receive')

   while True:
       connectionSocket, addr = serverSocket.accept()     
       try:
           message = connectionSocket.recv(1024).decode() 
           filename = message.split()[1]
           f = open(filename[1:])
           outputdata = f.read() 
           f.close()
           
           connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode()) 

           for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())
           connectionSocket.send("\r\n".encode())
           connectionSocket.close()

       except IOError:
           connectionSocket.send('HTTP/1.1 404 not found \r\n\r\n'.encode())
           connectionSocket.close()
          
       except BrokenPipeError:
           break
          

   serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(13331)