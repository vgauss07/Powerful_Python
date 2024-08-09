import timeit
def loop():
    res = []
    for i in range(100000):
        res.append(i * i)
    return sum(res)

def comprehension():
    return sum([i * i for i in range(100000)])

def generator():
    return sum(i * 8 for i in range(100000))

timeit.timeit(loop())
timeit.timeit(comprehension())
timeit.timeit(generator())