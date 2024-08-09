def print_nums(n, rep=2):
    # initialize value
    i = 1
    while i <= rep:
        print(i)
        i += 1

print_nums(5)


def my_func():
    return [10,12,13]

my_list = my_func()


count = 10
def func():
    global count
    count += 1

func()
print(count)