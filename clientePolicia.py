import socket
import json

server_ip = '127.0.0.1'
server_port = 12346

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_ip, server_port))

        filtroTipo = input("---------------------------------------------\n Você deseja encontrar informações de: \n\n 1 - Indivíduo detectado \n 2 - Código da Câmera \n---------------------------------------------\n")
        filtroTipo = int(filtroTipo)
        if filtroTipo == 1:
            filtro = input("Informe o Indivíduo detectado, podendo ser: VERMELHO, VERDE, AZUL, AMARELO, NADA \n")
        elif filtroTipo == 2:
            filtro = input("Informe o código da câmera \n")

        message = {"tipo": filtroTipo, "filtro": filtro}
        client_socket.sendall(json.dumps(message).encode())
        retorno = client_socket.recv(1024).decode()
        print(retorno)
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor.")
    finally:
        client_socket.close()