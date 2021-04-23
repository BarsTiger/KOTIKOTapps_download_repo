input("To start benchmark, press enter...")
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from random import randint
fromStartTest = 0

class Meow:
    def __init__(self, i):
        self.i = i

def bench1(n):
    print("Testing your computer...")
    fromStartTest = time.time_ns()
    def factorial(kolvo):
        fakt = 1
        for i in range(1, kolvo + 1):
            fakt = fakt * i
        return fakt
    schislo = factorial(n)
    timeForBench1 = time.time_ns() - fromStartTest
    print("Time elapsed for bench 1 is " + str(timeForBench1 / 1000000000) + "s")

def bench2(n):
    print("Testing your computer with test 2...")
    fromStartTest = time.time_ns()
    def fibonacciIt(pokolenia):
        if pokolenia == 1:
            return 0
        perv = 0
        vtor = 1
        result = perv + vtor
        for i in range(1, pokolenia - 1):
            tret = perv + vtor
            result = result + tret
            perv = vtor
            vtor = tret
        return result
    res = fibonacciIt(n)
    timeForBench2 = time.time_ns() - fromStartTest
    print("Time elapsed for bench 2 is " + str(timeForBench2 / 1000000000) + "s")

def bench3(n):
    print("Testing your computer with test 3...")
    fromStartTest = time.time_ns()
    a=7**n
    timeForBench1 = time.time_ns() - fromStartTest
    print("Time elapsed for bench 3 is " + str(timeForBench1 / 1000000000) + "s")

def benchMem4(chislo1):
    def fignia(chislo):
        i = []
        m = 0
        for k in range(chislo):
            m = Meow("Fluffy cats" * 1000000000)
            i.append(m)
        return "a"

    with ThreadPoolExecutor(max_workers=10) as pool:
        print("Testing your computer with test 4 (memory test)...")
        fromStartTest = time.time_ns()
        results = [pool.submit(fignia, 3) for i in range(1)]
        for future in as_completed(results):
            timeForBench1 = time.time_ns() - fromStartTest
            print("Time elapsed for bench 5 is " + str(timeForBench1 / 1000000000) + "s")

def bench5(n, a):
    print("Testing your computer with test 5...")
    fromStartTest = time.time_ns()
    peremannaa = n ** a
    timeForBench1 = time.time_ns() - fromStartTest
    print("Time elapsed for bench 5 is " + str(timeForBench1 / 1000000000) + "s")

bench1(100000)
bench2(500000)
bench3(5541315)
benchMem4(1)
bench5(55555, 1000000)
input("To exit CatBench press enter...")