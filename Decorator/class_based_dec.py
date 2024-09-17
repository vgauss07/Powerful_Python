class Prefixer:
    def __init__(self, prefix):
        self.prefix = prefix
    def __call__(self, message):
        return self.prefix + message



jeffsays = Prefixer("Jeff says: ")
print(jeffsays("Be the Best!"))

class PrintLog:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print(f'CALLING: {self.func.__name__}')
        return self.func(*args, **kwargs)

@PrintLog
def foo(x):
    print(x+2)

foo(7)

# print fullname and jobtitle
class FullName:
    def __init__(self, name):
        self.name = name
    def __call__(self, *args, **kwargs):
        print(f'CALLING: {self.name.__name__}')
        user_input = input("Enter Full Name: ")
        return self.name(*args, **kwargs)

@FullName
def title(job_title):
    job_title = input("Enter Job Title: ")
    return job_title

print(title("Ml Engineer"))