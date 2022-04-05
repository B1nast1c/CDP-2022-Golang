package main

import (
	"fmt"
	"math"
	"math/rand"
	"sync"
	"time"
)

var wg sync.WaitGroup //Espera que una colección de rutinas de Go se ejecuten - PARA LA SEGUNDA PARTE
var SIZE int
var tiempoFinal int64
var tiempoInit time.Time
var Jobs chan int
var Workers chan int

type Result struct {
	x1, y1, x2, y2            int
	matriz_1, matriz_2, final [][]int
}

func Init(a, b, c, d int) *Result {
	if b == c {
		temp_1 := make([][]int, a)
		for idx := range temp_1 {
			temp_1[idx] = rand.Perm(b)
		}

		temp_2 := make([][]int, c)
		for idx := range temp_2 {
			temp_2[idx] = rand.Perm(d)
		}

		temp_3 := make([][]int, a)
		for idx := range temp_3 {
			temp_3[idx] = make([]int, d)
		}

		return &Result{
			x1: a, y1: b, x2: c, y2: d,
			matriz_1: temp_1, matriz_2: temp_2, final: temp_3,
		}
	}
	return &Result{}
}

func generarMatrices(num int) (*Result, int) { //Funcion generadora de matrices
	rand.Seed(time.Now().UnixNano())
	a := rand.Intn(num) + 1
	//a, b, c := rand.Intn(num) + 1 MISMA DIMENSION
	SIZE = a
	generado := Init(a, a, a, a) //Genera una matriz cuadrada siempre, acomodado para otros casos
	return generado, a * a
}

func main() {
	var limite int
	fmt.Print("Ingrese limite maximo de dimensiones ")
	fmt.Scan(&limite)
	for idx := 1; idx <= limite; idx++ {
		//tiempoFinal = 0
		productoMatricesClasico(idx)
	}
	wg.Wait()
}

//Resolución de las matrices, a manera básica
func productoMatricesClasico(limit int) *Result {
	matriz, numHilos := generarMatrices(limit)
	Jobs = make(chan int, numHilos)
	Workers = make(chan int, numHilos)

	cantWorkers := math.Ceil(float64(SIZE / 10)) //10 - 500
	wg.Add(int(cantWorkers))                     //Cantidad de workers que va a esperar

	for w := 1; w <= int(cantWorkers); w++ { //Me falta determinar cuantos workers debo crear para lo más optimo unu
		go func(idx int) {
			for jobValue := range Jobs {
				Workers <- jobValue //Manda el valor computado al canal que recibe información
			}
			defer wg.Done()
		}(w)
	}

	for idxf, item := range matriz.final {
		for idxc := range item { //Producto individual va al canal de input
			tiempoInit = time.Now()
			Jobs <- productoIndividual(idxf, idxc, *matriz, tiempoInit) //Se crean hilos individuales para cada elemento de nuestra matriz
		}
	}
	close(Jobs)

	/* for idx := 1; idx <= numHilos; idx++ {
		fmt.Print(<-Workers) //Sale en desorden porque la multiplicación no es secuencial ni es un hilo para cada item - Además un worker se desocupa y sigue actuando
	} */
	defer fmt.Printf("%d %d \n", limit, tiempoFinal)
	//fmt.Print(matriz.matriz_1, matriz.matriz_2, matriz.final)
	//defer fmt.Printf("Tiempo final en microsegundos: %d", tiempoFinal)
	return matriz
}

func productoIndividual(fila int, column int, obj Result, tiempo time.Time) int { //Simplemente hace el cálculo
	for idx := 0; idx < SIZE; idx++ {
		obj.final[fila][column] += obj.matriz_1[fila][idx] * obj.matriz_2[idx][column]
	}
	defer func() {
		recorrido := time.Since(tiempo).Milliseconds()
		tiempoFinal += recorrido
	}()
	return obj.final[fila][column]
}
