import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from random import randint
import pprint

fromStartTest = 0
markForBench1 = "Didn't tested"
markForBench2 = "Didn't tested"
markForBench3 = "Didn't tested"
markForBench4 = "Didn't tested"
markForBench5 = "Didn't tested"
marksList = []

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
    markForBench1 = int(100000000000 - int(timeForBench1))
    marksList.append("Mark for test 1: ")
    marksList.append(str(markForBench1))

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
    markForBench2 = int(100000000000 - int(timeForBench2))
    marksList.append("Mark for test 2: ")
    marksList.append(str(markForBench2))

def bench3(n):
    print("Testing your computer with test 3...")
    fromStartTest = time.time_ns()
    a=7**n
    timeForBench3 = time.time_ns() - fromStartTest
    print("Time elapsed for bench 3 is " + str(timeForBench3 / 1000000000) + "s")
    markForBench3 = int(100000000000 - int(timeForBench3))
    marksList.append("Mark for test 3: ")
    marksList.append(str(markForBench3))

def bench4(n):
    print("Testing your computer with test 4...")
    fromStartTest = time.time_ns()
    peremannaa = "Fluffy cats" * n
    timeForBench4 = time.time_ns() - fromStartTest
    print("Time elapsed for bench 4 is " + str(timeForBench4 / 1000000000) + "s")
    markForBench4 = int(100000000000 - int(timeForBench4))
    marksList.append("Mark for test 4: ")
    marksList.append(str(markForBench4))

def benchMem5(chislo1):
    class Meow:
        def __init__(self, i):
            self.i = i

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
            timeForBench5 = time.time_ns() - fromStartTest
            print("Time elapsed for bench 5 is " + str(timeForBench5 / 1000000000) + "s")
            markForBench5 = int(100000000000 - int(timeForBench5))
            marksList.append("Mark for test 5: ")
            marksList.append(str(markForBench5))






input("To start benchmark, press enter...")

Tests = input("Write numbers of tests you like to run \n1 - Testing by 'factorial' system \n2 - testing by fibonacci numbers system \n3 - exponentiation big numbers test \n4 - words multiplying \n5 - memory test - long (16s on my PC) and 'eats' all of your RAM, use only if you REALLY want that \n \nAlso write letter near number \nl - for lite test, \nm - for medium, \nh - for hard \n \nPrint like this: 1m 2h 5l, you can start not only one test \nOn example tests 1 - in medium mode, 2 - in hard and 5 - in lite will start \nPlease, type here...      ").split()

if "1l" in Tests:
    bench1(50000)

if "1m" in Tests:
    bench1(100000)

if "1h" in Tests:
    print("Should not last more, than 1m, if more, stop the test")
    bench1(200000)

if "2l" in Tests:
    bench2(200000)

if "2m" in Tests:
    bench2(500000)

if "2h" in Tests:
    print("Should not last more, than 1m, if more, stop the test")
    bench2(650000)

if "3l" in Tests:
    bench3(2041315)

if "3m" in Tests:
    bench3(5541315)

if "3h" in Tests:
    print("Should not last more, than 1m, if more, stop the test")
    bench3(15541315)

if "4l" in Tests:
    bench4(190000000)

if "4m" in Tests:
    bench4(1000000000)

if "4h" in Tests:
    print("Should not last more, than 1m, if more, stop the test")
    bench4(3000000000)

if "5l" in Tests:
    print("Should not last more, than 3m, yes, it can last 3m, if more, stop the test")
    benchMem5(1)

if "5m" in Tests:
    print("Should not last more, than 3m, yes, it can last 3m, if more, stop the test")
    benchMem5(1)

if "5h" in Tests:
    print("Should not last more, than 3m, yes, it can last 3m, if more, stop the test")
    benchMem5(1)

print("\nYour final marks are:\n")
for i in range(len(marksList)):
    print(marksList[i])
#print(markForBench1, markForBench2, markForBench3, markForBench4, markForBench5)

input("\nTo exit CatBench press enter...")
