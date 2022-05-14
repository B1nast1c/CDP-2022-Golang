from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count

def trapecioSimple(func, x, y):
    func2 = func.replace('x', 'y') #Para la evaluación en la función dependiente de los dos límites
    integral = list() #Integral y sus valores
    if x<y:
        integral.append(0.5 * (eval(func) + eval(func2)) * (y-x)) #Suma por cada pequeño pedacito o división
        return integral
    integral.append(0)
    return integral

def trapecioCompuesto(func, x, y, jump):
    index = x
    suma, x1, y1 = 0, 0, 0
    salto = jump #Exactitud
    while index < y: #Sumatoria
        if index + salto < y: #Cada mini trapecio
            x1 = index
            y1 = salto + index #Se hace como un b', un sublimite poremos llamarle asi
            suma += trapecioSimple(func, x1, y1)[0] #Llamada
        index += salto
    return suma

def init(func, x, y): #Funcion principal
    integrales = []
    cpus = cpu_count()
    limit = 1
    jump = y - x
    Trapecios = 0
    index = 1
    
    init = trapecioCompuesto(func, x, y, jump)
    limit += 1
    integrales.append(float("{:.5f}".format(float(init))))
    
    while True:
        with ThreadPoolExecutor(10**cpus) as executor:
            if index%cpus == 0:
                second = executor.submit(trapecioCompuesto, func, x, y, jump/limit)
                #Colocarlo a la posición integrales -1
                integrales.insert(limit-1, float("{:.5f}".format(float(second.result().__str__()))))
                if integrales[-1] == integrales[-2]:
                    Trapecios = int((jump/limit)**-1)
                    break
            limit += 1
        index += 1
    return (Trapecios, integrales[-1]) #Tambien retorna la cantidad de trapecios más adecuada
