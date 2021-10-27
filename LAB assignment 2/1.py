import time

def delay():
    msg = input("Enter a message: ")
    delay = int(input("Enter delay time (in seconds): "))
    delay = time.sleep(delay)
    print(msg)
delay()