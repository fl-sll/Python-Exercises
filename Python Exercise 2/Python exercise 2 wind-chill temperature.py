t_a = float(input("Enter the temperature in Farenheit: "))
while True:
    if t_a < -58 or t_a > 41:
        print("Temperature must be between -58F and 41F")
        t_a = float(input("Please re-enter the temperature in Fahrenheit: "))
        continue
    else:
        break

v = float(input("Please enter the windspeed: "))
while True:
    if v < 2:
        print("Speed must be greater than or equal to 2")
        v = float(input("Please re-enter the windspeed (mph): "))
        continue
    else:
        wc = 35.74 + ((0.6215) * (t_a)) - ((35.75) * (v ** 0.16)) + ((0.4275) * (t_a) * (v ** 0.16))
        format_wc = "{:.3f}".format(wc)
        print("The windchill index is", format_wc)
        break 
