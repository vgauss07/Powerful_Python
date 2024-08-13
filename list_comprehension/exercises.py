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


"""
Given a list of numbers, remove all odd numbers from the list:
"""
numbers = [3,5,45,97,32,22,10,19,39,43]
result = []
odd_num = []

# print out even numbers
[result.append(num) for num in numbers if num % 2 == 0]

[odd_num.append(num) for num in numbers if num % 2 != 0]
print(odd_num)
print(result)

"""
Create a list of all the consonants in the string “Yellow Yaks 
like yelling and yawning and yesturday they yodled while eating yuky yams”
"""
vowels = "AEIOUaeiou"
word = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
consonants = []
[consonants.append(letter) for letter in word if letter not in vowels]
print(consonants)


