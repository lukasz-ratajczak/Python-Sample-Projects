# Benchmark App

# Setup
from time import time

def benchmark(n, fun):
    x = time()
    for i in range(0,n):
        fun()
    y = time()
    return round(y - x, 2)

def test_fun():
    x = 1
    for i in range(1,10000):
        x *= i
    return x

n = 1000
print(benchmark(n, test_fun))