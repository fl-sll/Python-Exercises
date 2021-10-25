def convert_to_days():
    hours = float(input("Enter the number of hours: "))
    minutes = float(input("Enter the number of minutes: "))
    seconds = float(input("Enter the number of seconds: "))

    def get_days():
        h1 = hours/24 
        m1 = minutes/(60*24)
        s1 = seconds/(60*60*24)
        days = h1 + m1 + s1
        print("The number of days is", round(days, 4))
    return get_days()

convert_to_days()