/*package main

import (
	"time"
)

var tiempo time.Duration //Variable global que mide el tiempo de todos las rutinas

type Caballo struct {
	name     string
	actuales int
	limite   int
}

func Init(nombre string, limit int) *Caballo {
	return &Caballo{
		name:     nombre,
		limite:   limit,
		actuales: 1,
	}
}

func main() {
	//caballo, caballo1 := new(Caballo), new(Caballo)
	//caballo1 := Caballo{name: "Mirella", limite: 12, actuales: 1} //Inicialización basica, comun
	//caballo2 := Caballo{name: "Valeria", limite: 10, actuales: 1}
	caballo1 := Init("Mirella", 12)
	caballo2 := Init("Valeria", 10)

	go caballo1.Correr()
	go caballo2.Correr()
	time.Sleep(500 * time.Millisecond)
	defer fmt.Printf("Tiempo final flujo principal: %dmicroseg", tiempo.Microseconds())
}

func Medir(inicio time.Time, c *Caballo) {
	recorrido := time.Since(inicio) //Mide el llamado de la funcion, se usara en el defer
	fmt.Printf("Tiempo de demora %s: %dmicroseg\n", c.name, recorrido.Microseconds())
	tiempo += recorrido
}

func (c *Caballo) Correr() {
	defer Medir(time.Now(), c)
	for idx := 1; idx <= c.limite; idx++ {
		fmt.Printf("%s: %d\n", c.name, idx)
	}
}
*/
