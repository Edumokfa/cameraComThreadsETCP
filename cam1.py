import socket
import json
import random
import time

server_ip = '127.0.0.1'
server_port = 12345

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    time.sleep(5)
    try:
        client_socket.connect((server_ip, server_port))

        with open("random-cameras.json", encoding="utf-8") as meu_json:
            dados = json.load(meu_json)
        
        numAleatorio = random.randint(0,4)
        
        lista_filtrada = [item for item in dados['cameras'] if item['id'] == 1]
        objetoDetectado = lista_filtrada[numAleatorio]
        client_socket.sendall(json.dumps(objetoDetectado).encode())
        modified_message = client_socket.recv(1024).decode()
        print("Objeto identificado:", modified_message)
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor.")
    finally:
        client_socket.close()