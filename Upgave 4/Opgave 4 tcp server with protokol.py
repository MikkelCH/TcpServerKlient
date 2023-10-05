from socket import *
import threading
import random

def calc(sentence):
   splitsentence = sentence.split(";")
   protokol = splitsentence[0]

   match protokol:

      case 'Random':
         result = random.randrange(int(splitsentence[1]), int(splitsentence[2]))
         return result

      case 'Add':
         result = int(splitsentence[1]) + int(splitsentence[2])
         return result

      case 'Subtract':
         result = int(splitsentence[1]) - int(splitsentence[2])
         return result


def handleClient(connectionSocket, addr):
   print(addr, 'has connected')
   sentence = connectionSocket.recv(1024).decode()
   while sentence != ('quit'):
      connectionSocket.send(str(calc(sentence)).encode())
      sentence = connectionSocket.recv(1024).decode()
   connectionSocket.close()

   
serverPort = 13000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()