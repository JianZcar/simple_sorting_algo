import random
from time import time


class Color:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

    def __repr__(self):
        return {'red': '🟥',
                'green': '🟩',
                'blue': '🟦',
                'white': '⬜'
                }[self.color]

    def value(self):
        # value should start from 1
        return {'red': 1,
                'green': 4,
                'blue': 3,
                'white': 2
                }[self.color]


def str_to_int(x):
    if x.isdigit():
        return int(x)
    elif x == '':
        return 10
    else:
        print('Integer only!')
        return str_to_int(input("==> "))


def timer(func):
    def wrap_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print('\n')
        print(f'Function {func.__name__!r} executed in {(end-start):.4f}s')
        print('\n')
        return result
    return wrap_func


def random_color(x=None, max_=10):
    x = [Color('red'), Color('green'), Color('blue'), Color('white')] if x is None else x
    container = []
    for i in range(max_):
        container.append(random.choice(x))
    return container


@timer
def sorting(container: list = None):
    container = [Color('')] if container is None else container
    parent, output = {}, []
    for i in container:
        if str(i.value()) not in parent:
            parent[str(i.value())] = [i]
        else:
            parent[str(i.value())].append(i)
    for index in range(len(parent)):
        index += 1
        output.extend(parent[str(index)])
    return output


if __name__ == '__main__':
    print("Just press enter to use default value (10)")
    max__ = str_to_int(input("Enter the number of items in the array ==> "))
    random_list = random_color(max_=max__)
    print(f"unsorted ==> {random_list}")
    print(f"sorted   ==> {sorting(random_list)}")
    pass
