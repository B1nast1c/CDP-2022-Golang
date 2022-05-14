import integrate
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Creación del socket UDP

server_address = ('', 5000)

print('Iniciando en el servidor {} puerto {}'.format(*server_address))
sock.bind(server_address)

while True:
    integrate.integralfinal = 0 #Reinicia para evitar la acumulación
    print('\nEsperando parámetros')
    data, address = sock.recvfrom(4096)
    parameters = data.decode().split(' ') #Separa el input de la consola
    if data:
        print("Parametros Recibidos: {!r}".format(data))
        Decoded_Data = integrate.init(parameters[0], float(parameters[1]), float(parameters[2])) #Llama a la integración
        
        print('\nEnviando respuesta')
        sent = sock.sendto(str(Decoded_Data).encode(), address) #Envia la rpta
        print('\nRespuesta Enviada')
