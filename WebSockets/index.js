let express = require('express')
let app = express()
let httpServ = require('http').createServer(app)
let io = require('socket.io')(httpServ)

let people = [] //Todas las conexiones

//Conexión
io.on('connect', (socket) => {
    people.push(socket)
    console.log("Nuevo conectado")

    socket.on('draw', (drawing) => { //Broadcasting al resto de las conexiones
        people.forEach(
            (person) => {
                person.emit('ondraw', {x: drawing.x, y: drawing.y}) //Evento de dibujo
            }
        )
    })

    socket.on('down', (drawing) => { //Salto del dibujo, no se hacen lineas innecesarias
        people.forEach(
            (person) => {
                person.emit('ondown', {x: drawing.x, y: drawing}) //Evento de click para dibujo
            }
        )
    })
})

app.use(express.static('public')) //Escucha a los archivos dentro de la carpeta public

let PUERTO = 5000
httpServ.listen(PUERTO, () => {console.log("Servidor en el puerto 5000")})