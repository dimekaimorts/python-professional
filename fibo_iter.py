
import time

class FiboIter():

    def __init__(self, max:int=None) -> None:
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.counter += 1
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self

            if not self.max:
                return self.aux
            else:
                if self.aux > self.max:
                    raise StopIteration
                else:
                    return self.aux


if __name__ == "__main__":
    fibonacci = FiboIter(0)
    for n in fibonacci:
        print(n)
        time.sleep(1)