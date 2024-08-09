# list_comp: [EXPRESSION for VARIABLE in SEQUENCE]
# list_comp: [EXP for VAR in SEQ if CONDITION]

def double_short_words(words):
    return [
        word + word
        for word in words
        if len(word) < 5
        ]

# Multiple Sources and Filtering

colors = ["orange", "purple", "pink"]
toys = ["bike", "basketball", "skateboard", "doll"]


result = [
    color + " " + toy
    for color in colors
    for toy in toys
]
print(result)

ranges = [range(1,7), range(4,12,3), range(-5,9,4)]
parse_range = [
    float(num)
    for subrange in ranges
    for num in subrange
]

print(parse_range)

# Nested One
# empty list
build_color_toys = []
for color in colors:
    for toy in toys:
        build_color_toys.append(color + " " + toy)

print(build_color_toys[0])


# filter out odd positive number
numbers = [ 9, -1, -4, 20, 17, -3 ]

odd_post_filter = [
    num
    for num in numbers
    if num > 0 
    if num % 2 != 0
]

print(odd_post_filter)  

# solving the odd positive filter 
# with helper functions
numbers = [9, -1, -4, 20, 11, -3]

def mult_of_2_or_3(num):
    return (num % 2 == 0) or (num % 3 == 0)

check_num = [
    num 
    for num in numbers
    if mult_of_2_or_3(num)
]
print(check_num)

# using multiple if and for clauses
weights = [0.2, 0.5, 0.9]
values = [27.5, 13.4]
offsets = [4.3, 7.1, 9.5]

multiple_clauses = [
    (weight, value, offset)
    for weight in weights
    for value in values
    for offset in offsets
    if offset > 5.0
    if weight * value < offset]

print(multiple_clauses)

