
from time import sleep

def fibo_gen(max:int=100):
    n1, n2 = 0, 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            counter += 1
            aux = n1 + n2
            n1, n2 = n2, aux
            if not max:
                yield aux
            else:
                if aux > max:
                    raise StopIteration
                else:
                    yield aux

if __name__ == "__main__":
    fibonacci = fibo_gen(16)
    for n in fibonacci:
        print(n)
        sleep(1)


