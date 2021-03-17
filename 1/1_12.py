import numpy as np
def main(filename:str):
    with open(filename,'r') as f:
        for line in f.readlines():
            a = list(map(int, line.split()))
            a = np.array(a)

            count = 0
            for i in a:
                if i % 2 == 0:
                    count += 1
            sorted_even = np.ndarray(count).astype(int)
            for i in a:
                if i % 2 == 0:
                    count-=1
                    sorted_even[count] = i

            print(sorted_even)
