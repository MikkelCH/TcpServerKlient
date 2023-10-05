from socket import *
import json

def stringToJson(importedstring):
    splitsentence = importedstring.split(';')
    JsonObjekt = {"Method": splitsentence[0], "Tal1": splitsentence[1], "Tal2": splitsentence[2]}
    return json.dumps(JsonObjekt)

serverName = "localhost"
serverPort = 13000 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input sentence: ')

while sentence != ("quit"):
  JsonSentence = stringToJson(sentence).encode() 
  clientSocket.send(JsonSentence)
  modifiedSentence = clientSocket.recv(1024).decode()
  JsonDecoded = json.loads(modifiedSentence)
  print('From server: ', JsonDecoded)
  sentence = input('Input sentence: ')

clientSocket.send(sentence.encode())
clientSocket.close()