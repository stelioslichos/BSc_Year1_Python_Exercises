# first way
def arithmetic_sum(a, d, n):
    s = 0
    while n > 0:
        s += a + (n - 1) * d
        n -= 1
    return s


if __name__ == "__main__":
    result = arithmetic_sum(10, 4, 5)
    print(result)
    
# second way    
def arithmetic_sum(a, d, n):
    s = 0
    for i in range(a, d * n + a, d):
        s += i
    return s


if __name__ == "__main__":
    result = arithmetic_sum(1, 1, 100)
    print(result)