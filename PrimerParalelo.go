package main

import (
	"fmt"
	"time"
)

type Caballo struct {
	name     string
	actuales int
	limite   int
}

func main() {
	//caballo, caballo1 := new(Caballo), new(Caballo)
	caballo1 := Caballo{name: "Mirella", limite: 12, actuales: 1}
	caballo2 := Caballo{name: "Valeria", limite: 10, actuales: 1}
	go caballo1.Correr()
	go caballo2.Correr()
	time.Sleep(500 * time.Millisecond)
}

func (c *Caballo) Correr() {
	for idx := 1; idx <= c.limite; idx++ {
		fmt.Printf("%s: %d\n", c.name, idx)
	}
}
