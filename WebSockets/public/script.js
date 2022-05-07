let canvas = document.getElementById('canvas');
canvas.width =  window.innerWidth;
canvas.height =  window.innerHeight;

var io = io.connect('http://localhost:5000')

let place = canvas.getContext('2d') //Obtener el input, o lo que se haga o presente

let x
let y
let Movement = false //Si el mause ya no se mueve

window.onmousedown = (move) => { //Si hay click
    place.moveTo(x, y)
    io.emit('down', ({x, y}))
    Movement = true
}

window.onmouseup = (move) => { //No hay click
    Movement = false
}

io.on('ondraw', ({x, y}) => {
    place.lineTo(x, y)
    place.stroke()
})

io.on('ondown', ({x, y}) => {
    place.moveTo(x, y)
})

window.onmousemove = (move) => {
    x = move.clientX
    y = move.clientY
    if (Movement) {
        io.emit("draw", {x, y})
        place.lineTo(x, y)
        place.stroke()   
    }
}