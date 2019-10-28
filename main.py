import math as m
from functools import reduce
from typing import List
from typing import Tuple

def primes_to(x: int) -> List[int]:
    if x < 2:
        return []
    l = [True for i in range(x+1)]
    res = []
    l[0] = False
    l[1] = False
    for i in range(2,x+1):
        if(l[i]):
            res.append(i)
            j = i + i
            while j < x:
                l[j] = False
                j = j + i
    return res



def primes_for(x: int) -> List[int]:
    return primes_to(m.floor(m.sqrt(x)))


def factorize(number: int) -> List[Tuple[int, int]]:
    primes = primes_for(number)
    res = []
    n = number
    for p in primes:
        c = 0
        while n % p == 0:
            c = c + 1
            n = n // p
        if c > 0:
            res.append((p,c))
    return res


def all_factors(prime_factors: List[Tuple[int, int]]) -> List[int]:
    l = [0 for i in range(len(prime_factors))]
    l.append(0)
    res = []
    while True:
        divisor = 1
        for i in range(len(prime_factors)):
            divisor = divisor * (prime_factors[i][0] ** l[i])
        res.append(divisor)
        l[0] = l[0] + 1
        for i in range(len(prime_factors)):
            if l[i] > prime_factors[i][1]:
                l[i] = 0
                l[i + 1] = l[i + 1] + 1
        if l[len(l) - 1] == 1:
            return res


def main():
    num_str = input("Enter number to be factorised: ")
    num_str = "123456789987654321"
    num = int(num_str)
    prime_factors = factorize(num)
    prime_str = ""
    for t in prime_factors:
        prime_str = prime_str + "%d^%d * " % t
    prime_str = prime_str.strip(' *')
    print("\n%d = %s\n" % (num, prime_str))
    factors = all_factors(prime_factors)
    print(factors)
    print("\nAll factors count: %d" % len(factors))


if __name__ == "__main__":
    main()