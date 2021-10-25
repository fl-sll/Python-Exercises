def convert_to_days():
    hours = float(input("Enter the number of hours: "))
    minutes = float(input("Enter the number of minutes: "))
    seconds = float(input("Enter the number of seconds: "))
    return hours, minutes, seconds

def get_days(hours,minutes,seconds):
    h1 = hours/24 
    m1 = minutes/(60*24)
    s1 = seconds/(60*60*24)
    days = h1 + m1 + s1
    return days

def main():
    h,m,s = convert_to_days()
    days = get_days(h,m,s)
    days1 = round(days, 4)
    print(f"The number of days is: {days1}")

main()