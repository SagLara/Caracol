def leerMatriz(archivo):
    return [linea[:-1].split(' ') for linea in open(archivo).readlines()]

def girarMatriz(matriz):
    return [[x[y]  for x in matriz] for y in range(-1,((len(matriz[0])+1)*-1),-1)]


def llenarMatriz(lista,matriz,comodin):
    if len(matriz) <=1:
        return lista+[matriz[0][comodin]];
    if (len(matriz[0])!=comodin):
        return llenarMatriz(lista+[matriz[0][comodin]],matriz,comodin+1)
    else:
        return llenarMatriz(lista,girarMatriz(matriz[1:]),0)
 
    
print llenarMatriz([],leerMatriz("matriz.txt"),0)
