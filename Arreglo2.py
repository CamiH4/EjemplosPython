listaEst = []
resp = "Si"
while(resp.upper() != "NO"):
    tam = len(listaEst)
    print("Elementos guardados: ", tam)
    nombre = (input("Escriba el nombre del estudiante: "))
    listaEst.append(nombre)
    resp = input("Desea aregar mas? SI -NO: ")

    for est in listaEst:
        print(est)