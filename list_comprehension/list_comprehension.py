# list_comp: [EXPRESSION for VARIABLE in SEQUENCE]
# list_comp: [EXP for VAR in SEQ if CONDITION]

squares = [n*n for n in range(6)]
print(squares)

# define some source sequences
pets = ["dog", "parakeet", "cat", "llama"]
numbers = [9, -1, -4, 20, 11, -3]

# and a helper function
def repeat(s):
    return s + s

#_______list-comprehension_______#
y = [2*m+3 for m in range(10, 20, 2)]
x = [abs(num) for num in numbers]
print(x)
print(y)

z = ["The " +  pet for pet in sorted(pets)]
print(z)

# repeat pets
repeat_ = [repeat(pet) for pet in sorted(pets)]
print(repeat_)

# upper case for pets with letters more than 4
pets_upper = [pet.upper() for pet in pets if len(pet) > 3]
print(pets_upper)

# square for even numbers
even_squares = [n**2 for n in numbers if n % 2 == 0]
print(even_squares)


# palindrome
def palindrome(s):
    return s == s[::-1] # create a reverse string of s

words = ["bib", "bias", "dad", "eye", "deed", "tooth"]

pal_ = [word for word in words if palindrome(word)]
print(pal_)


