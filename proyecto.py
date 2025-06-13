def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

if __name__ == "__main__":
    x = 10
    y = 5

    print(f"{x} + {y} = {suma(x, y)}")
    print(f"{x} - {y} = {resta(x, y)}")
    print(f"{x} * {y} = {multiplicacion(x, y)}")
    print(f"{x} / {y} = {division(x, y)}")
