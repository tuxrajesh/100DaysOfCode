def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(f"Sum : {add(1, 2, 3, 4, 5)}")

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)

def all_aboard(a, *args, **kwargs):
    print(a, args, kwargs)

all_aboard(4, 7, 3, 0, x=10, y=5)