
def make_repeater_of(times:int):
    def repeater(text:str):
        assert type(text) == str, "Solo puedes usar cadenas..."
        return text * times

    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Platzi"))


if __name__ == "__main__":
    run()