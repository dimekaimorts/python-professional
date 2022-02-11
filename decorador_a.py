
def decorador(func):
    def envoltura():
        print("Esto se agrega a mi funcion original")
        func()

    return envoltura


def saludo():
    print("Hola!")


saludo()

saludo_A = decorador(saludo)
saludo_A()