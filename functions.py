def add(x, y):
    return x + y


def subtract(x, y):
    return x - y  


def multiply(x, y):
    return x * y


def convert_fahrenheit_to_celsius(fahrenheit):
    if fahrenheit < -459.67:
        raise AssertionError("Farenheit is below absolute 0")
    return multiply(subtract(fahrenheit, 32), 5 / 9)  
