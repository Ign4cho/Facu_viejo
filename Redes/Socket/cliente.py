import socket

# Crea un objeto socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtiene el nombre de la máquina local
host = socket.gethostname()

port = 9999

# Enlaza al puerto
serversocket.bind((host, port))

# Coloca el servidor en modo de escucha
serversocket.listen(5)

while True:
    # Establece una conexión con el cliente
    (clientsocket, addr) = serversocket.accept()

    print("Conexión establecida con %s" % str(addr))

    # Aquí es donde recibimos una cadena de texto del cliente
    received_message = clientsocket.recv(1024).decode('utf-8')
    print("Mensaje recibido del cliente: ", received_message)

    msg = received_message.upper()
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
