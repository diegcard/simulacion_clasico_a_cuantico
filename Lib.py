import cal_matrix_cpmx as cal
from matplotlib import pyplot
import numpy as np

# Programming Drill 3.1.1
def marble(matriz,state,clicks):
    cli = 0
    if len(matriz) == len(state):
        while cli != clicks:
            state = cal.accion_mat(matriz,state)
            cli+=1
        return state
    else:
        return "The size is different"

# Programming Drill 3.2.2

def double(matriz,state,clicks):
    cli = 0
    oring = state
    if len(matriz) == len(state):
        while cli != clicks:
            state = cal.accion_mat(matriz,state)
            cli+=1
        return cal.transicion(state,oring)
    else:
        return "The size is different"


# Programming Drill_probal 3.3.2
def multiple_slits_probal(matrix,vector,n):
    re = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 1:
                return "No es unitaria"
            else:
                case = 0
                while case != n:
                    case+=1
                    re.append(cal.accion_mat(matrix, vector))
    return vector

# Graph
def graph(res,no,dates,n):
    pyplot.title("El estado del sistema es")
    g = range(len(res))
    pyplot.bar(g,dates,height=1,width=0.9)
    pyplot.xlabel("Vertices")
    pyplot.show()
