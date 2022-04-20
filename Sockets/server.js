const dgram = require('dgram');
const server = dgram.createSocket('udp4'); //Creacion de socket servidor

var args = process.argv.slice(2); //Obtener argumentos de la consola
let address = args[0]
let port = args[1]

const main = function () {
    server.on('error', (err) => {
        console.log('Un error ha ocurrido ->\n ${err.stack}') //Manejo de posibles errores de servidor
        server.close()
    })
    
    server.on('message', (info, infomsg) => {
        console.log('Mensaje enviado -> ${info} desde ${infomsg.address}:${infomsg.port}'); //Obtención de mensaje que se envian al sv
    })
    
    server.on('listening', () => { //Inicia el server, y a donde escucha
        const address = server.address();
        console.log('Host y Puerto del server -> ${address.address}:${address.port}');
    })
    
    server.bind({address: address, port: port, exclusive: true}) //Incializacion del server en los puertos de parametros
}

main() //Llamada