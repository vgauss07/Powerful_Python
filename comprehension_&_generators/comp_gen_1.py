# to optimize memory allocation when creating list
# comprehension, use generator comprehension

squares = [n**2 for n in range(6)]
print(squares)

#___________squares using generators_______________
NUM_SQUARES = 10*1000*1000
gen_squares = (n*n for n in range(NUM_SQUARES))

# gen_squares is equivalent to the function below
def gen_many_squares(limit):
    for n in range(limit):
        yield n * n

# sort a list of user's email
# addresses
"""sorted((user.email for user in user.all_users
        if user.is_active), reverse=True)

## OR
active_emails = (
    user.email 
    for user in user.all_users
    if user.is_active
)

sorted(active_emails)
"""