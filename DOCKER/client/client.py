import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Creación del socket
host = socket.gethostname()
ip = socket.gethostbyname(host)
ip = ip.replace(ip[len(ip)-1:], "2")

server_address = (str(ip), 5000)

funcion = input() #Entrada por consola
x = float(input())
y = float(input())

message = str(funcion + " " + str(x) + " " + str(y))

try:
    print('Enviando los parametros: {!r}'.format(message))
    sent = sock.sendto(message.encode(), server_address) #Envio al cliente, mensaje en bytes 

    data, server = sock.recvfrom(4096)
    print('Integral Computada:  {!r}'.format(data)) #Aqui va el mensaje que se recibe del servidor, en este caso la integral

finally:
    print('Terminando Conexión')
    sock.close()

