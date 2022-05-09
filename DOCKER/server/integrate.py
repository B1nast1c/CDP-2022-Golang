import threading #Uso de hilos

integralfinal = 0 #Variable compartida

def trapecioSimple(func, x, y):
    func2 = func.replace('x', 'y') #Para la evaluación en la función dependiente de los dos límites
    integral = list() #Integral y sus valores
    if x<y:
        integral.append(0.5 * (eval(func) + eval(func2)) * (y-x)) #Suma por cada pequeño pedacito o división
        return integral
    integral.append(0)
    return integral

def trapecioCompuesto(func, x, y, jump):
    global integralfinal
    
    index = x
    suma, x1, y1 = 0, 0, 0
    salto = jump #Exactitud
    integral = 0
    while index < y: #Sumatoria
        if index + salto < y: #Cada mini trapecio
            x1 = index
            y1 = salto + index #Se hace como un b', un sublimite poremos llamarle asi
            suma += trapecioSimple(func, x1, y1)[0] #Llamada
        index += salto
    integralfinal += suma #Acumulación

def init(func, x, y): #Funcion principal
    threads = list() #Lista de hilos
    limit = x
    
    for i in range(int((y-x)/0.1)): #Aqui modificar y ver la cantidad de hilos a generar de manera dinámica
        rango = 0.1 #Rango de separación para los trapecios
        thread = threading.Thread(target=trapecioCompuesto, args=(func, limit, limit+rango, 0.01)) #Llamada con argumentos
        threads.append(thread) #Agregar a la lista
        thread.start() #Inicialización
        limit += rango #Límites
    for i, thread in enumerate(threads):
        thread.join() #Entran
    
    return integralfinal #Retornar Integral