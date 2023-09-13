import socket

server_ip = '127.0.0.1'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server_ip, server_port))

    server_socket.listen(1)
    print("Servidor pronto para receber conexões")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexão estabelecida com:", client_address)

        message = client_socket.recv(1024).decode()
        print("String recebida", message)

        client_socket.send(message.encode())

        client_socket.close()
        print("Conexão encerrada com:", client_address)

finally:
    server_socket.close()