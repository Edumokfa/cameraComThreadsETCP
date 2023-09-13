import socket
import json
import time

server_ip = '127.0.0.1'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server_ip, server_port))

    server_socket.listen(1)
    print("Servidor pronto para receber informações")

    while True:
        client_socket, client_address = server_socket.accept()

        message = client_socket.recv(1024).decode()

        print("Informação recebida", message)
        objetoArquivoJson = json.loads(message)
        objetoArquivoJson["data"] = time.ctime()
        print(objetoArquivoJson)

        with open("dadosLidos.json", 'r+') as meu_json:
            dados = json.load(meu_json)
            
            dados["dadosLidos"].append(objetoArquivoJson)
            meu_json.seek(0)
            json.dump(dados, meu_json, indent = 4)

        client_socket.send(message.encode())

        client_socket.close()
finally:
    server_socket.close()