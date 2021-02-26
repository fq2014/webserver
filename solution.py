from socket import *
import sys
def webServer(port=13331):
   serverSocket = socket(AF_INET, SOCK_STREAM)
   serverSocket.bind(('', port))
   serverSocket.listen(1)
   while True:
	  
       #print('Ready to serve...')
       connectionSocket, addr = serverSocket.accept()
       try:
           message = connectionSocket.recv(1024)
           filename = message.split()[1]
           f = open(filename[1:])
           outputdata = f.read()
           f.close()
		  
           connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
           for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())
           connectionSocket.send("\r\n".encode())
           connectionSocket.close()
       except IOError:
           connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
           connectionSocket.close()
		  
       except BrokenPipeError:
           break
		  
   serverSocket.close()
   sys.exit()
if __name__ == "__main__":
    webServer(port=13331)