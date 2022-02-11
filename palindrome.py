

def is_palindrome(texto: str) -> bool:
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

def run():
    print("Rosa is palindrome: {}".format(is_palindrome("Rosa")))
    print("Ana is palindrome: {}".format(is_palindrome("Ana")))
    print("1000 is palindrome: ".format(is_palindrome(1000)))

if __name__ == "__main__":
    run()

