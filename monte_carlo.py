import random
import math
import sys

def main(num):
    n = int(num)
    c = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        dist = math.sqrt(x**2+y**2)
        if dist <= 1:
            c += 1
    pi = (c/n) * 4
    print(pi)
        

if __name__ == "__main__":
    main(sys.argv[1])
