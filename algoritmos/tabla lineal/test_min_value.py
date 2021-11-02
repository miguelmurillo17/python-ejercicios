from array import array

def main():
    scores = array('i')
    scores = array('i',[60,50,95,80,70])
    minValue = min(scores)
    print('Valor mínimo: ',minValue)

def min(arrays):
    # almacena el índice que corresponder al valor más pequeño en el arreglo
    minIndex = 0
    length = len(arrays)
    for i in range(0,length):
        if arrays[i] < arrays[minIndex]:
            minIndex = i
    return arrays[minIndex]

if __name__ == '__main__':
    main()