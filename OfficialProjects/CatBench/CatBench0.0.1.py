input("To start benchmark, press enter...")
import time
fromStartTest = 0


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



bench1(100000)


input("To exit CatBench press enter...")