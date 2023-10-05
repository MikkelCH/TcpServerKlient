from socket import *

serverName = "localhost" #ip til server
serverPort = 13000 # hvilken port der bruges, skal være det sammen som server
clientSocket = socket(AF_INET, SOCK_STREAM) # AF_INET is the familiy address (Internet protocol v4 addresses (IPV4)) SOCK_STREAM er hvilken type af Socket der skal bruges. TDC eller UDP
clientSocket.connect((serverName, serverPort)) # connect ved brug af serverName og serverPort, det sendes som en touple
sentence = input('Input sentence: ') # Laver en string

while sentence != ("quit"):
  clientSocket.send(sentence.encode()) # Skriver den valgte string. Encode Laver den valgte string til noget andet code.
  modifiedSentence = clientSocket.recv(1024) # recv() = Receive data from the socket. The return value is a bytes object representing the data received. #The maximum amount of data to be received at once is specified by bufsize.
  print('From server: ', modifiedSentence.decode()) # descoder, altså den tager den encodede og decoder den så den returnere til den orginale string.
  sentence = input('Input sentence: ')


clientSocket.send(sentence.encode())
clientSocket.close() # slukker for Socket