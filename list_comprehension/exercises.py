"""

Find all of the numbers from 1-1000 
that are divisible by 7

output: list of numbers
expression: num
var & SEQ: for num in range(1001)

condition: if num % 7 == 0


"""
num_ = [num for num in range(1001) if num % 7 == 0]
print(num_)

"""
''
Find all of the numbers from 1-1000 
that have a 3 in them
"""
num_3 = [num for num in range(1001) if '3' in str(num)]
print(num_3)


"""
Count the number of spaces in string
decompose = 
"""
string = "  "
print(len(string))

spaces = "Jeffrey you have the mind of Christ"
num_of_space = [len(space) for space in spaces if space == " "]
print(num_of_space)