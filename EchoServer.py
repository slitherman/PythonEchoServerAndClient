from socket import *
import threading

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('192.168.0.199', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()


def handleClient(connectionSocket, address):
    while True:
        sentence = connectionSocket.recv(1024).decode()
        print(sentence)
        if sentence == "bye":
            break
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    t = threading.Thread(target=handleClient, args=(connectionSocket, addr))
    t.start()







