
def make_division_by(n:int):
    """This closure returns a function that returns the division of an X number by N"""
    def divide_by(m:int):
        assert n != 0, "No puedes dividir por cero..."
        return m / n

    return divide_by

def make_division_by_v2(n):
    return lambda x: x/n

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))


if __name__ == "__main__":
    run()