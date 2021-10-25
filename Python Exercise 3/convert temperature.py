def convert_temp():
    f = float(input("Enter a temperature in Fahrenheit: "))
    return f

def convert_to_celcius(f):
    return ((5/9)*(f - 32))
        
def convert_to_kelvin(c):
    return c + 273.15

f = convert_temp()
c = convert_to_celcius(f)
k = convert_to_kelvin(c)
print(f"The temperature in Fahrenheit is {f}")
print(f"The temperature in Celcius is: {c}")
print(f"The tempreature in kelvin is: {k}")