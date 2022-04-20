const dgram = require('dgram');
const client = dgram.createSocket('udp4');

var args = process.argv.slice(2);
let address = args[0]
let port = args[1]
let mensaje = args[2]

const main = function main(){
    client.send(mensaje, 0, mensaje.length, port, address, function(err) { //Envio de información al server
        if (err) {
            console.log(address, port)
            throw err;
        }
        console.log('Mensaje enviado a: ' + address +':'+ port); //Que mensaje se ha enviado y a donde
    })
}

main() //Llamada
