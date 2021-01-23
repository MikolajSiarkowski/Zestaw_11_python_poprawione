import random
import math
def a(n):
    L = list(range(n))
    random.shuffle(L)
    print(L)

def b(n):
    L = list(range(n))
    def mykey(x):
        t = random.randint(-2,2)
        return x+t;
    L=sorted(range(n),key = mykey)
    print(L)

def c(n):
    L=list(range(n))
    def mykey(x):
        t = random.randint(-2,2)
        return x+t;
    L=sorted(range(n),key = mykey,reverse=True)
    print(L)

def d(n):
    L=list(range(n))
    L=[random.gauss(3,4) for i in range(n)]
    print(L)

def e(n):
    L = list(range(n))
    L= [random.randint(0, int(math.sqrt(n))) for i in range(n)]
    print(L)

