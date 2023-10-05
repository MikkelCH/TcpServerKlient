from socket import *
import threading
import random
import json

def calc(sentence):
   jsonSentence = json.loads(sentence)
   protokol = jsonSentence["Method"]

   match protokol:

      case 'Random':
         result = random.randrange(int(jsonSentence["Tal1"]), int(jsonSentence["Tal2"]))
         return result

      case 'Add':
         result = int(jsonSentence["Tal1"]) + int(jsonSentence["Tal2"])
         return result

      case 'Subtract':
         result = int(jsonSentence["Tal1"]) - int(jsonSentence["Tal2"])
         return result

def handleClient(connectionSocket, addr):
   print(addr, 'has connected')
   sentence = connectionSocket.recv(1024).decode()
   while sentence != ('quit'):
      calcSentence = str(calc(sentence))
      jsonSentence = json.dumps(calcSentence)
      connectionSocket.send(jsonSentence.encode())
      sentence = connectionSocket.recv(1024).decode()
      calcSentence = str(calc(sentence))
      jsonSentence = json.dumps(calcSentence)
   connectionSocket.close()

   
serverPort = 13000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()