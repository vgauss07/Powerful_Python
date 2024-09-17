def normal_function(a, b, c):
    print(f'a:{a} b:{b} c:{c}')

numbers = (7, 5, 3)
normal_function(*numbers)

def get_rental_cars(size, doors=4, transmission='automatic'):
    template = "Looking for a {}-door {} car with {} transmission...."
    print(template.format(doors, size, transmission))


get_rental_cars("economy", transmission="manual")


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} -> {value}")

print_kwargs(hero="Homer", antihero="Bart",
            genius="Jeffrey")
            