#Compare arrays[j] con arrays[j + 1], si arrays[j]> arrays[j + 1] se intercambian.
from array import array

def main():
    scores = array('i')
    scores = array('i',[60,50,95,80,70])
    sort(scores)
    for score in scores:
        print(score)

def sort(arrays):
    length = len(arrays)
    for j in range(0,length-1):
        for i in range(0,length-1-j):
            if arrays[i] > arrays[i+1]:
                pivot = arrays[i]
                arrays[i] = arrays[i+1]
                arrays[i+1] = pivot

if __name__ == '__main__':
    main()
