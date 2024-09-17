def foo(a, b, x=3, y=2):
    return (a+b)/(x+y)

#--------------------Accepting & Passing Variable Arguments----------------#
def takes_any_args(*args):
    print("Type of args: " + str(type(args)))
    print("Value of args: " + str(args))

takes_any_args("x", "y", "z")
takes_any_args('x', 'y', 'z')
takes_any_args(5, 4, 3, 2, 1)
takes_any_args(["first", "list"], ["another", "list"])

# rewrite takes_any_args function
def takes_a_list(items):
    print("Types of items: " + str(type(items)))
    print("Value of items: " + str(items))

takes_a_list(['x', 'y', 'z'])

#------------------Read files----------------------#
def read_files(*paths):
    data = " "
    for path in paths:
        with open(path) as handle:
            data += handle.read()
    return data