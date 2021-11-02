from array import array

def main():
    scores = array('i')     #crea una matriz de tipo int
    scores = array('i',[90,70,50,80,60,85])
    length = len(scores)
    for i in range(0,length):
        print(scores[i])

if __name__ == '__main__':
    main()
